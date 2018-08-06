import json

import requests
from bs4 import BeautifulSoup


def creat_subject():
    url = "localhost:8083/cip/subject"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB e6ebb126-b956-421e-bcde-351e88366de8'
    }

    body = {
        "subjectId": "friend01",
        "subjectName": "friend01",
        "gender": "MALE",
        "birthday": "2018-02-27T02:38:47.033Z",
        "ethnicity": "HAN",
        "personalHistory": [
            "HYPERTENSION"
        ],
        "familyHistory": [
            "HYPERTENSION"
        ],
        "smoke": "NONE",
        "drink": "NONE",
        "chewingAreca": "NONE",
        "unitId": "unit123"
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
        print(body.get('subjectId'))
        print(soup)
        print('+=============================================+')


creat_subject()
