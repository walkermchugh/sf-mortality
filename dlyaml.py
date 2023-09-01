import requests

yaml_url = "https://theunitedstates.io/congress-legislators/legislators-historical.yaml"
output_file_path = "legislators-historical.yaml"

response = requests.get(yaml_url)

if response.status_code == 200:
    with open(output_file_path, "wb") as output_file:
        output_file.write(response.content)
    print(f"YAML file downloaded and saved as '{output_file_path}'")
else:
    print(f"Failed to download YAML file. Status code: {response.status_code}")
