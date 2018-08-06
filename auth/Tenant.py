import json

import requests
from bs4 import BeautifulSoup


def creat_tenant():
    url = "http://localhost:8080/aaa/tenant"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB 6420fb71-3d2a-45e6-a4cd-f953b6b118f3'
    }

    body = {
        "tenantId": "TTSHB",
        "tenantName": "TTSHB",
        "permissionIds": [
            "DELETE /vitals/device","GET /vitals/user/:userId/subject/:subjectId/waist","POST /aaa/group","GET /vitals/subject/:subjectId/bloodPressure","GET /vitals/subject/:subjectId/bodyInfo","DELETE /aaa/unit","GET /vitals/subject/:subjectId","GET /aaa/unit/:unitId","POST /aaa/unitMeta","DELETE /aaa/unitMeta","GET /aaa/group/:groupId","GET /vitals/user/:userId/subject","GET /aaa/tenant/:tenantId","GET /aaa/subTenant","POST /aaa/role","GET /ownership/getpushlist","GET /ownership/simpleUser","GET /abnormality/bloodPressure/case","POST /aaa/subTenant","POST /import/initialization","GET /aaa/config","POST /aaa/unit","GET /vitals/user/:userId/subject/:subjectId","GET /ownership/request","DELETE /aaa/user","GET /vitals/user/:userId/subject/:subjectId/biochemistry","POST /vitals/subject/:subjectId/bloodGlucose","GET /vitals/subject/:subjectId/bodyTemperature","GET /aaa/role/:roleId","GET /vitals/subject/:subjectId/bloodGlucose","DELETE /aaa/subTenant","POST /aaa/tenant","POST /questionnair/:questionnairId/reply","PUT /ownership/consent/:ownershipId","PUT /aaa/user/:userId","PUT /aaa/unit/:unitId","GET /aaa/tenant","GET /questionnair/:questionnairId","GET /vitals/device/:deviceId","GET /vitals/subject/:subjectId/waist","GET /aaa/user/:userId","GET /vitals/user/:userId/subject/:subjectId/bodyInfo","GET /questionnair/:questionnairId/question","PUT /aaa/role/:roleId","GET /vitals/user/:userId/subject/:subjectId/bodyTemperature","GET /vitals/provider/:userId/subject/:subjectId/waist","GET /questionnair/:questionnairId/question/:questionId","PUT /aaa/tenant/:tenantId","GET /vitals/device","PUT /aaa/group/:groupId","POST /vitals/subject/:subjectId/waist","GET /aaa/user","POST /aaa/user","DELETE /ownership/consent","GET /vitals/user/:userId/subject/:subjectId/bloodPressure","GET /vitals/user/:userId/subject/:subjectId/bloodGlucose","GET /vitals/provider/:userId/subject/:subjectId/biochemistry","POST /vitals/subject/:subjectId/bodyTemperature","GET /aaa/permission","POST /vitals/subject/:subjectId/bloodPressure","GET /vitals/report/opinion","POST /abnormality/bloodPressure/case/:caseId/log","PUT /aaa/subTenant/:tenantId","GET /vitals/report/record","POST /vitals/subject/:subjectId/biochemistry","GET /aaa/guest","PUT /vitals/device/:deviceId","GET /aaa/role","GET /vitals/subject/:subjectId/biochemistry","GET /abnormality/bloodPressure/case/:caseId/log","DELETE /aaa/group","PUT /aaa/config/:configId","GET /vitals/provider/:userId/subject/:subjectId/bodyInfo","GET /vitals/provider/:userId/subject/:subjectId/bodyTemperature","POST /ownership/request","GET /aaa/unitMeta/:unitId","PUT /aaa/guest","GET /aaa/unit","DELETE /aaa","GET /questionnair","GET /abnormality/bloodPressure/case/:caseId","GET /ownership/consent","DELETE /vitals/subject","PUT /aaa/password","PUT /aaa/unitMeta/:unitId","GET /aaa/group","GET /ownership/myfollow","GET /vitals/report/amount","GET /abnormality/subject","PUT /aaa/user/:userId/password","GET /vitals/report/amountByAge","GET /vitals/provider/:userId/subject/:subjectId/bloodGlucose","DELETE /ownership/request","GET /vitals/provider/:userId/subject/:subjectId/bloodPressure","PUT /vitals/subject/:subjectId","GET /abnormality/report/amount","DELETE /aaa/tenant","GET /aaa/subTenant/:tenantId","DELETE /aaa/role","GET /aaa/unitMeta","POST /vitals/device","GET /vitals/measuredSubject","POST /vitals/subject/:subjectId/bodyInfo","GET /abnormality/bloodPressure/case/:caseId/log/:logId","POST /vitals/subject"
        ],
        "userId": "TTSHB",
        "password": "1qaz2wsx",
        "confirmPassword": "1qaz2wsx"
    }

    res = requests.post(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


creat_tenant()
