import csv
import yaml
import requests

# URL of the YAML file
yaml_url = 'https://theunitedstates.io/congress-legislators/legislators-historical.yaml'

# Fetch the YAML content from the URL
response = requests.get(yaml_url)
yaml_content = response.text

# Load YAML content
data = yaml.safe_load(yaml_content)

# CSV file path
csv_file_path = 'legislators.csv'

# Extract headers
headers = set()
for entry in data:
    headers.update(entry.keys())

# Write data to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=sorted(headers))
    csv_writer.writeheader()
    csv_writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been created.")
