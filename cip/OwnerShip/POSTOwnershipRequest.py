import json

import requests
from bs4 import BeautifulSoup


def add_ownership(authorization, userId):

    url = "http://localhost:8083/cip/ownership/request"

    headers = {
        'Authorization': authorization
    }

    body = {
        "userId": userId,
        "type": "VITALS"
    }

    print('新增請求授權 [POST /ownership/request]')

    res = requests.post(url, data=body, headers = headers)

    soup1 = BeautifulSoup(res.text, "html.parser")

    if res.status_code == 200:
        print(soup1)
    else:
        print(res.status_code)
        print(res.text)

    print('+===============================================================+')


