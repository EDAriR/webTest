import json

import requests
from bs4 import BeautifulSoup


def create_user2(userId, userName, password):
    url = "http://172.17.9.58:8000/aaa/user"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB 4c60fe14-d219-431b-98c3-23aa31084d6e'
    }

    body = {
        "userId": userId,
        "userName": userName,
        "password": password,
        "confirmPassword": password,
        "email": userId + "@1qaz2wsx.com",
        "cardIds": [],
        "unitIds": [],
        "roleIds": ["DEFAULT_USER"],
        "status": "ENABLED"
    }

    res = requests.post(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


create_user2("n124331915", "1qaz2wsx", "1qaz2wsx")

