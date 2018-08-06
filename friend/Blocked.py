import json

import requests
from bs4 import BeautifulSoup


url = "http://localhost:9453/blocklist"

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
print('blocklist test 1 Unauthorized urlpath : ' + url + testPath)


res = requests.post(url + testPath)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')


testPath = '/1'
print('blocklist test 2 user doesnot exit urlpath : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend01'
print('blocklist test 3 cannt add yourself : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend02'
print('blocklist test 4 user doesnot exit urlpath : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')