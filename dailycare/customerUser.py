import login

import json
import requests
from bs4 import BeautifulSoup

authorization = login.authorization
api = "customerUser"

headers = {
    'content-type': 'application/json',
    'authorization': authorization
}

body = {
    "id": 'sincerered',
    "name": 'sincerered',
    "password": '1060821',
    "gender": 'MALE',
    "birthday": '2017-08-21T06:05:09.365Z',
    "homePhone": '111111111',
    "companyPhone": '111111111',
    "mobilePhone": '1111111111',
    "email": "chenken_chen@syntrontech.com",
    "address": 'sdafasdfasd',
    "emergencyContactPerson": 'fasdf',
    "emergencyContactHomePhone": '111111111',
    "emergencyContactMobilePhone": '1111111111',
    "emergencyContactEmail": 'sdaf@sadf.sdaf',
    "from": 'HOSPITAL',
    "fromComment": 'sdafasdf',
    "medicationComment": 'sdfa',
    "comment": 'sdaf'

}

res = requests.post(login.url + api, data=json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

if(res.status_code == 200):
    print("create customerUser ok")

print(soup)
