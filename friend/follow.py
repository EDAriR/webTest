import json

import requests
from bs4 import BeautifulSoup


url = "http://localhost:9453/follow"

systemAdminheaders = {
    'Authorization': 'WEB b78f214a-0e9c-49b3-b892-ddf99000468a'
}
firend01headers = {
    'Authorization': 'WEB dd284456-39e0-4df4-ae51-55240e51773f'
}
firend02headers = {
    'Authorization': 'WEB dd284456-39e0-4df4-ae51-55240e51773f'
}

testPath = '/1'
print('follow test 1 Unauthorized urlpath : ' + url + testPath)


res = requests.post(url + testPath)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')


testPath = '/1'
print('follow test 2 user doesnot exit urlpath : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend01'
print('follow test 3 cannt follow yourself : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')


testPath = '/friend02'
print('follow test 4  follow successful : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/1'
print('get follow test 1 user not exist : ' + url + testPath)

res = requests.get(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend01'
print('get follow test 2 cannt follow yourself : ' + url + testPath)

res = requests.get(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend02'
print('get follow test 3 successful : ' + url + testPath)

res = requests.get(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

print('get follow list test 1 successful : ' + url)

res = requests.get(url, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')


testPath = '/1'
print("delete follow test 1 doesn't exist : " + url+ testPath)

res = requests.delete(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')
