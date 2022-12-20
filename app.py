import requests
import json
import os

prompt = """Summarize this incident chat transcript 

[Person 1] Hi, we've been seeing reports of down time in our Europe region. Can anyone check?
[Person 2] Yes, I'm on it.
[Person 3] I'm also looking into it.
[Person 4] I can look into this too.
[Person 5] I just ran a diagnostic on our servers and everything looks good from here.
[Person 6] I'm checking the databases now.
[Person 7] We'll need to talk to the hosting provider to get more information about what's going on.
[Person 8] I just checked with our server engineers and they said that the issue appears to be related to the DNS servers. They are working on resolving the issue now.
[Person 1] Thanks everyone for all your help. We'll keep monitoring the situation and inform everyone if anything changes."""

api_key = os.getenv("FOREFRONT_API_KEY")

headers = {
  "Authorization": "Bearer " + api_key,
  "Content-Type": "application/json"
}

body = {
	"compression_level": 5,
	"text": prompt
	}

res = requests.post(
  "https://solutions.forefront.ai/v1/organization/DbmudTXQWYwZ/summarize",
  json=body,
  headers=headers
)

data = res.json()
if ('summary' in data):
  summary = data['summary']
  print(summary)
