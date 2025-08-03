import requests
import json
import pandas as pd

response_API = requests.get('https://remoteok.com/api')
data = response_API.json()

# Get the first 5 actual job listings (skipping metadata at index 0)
jobs = data[1:6]

raw_json_strings = [json.dumps(job, indent=2) for job in data[1:6]]  # skipping metadata

# Create a DataFrame with one column
df = pd.DataFrame(raw_json_strings, columns=["Raw API Data"])

# Save to Excel
file_name = "remote_job_raw.xlsx"
df.to_excel(file_name, index=False)


for job in jobs:
    slug = job.get('position', "N/A")
    company = job.get("company", "N/A")
    url = job.get("url", "N/A")

    print(f"{slug} at {company} — {url}")

keyword = input("Enter a keyword to find a job listing ")