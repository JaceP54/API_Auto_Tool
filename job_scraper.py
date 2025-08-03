import requests
import json
import pandas as pd
import csv

response_API = requests.get('https://remoteok.com/api')
data = response_API.json()

# Get the first 5 actual job listings (skipping metadata at index 0)
jobs = data[1:6]

raw_json_strings = [json.dumps(job, indent=2) for job in jobs]


pd.DataFrame(raw_json_strings, columns=["Raw JSON"]).to_csv("remote_jobs_raw.csv", index=False)

# Save parsed data for all jobs to CSV
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
parsed.to_csv("remote_jobs_parsed.csv", index=False)



for job in jobs:
    slug = job.get('position', "N/A")
    company = job.get("company", "N/A")
    url = job.get("url", "N/A")

    print(f"{slug} at {company} — {url}")

#keyword = input("Enter a keyword to find a job listing ")