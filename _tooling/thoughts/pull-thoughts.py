import os
import json
import requests

url = "https://api.airtable.com/v0/app0FmuCNjKX26oal/Thoughts"

headers = {
    'authorization': "Bearer {}".format(os.environ['AIRTABLE_TOKEN'])
}

response = requests.request("GET", url, headers=headers)

print(response.text)

dir_path = os.path.dirname(os.path.realpath(__file__))

thoughts = [record["fields"] for record in response.json()["records"]]

with open(os.path.join(dir_path, 'thoughts.json'), 'w') as outfile:
    json.dump(thoughts, outfile, indent=4)