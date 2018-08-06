import login

import json
import requests
from bs4 import BeautifulSoup

authorization = login.authorization
api = "resident"

headers = {
    'content-type': 'application/json',
    'authorization': authorization
}

body = {
    "hospitalSequence":1,
    "payment":"RESIDENT",
    "emailId":"robert09@gmail.com",
    "password":"1qaz2wsx",
    "name":"RESIDENT",
    "mobilePhone":"0287654321",
    "status":"ENABLED"
}

res = requests.post(login.url + api, data = json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print(soup)