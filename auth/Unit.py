import json

import requests
from bs4 import BeautifulSoup


def create_unit():
    url = "http://localhost:8080/aaa/unit"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB 9f2ae5c5-72f2-45e9-a37c-d2757cc32daf'
    }

    body = {
        "unitId": "1001401001101",
        "unitName": "馬蘭部落文化健康站",
        "parentUnitId": "1001401"
    }

    res = requests.post(url, data=json.dumps(body), headers=headers)

    if res.status_code == 404:
        print(res.status_code)
    elif res.status_code == 400:
        print(res.text)
    elif res == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        print(res.text)
        print('+--------------------------------------------+')
        print(body.get('unitId'))
        print(soup)
        print('+=============================================+')
    else:
        print(res.status_code)
        print(res.text)


create_unit()
