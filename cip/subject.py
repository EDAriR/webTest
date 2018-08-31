import json

import requests
from bs4 import BeautifulSoup


# 新增受測者 [POST /vitals/subject]
def create_subject(subjectId, subjectName, gender, birthday, unitId, permission):
    url = "http://localhost:8080/vitals/subject"

    headers = {
        'content-type': 'application/json',
        'Authorization': permission
    }

    body = {
        "subjectId": subjectId,
        "subjectName": subjectName,
        "gender": gender,
        "birthday": birthday,
        "homePhone":"0212398722",
        "address":"台北市中山區松江路101號9樓",
        "ethnicity": "HAN",
        "personalHistory": [

        ],
        "familyHistory": [

        ],
        "smoke": "NONE",
        "drink": "NONE",
        "chewingAreca": "NONE",
        "unitId": unitId
    }

    res = requests.post(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


# subjectId = "systemAdmin"
# subjectName = "systemAdmin"
# birthday = "1976-07-26"
# permission = 'WEB 7c59cb34-5ab6-4c98-906a-212d6bccbdff'
# unitId = "1001401000201"
#
# # subjectId, subjectName, gender, birthday, unitId
# create_subject(subjectId, subjectName, "FEMALE", birthday, unitId, permission)
#
#
# subjectId = "test_ownership01"
# subjectName = "test_ownership01"
# birthday = "1976-07-26"
# permission = 'WEB 7b45bf80-88fb-414f-8d02-184e88c8ccd8'
# unitId = "1001401000201"
#
# # subjectId, subjectName, gender, birthday, unitId
# create_subject(subjectId, subjectName, "FEMALE", birthday, unitId, permission)
#
#
# subjectId = "test_ownership02"
# subjectName = "test_ownership02"
# birthday = "1996-07-26"
# permission = 'WEB c8a34371-a60f-45db-a7f9-8b69c206939e'
# unitId = "1001401000201"
#
# # subjectId, subjectName, gender, birthday, unitId
# create_subject(subjectId, subjectName, "MALE", birthday, unitId, permission)
#
#
# subjectId = "test_ownership06"
# subjectName = "test_ownership06"
# birthday = "1966-07-26"
# permission = 'WEB 4d172a55-e241-412b-baa2-1739134ecfec'
# unitId = "1001401000201"
#
# # subjectId, subjectName, gender, birthday, unitId
# create_subject(subjectId, subjectName, "FEMALE", birthday, unitId, permission)


subjectId = "systemAdmin"
subjectName = "systemAdmin"
birthday = "2018-05-23"
permission = 'WEB 51d430df-9841-4846-a29f-7cfce62101a1'
unitId = "1001401004201"

# subjectId, subjectName, gender, birthday, unitId
create_subject(subjectId, subjectName, "MALE", birthday, unitId, permission)
