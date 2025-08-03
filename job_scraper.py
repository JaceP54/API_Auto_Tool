import requests
import json
import pandas as pd

response_API = requests.get('https://remoteok.com/api')
data = response_API.json()

# Get the first 5 actual job listings (skipping metadata at index 0)
jobs = data[1:6]

raw_json_strings = [json.dumps(job, indent=2) for job in jobs]


with pd.ExcelWriter("remote_jobs_dual.xlsx") as writer:
    # Raw data
    pd.DataFrame(raw_json_strings, columns=["Raw JSON"]).to_excel(writer, sheet_name="Raw", index=False)

    # Parsed data
    parsed = pd.DataFrame([
        {
            "Position": job.get("position", "N/A"),
            "Company": job.get("company", "N/A"),
            "Location": job.get("location", "N/A"),
            "Tags": ", ".join(job.get("tags", [])),
            "URL": job.get("url", "N/A")
        }
        for job in data[1:]
    ])
    parsed.to_excel(writer, sheet_name="Parsed", index=False)


for job in jobs:
    slug = job.get('position', "N/A")
    company = job.get("company", "N/A")
    url = job.get("url", "N/A")

    print(f"{slug} at {company} — {url}")

keyword = input("Enter a keyword to find a job listing ")