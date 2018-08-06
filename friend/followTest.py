import json

import requests
from bs4 import BeautifulSoup


url = "http://localhost:9453/follow"

friend01headers = {
    'content-type': 'application/json',
    'Authorization': 'WEB e28311b1-abc9-4178-b474-3188ab591b3b'
}

testPath = "?userId=friend01"

print('follow test addFollow : ' + url + testPath)

res = requests.post(url + testPath)

soup1 = BeautifulSoup(res.text, "html.parser")

print(soup1)
print('+===============================================================+')
