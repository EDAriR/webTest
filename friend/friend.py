import json

import requests
from bs4 import BeautifulSoup


url = "http://localhost:9453/friend"

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
print('addfriend test 1 Unauthorized urlpath : ' + url + testPath)


res = requests.post(url + testPath)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/1'
print('addfriend test 2 user doesnot exit urlpath : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend01'
print('addfriend test 3 user cannt add yourself urlpath : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/friend02'
print('addfriend test 4 add successful : ' + url + testPath)


res = requests.post(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/agree/1'
print("agree friend test 1 friend sequence doesn't exist : " + url + testPath)


res = requests.put(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)

print('+===============================================================+')

testPath = '/agree/2'
print('agree friend test 2 you are not friend: ' + url + testPath)


res = requests.put(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/1'
print("delete friend test 1 friend sequence 1  doesn't exist: " + url + testPath)


res = requests.delete(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')

testPath = '/2'
print("delete friend test 2 you are not friend: " + url + testPath)


res = requests.delete(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup1)
print('+===============================================================+')


testPath = '?sequence=1'
print("refuse Be friend test 1 friend sequence 1  doesn't exist: " + url + testPath)


res = requests.delete(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')

testPath = '?sequence=2'
print("refuse Be friend test 2 you are not friend: " + url + testPath)


res = requests.delete(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')


print("get friend test 1 you are not friend: " + url)


res = requests.get(url , headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')

testPath = '/2'
print("get friend test 3 找不到: " + url + testPath)


res = requests.get(url + testPath, headers=firend01headers)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')