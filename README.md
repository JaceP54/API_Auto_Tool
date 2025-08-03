README.md
RemoteOK Job Scraper
This Python script pulls live remote job listings from the RemoteOK API, filters them based on a user-provided keyword, and saves both raw and filtered data to CSV files. It’s a lightweight, command-line tool ideal for tracking job opportunities in real time.

Features
Connects to the RemoteOK public API

Retrieves and parses remote job listings

Saves:

Raw JSON for each job (for auditing or backup)

Parsed, readable job listings to remote_jobs_parsed.csv

Prompts the user for a keyword (e.g. "python", "flask", "developer")

Filters jobs by keyword match in position title or tags

Displays matching jobs in the console

Exports filtered results to a timestamped CSV (e.g., jobs_python_2025-08-01.csv)

Technologies Used
Python 3

requests – to access the RemoteOK API

json – to handle raw API responses

csv – to read and write job data

pandas – for structured data export and reporting

datetime – to timestamp output filenames

