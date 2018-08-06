import json

import requests
from bs4 import BeautifulSoup




def creat_user():

    url = "http://localhost:8080/aaa/user"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB e6ebb126-b956-421e-bcde-351e88366de8'
    }

    friend01body = {
        "userId": "friend01",
        "userName": "friend01",
        "password": "1qaz2wsx",
        "confirmPassword": "1qaz2wsx",
        "email": "friend01@1qaz2wsx.com",
        "mobilePhone": "0987654321",
        "cardIds": [],
        "unitIds": [],
        "roleIds": ["DEFAULT_USER", "testROLE"],
        "status": "ENABLED"
    }

    res = requests.post(url , data=json.dumps(friend01body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(friend01body.get('userId'))
    print(soup)
    print('+=============================================+')

    friend02body = {
        "userId": "friend02",
        "userName": "friend02",
        "password": "1qaz2wsx",
        "confirmPassword": "1qaz2wsx",
        "email": "friend02@1qaz2wsx.com",
        "mobilePhone": "0987654322",
        "cardIds": [],
        "unitIds": [],
        "roleIds": ["DEFAULT_USER", "testROLE"],
        "status": "ENABLED"
    }

    res2 = requests.post(url , data=json.dumps(friend02body), headers=headers)

    soup2 = BeautifulSoup(res2.text, "html.parser")

    print(headers)
    print(res2.text)

    print('+--------------------------------------------+')
    print(friend02body.get('userId'))
    print(soup2)
    print('+=============================================+')

creat_user()