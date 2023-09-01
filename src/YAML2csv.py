import csv
import yaml

# Read the YAML file from your local machine
with open('legislators-historical.yaml', 'r', encoding='utf-8') as yaml_file:
    data = yaml.safe_load(yaml_file)

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
