import login

import json
import requests
from bs4 import BeautifulSoup

authorization = login.authorization
api = "deviceRentalPricing"

headers = {
    'content-type': 'application/json',
    'authorization': authorization
}

body = {
    "deviceName":1,
    "period":"ONE_WEEK",
    "point":1,
    "status":"ENABLED"
}


res = requests.post(login.url + api, data = json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print(soup)