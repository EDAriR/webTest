import login

import json
import requests
from bs4 import BeautifulSoup

authorization = login.authorization
api = "deviceRental"

headers = {
    'content-type': 'application/json',
    'authorization': authorization
}

body = {
    "userSequence":1,
    "deviceRentalPricingSequence":1,
    "deviceSerial":1,
    "comment":"",
}


res = requests.post(login.url + api, data = json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print(soup)