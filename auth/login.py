import json

import requests
from bs4 import BeautifulSoup

url = "http://localhost:8080/"
# url = "http:///172.17.9.60:8080/aaa"
api = "aaa"
headers = {
    'content-type': 'application/json'
}

body = {
    'userId': 'systemAdmin',
    'password': '1qaz2wsx',
    'userAgent': 'WEB',
}
body1 = {
    'userId': 'friend01',
    'password': '1qaz2wsx',
    'userAgent': 'WEB',
}
body2 = {
    'userId': 'friend02',
    'password': '1qaz2wsx',
    'userAgent': 'WEB',
}

res = requests.post(url + api, data = json.dumps(body), headers=headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(url)

print('+=============================================+')
print(body.get('userId'))
print(soup1)
print('+=============================================+')

res = requests.post(url + api, data = json.dumps(body1), headers=headers)

soup2 = BeautifulSoup(res.text, "html.parser")
print(body1.get('userId'))
print(soup2)
print('+=============================================+')

res = requests.post(url + api, data = json.dumps(body2), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")
print(body2.get('userId'))
print(soup2)
print('+=============================================+')
