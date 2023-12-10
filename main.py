
from bardapi import BardCookies
import requests
import json


with open("keys.json","r") as keys:
    jsonData = json.load(keys)

bard = BardCookies(cookie_dict=jsonData["cookie_dict"])

topic = input("Enter Topic for Linkedin Post: ")
BardOutput = (bard.get_answer("Act as a professional Linkedin content writer who has expertise in writing authentic and engaging content. \
                              You will write an linkedin post on "+str(topic)+",trying to maximize likes and comments. You can use historical\
                                  stories as well as future predictions.")['content'])
print(BardOutput)
    
while True:
    next_instruction = str(input("Press 'Enter' to approve or enter your next instruction: "))
    if len(next_instruction) == 0:
        break
    BardOutput = (bard.get_answer(next_instruction)['content'])
    print(BardOutput)

api_url = 'https://api.linkedin.com/v2/ugcPosts'

headers = {
    'Authorization': f'Bearer {jsonData["access_token"]}',
    'Connection': 'Keep-Alive',
    'Content-Type': 'application/json',
}

post_body = {
    "author": "urn:li:person:_SzLgAE0Yg",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": BardOutput #"Hello World! This is my Second Automated Share on LinkedIn!"#BardOutput
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(api_url, headers=headers, json=post_body)
if response.status_code == 201:
    print('Post successfully created!')
else:
    print(f'Post creation failed with status code {response.status_code}: {response.text}')
