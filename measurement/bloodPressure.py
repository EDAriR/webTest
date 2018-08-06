import json

import requests
from bs4 import BeautifulSoup

# 新增血壓心跳 [POST /vitals/subject/:subjectId/bloodPressure]
def create_bloodPressure():
    url = "http://localhost:8084/measurement/subject/A112494960/bloodPressure"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB 6fa90d3f-1c6f-4c94-9da6-e84ce374dfb2'
    }

    body = {
        "latitude": 12.345678,
        "longitude": 12.345678,
        "systolic": 130,
        "diastolic": 89,
        "heartRate": 100,
        "createTime": "2018-03-06"
    }


    res = requests.post(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


create_bloodPressure()

