import json

import requests
from bs4 import BeautifulSoup


# 真正使用者註冊用
# 要收信 OPT認證後 才可以使用 要真的email

def creat_guest():
    url = "http://localhost:8080/aaa/guest"

    headers = {
        'content-type': 'application/json',
    }

    body = {
        "userId": "a159672679",
        "userName": "使用者1",
        "password": "1qaz2wsx",
        "email":"luciferomax002@gmail.com",
        "confirmPassword": "1qaz2wsx",
        "cardIds": [
            1234567890
        ]

    }

    res = requests.post(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


creat_guest()

