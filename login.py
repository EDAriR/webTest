import json

import requests
from bs4 import BeautifulSoup

url = "http://localhost:8080/"
# url = "http://172.17.9.60:8080/aaa"
# url = 'http://syncare.0.dailycare/'
api = "aaa"
headers = {
    'content-type': 'application/json'
}

body = {
    'loginId': 'robert07@gmail.com',
    'password': '1qaz2wsx',
    'device': 'WEB',
}
body2 = {
    'loginId': 'robert09@gmail.com',
    'password': '1qaz2wsx',
    'device': 'WEB',
}
#-Duser.timezone=UTC
# 'loginId': 'sincerered',
# 'password': '1060821',

# 'loginId': 'robert09@gmail.com',
#     'password': '1qaz2wsx',
#     'device': 'WEB',
# datasource:
# url: jdbc:postgresql: // 172.17.9.60/ dailycaredb

# http://syncare.0.dailycare/
# 'loginId': 'uuu',
#     'password': '1070101',
#     'device': 'WEB',

res = requests.post(url + api, data = json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

authorization = soup.string.split(':')[1].split(',')[0].split("\"")[1]
print(url)

print('+=============================================+')
print(soup)
print('+=============================================+')
print(authorization)

res = requests.post(url + api, data = json.dumps(body2), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print('------------------------------------------------------------------')
print('------------------------------------------------------------------')

authorization = soup.string.split(':')[1].split(',')[0].split("\"")[1]

print(soup)
print('+=============================================+')
print(authorization)


print('------------------------------------------------------------------')
print('------------------------------------------------------------------')
delete_header = {
    "authorization":authorization
}
res = requests.delete(url + api, data = json.dumps(body2), headers=delete_header)
print("delete ok")