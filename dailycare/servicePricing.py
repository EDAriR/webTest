import login

import json
import requests
from bs4 import BeautifulSoup

authorization = login.authorization
api = "servicePricing"

headers = {
    'content-type': 'application/json',
    'authorization': authorization
}

body = {
    "hospitalSequence":1,"caseManagerReport":1,"doctorReport":2,"uploadECG":3,
    "uploadBP":4,"uploadGlucose":5,"uploadSpO2":6,"download":7,
    "paperConsultation":8,"phoneConsultation":9,"status":"ENABLED"
}


res = requests.post(login.url + api, data = json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print(soup)