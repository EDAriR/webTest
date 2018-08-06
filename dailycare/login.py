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
    'account': 'systemAdmin',
    'password': '1qaz2wsx',
    'userAgent': 'WEB',
}
body1 = {
    'account': 'test_ownership01',
    'password': '1qaz2wsx',
    'userAgent': 'WEB',
}
body2 = {
    'account': 'test_ownership06',
    'password': '1qaz2wsx',
    'userAgent': 'WEB',
}

res = requests.post(url + api, data=json.dumps(body), headers=headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(url)

print('+=============================================+')
print(body.get('account'))
print(soup1)
print('+=============================================+')

res = requests.post(url + api, data=json.dumps(body1), headers=headers)

soup2 = BeautifulSoup(res.text, "html.parser")
print(body1.get('account'))
print(soup2)
print('+=============================================+')

res = requests.post(url + api, data=json.dumps(body2), headers=headers)

soup3 = BeautifulSoup(res.text, "html.parser")
print(body2.get('account'))
print(soup3)
print('+=============================================+')
