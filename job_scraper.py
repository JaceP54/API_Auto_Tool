import requests
import json
import pandas as pd
import csv
from datetime import datetime

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

keyword = input("Enter a keyword to find a job listing: ").lower()
found_rows = []


with open('remote_jobs_parsed.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if keyword in row['Position'].lower() or keyword in row['Tags'].lower():
            found_rows.append(row)

print(f"\nJobs matching {keyword}:\n")
for row in found_rows:
    print(f"{row['Position']} at {row['Company']} — {row['URL']}")

filename = f"jobs_{keyword}_{datetime.now().strftime('%Y-%m-%d')}.csv"
pd.DataFrame(found_rows).to_csv(filename, index=False)

print(filename)