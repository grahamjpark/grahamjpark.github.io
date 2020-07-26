import os
import json
import requests

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

querystring = {"screen_name":"grahamjpark","count":"5"}

payload = ""
headers = {
    'authorization': "Bearer {}".format(os.environ['TWITTER_TOKEN'])
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

with open('tweets.json', 'w') as outfile:
    json.dump(response.json(), outfile, indent=4)
