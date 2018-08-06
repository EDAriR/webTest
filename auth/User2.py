import json

import requests
from bs4 import BeautifulSoup


def create_user2(userId, userName, password):
    url = "http://localhost:8080/aaa/user"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB a40c9707-7858-4814-ad7d-560d8e66f4ee'
    }

    body = {
        "userId": userId,
        "userName": userName,
        "password": password,
        "confirmPassword": password,
        "email": userId + "@1qaz2wsx.com",
        "cardIds": [],
        "unitIds": [],
        "roleIds": ["DEFAULT_USER", "testROLE"],
        "status": "ENABLED"
    }

    res = requests.post(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


create_user2("n124331915", "n124331915", "1qaz2wsx")

