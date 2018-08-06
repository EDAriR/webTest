import json

import requests
from bs4 import BeautifulSoup

url = "http://localhost:8083/cip/ownership/"
api = "request"  # post

headers = {
    'content-type': 'application/json',
    'Authorization': 'WEB 9c6e36e0-4731-403e-b96e-0ee02395b795'
}

body = {
    "userId": "friend01",
    "type": "VITALS"
}

res = requests.post(url + api, data=json.dumps(body), headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

print(res.text)

print('+-POST /cip/ownership/request-----------------+')
print(body.get('userId'))
print(soup)
print('+=============================================+')

api = "request?keyword=ow"  # GET

getRes = requests.get(url + api, headers=headers)
getSoup = BeautifulSoup(res.text, "html.parser")

print(getRes.text)
print('+-GET /cip/ownership/request no Request Query String -----------------+')
# print(body.get('userId'))
print(getSoup)
print('+=============================================+')

api = "consent/"  # PUT

friend01headers = {
    'content-type': 'application/json',
    'Authorization': 'WEB f2498903-4658-4335-898a-a5cd22b644ba'
}

agreeBody = {
    "status": "CONSENT"
}

agreeRes = requests.put(url + api + res.json().get("ownershipId"), data=json.dumps(agreeBody), headers=friend01headers)
agreeSoup = BeautifulSoup(agreeRes.text, "html.parser")

print(agreeRes.text)

print('+-PUT /cip/ownership/consent/:ownershipId-----+')
# print(body.get('userId'))
print(agreeSoup)
print('+=============================================+')

api = "request?ownershipIds="  # DELETE

deleteRes = requests.delete(url + api + res.json().get("ownershipId"), data=json.dumps(agreeBody), headers=headers)
deleteSoup = BeautifulSoup(deleteRes.text, "html.parser")

print(deleteRes.status_code)

print('+-DELETE /ownership/request-----+')
# print(body.get('userId'))
print(deleteSoup)
print('+=============================================+')

api = "consent"  # GET
api = "consent"  # DELETE
