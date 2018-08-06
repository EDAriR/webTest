import json

import requests
from bs4 import BeautifulSoup


def creat_tenant():
    url = "http://localhost:8080/aaa/tenant/DEFAULT_TENANT"

    headers = {
        'content-type': 'application/json',
        'Authorization': 'WEB f5f77136-c8ac-4545-af16-b4f28bbc69c9'
    }

    body = {

        "permissionIds": [
            "POST /follow",
            "DELETE /vitals/device",
            "GET /vitals/user/:userId/subject/:subjectId/waist",
            "POST /aaa/group",
            "GET /friend/:userId",
            "GET /vitals/subject/:subjectId/bloodPressure",
            "DELETE /friend",
            "DELETE /follow/:sequence",
            "GET /vitals/subject/:subjectId/bodyInfo",
            "DELETE /aaa/unit",
            "GET /follow/followme",
            "GET /vitals/subject/:subjectId",
            "GET /aaa/unit/:unitId",
            "POST /aaa/unitMeta",
            "DELETE /aaa/unitMeta",
            "GET /vitals/provider/:userId/subject/:subjectId/ecg",
            "GET /aaa/group/:groupId",
            "GET /vitals/user/:userId/subject",
            "GET /aaa/tenant/:tenantId",
            "GET /aaa/subTenant",
            "POST /aaa/role",
            "GET /ownership/getpushlist",
            "GET /abnormality/bloodPressure/case",
            "POST /aaa/subTenant",
            "POST /import/initialization",
            "GET /aaa/config",
            "GET /friend",
            "POST /aaa/unit",
            "GET /vitals/user/:userId/subject/:subjectId",
            "GET /ownership/request",
            "DELETE /aaa/user",
            "GET /vitals/user/:userId/subject/:subjectId/biochemistry",
            "POST /vitals/subject/:subjectId/bloodGlucose",
            "PUT /friend/agree/:sequence",
            "GET /blocklist/:userId",
            "GET /vitals/subject/:subjectId/bodyTemperature",
            "GET /aaa/role/:roleId",
            "GET /vitals/subject/:subjectId/bloodGlucose",
            "DELETE /aaa/subTenant",
            "POST /aaa/tenant",
            "PUT /ownership/consent/:ownershipId",
            "PUT /aaa/user/:userId",
            "PUT /aaa/unit/:unitId",
            "GET /aaa/tenant",
            "GET /vitals/device/:deviceId",
            "GET /vitals/subject/:subjectId/waist",
            "GET /aaa/user/:userId",
            "GET /follow/:userId",
            "GET /vitals/user/:userId/subject/:subjectId/bodyInfo",
            "PUT /aaa/role/:roleId",
            "GET /vitals/user/:userId/subject/:subjectId/bodyTemperature",
            "GET /vitals/provider/:userId/subject/:subjectId/waist",
            "PUT /aaa/tenant/:tenantId",
            "GET /vitals/device",
            "DELETE /friend/:sequence",
            "PUT /aaa/group/:groupId",
            "POST /vitals/subject/:subjectId/waist",
            "GET /aaa/user",
            "POST /friend/:userId",
            "POST /aaa/user",
            "DELETE /ownership/consent",
            "GET /vitals/user/:userId/subject/:subjectId/bloodPressure",
            "GET /vitals/user/:userId/subject/:subjectId/bloodGlucose",
            "GET /vitals/provider/:userId/subject/:subjectId/biochemistry",
            "POST /vitals/subject/:subjectId/bodyTemperature",
            "GET /aaa/permission",
            "DELETE /follow/userId/:userId",
            "POST /vitals/subject/:subjectId/bloodPressure",
            "POST /abnormality/bloodPressure/case/:caseId/log",
            "PUT /aaa/subTenant/:tenantId",
            "GET /vitals/report/record",
            "POST /vitals/subject/:subjectId/biochemistry",
            "GET /aaa/guest",
            "PUT /vitals/device/:deviceId",
            "GET /aaa/role",
            "GET /vitals/subject/:subjectId/biochemistry",
            "GET /abnormality/bloodPressure/case/:caseId/log",
            "DELETE /aaa/group",
            "PUT /aaa/config/:configId",
            "GET /vitals/provider/:userId/subject/:subjectId/bodyInfo",
            "GET /vitals/provider/:userId/subject/:subjectId/bodyTemperature",
            "POST /ownership/request",
            "GET /aaa/unitMeta/:unitId",
            "POST /follow/:userId",
            "PUT /aaa/guest",
            "GET /aaa/unit",
            "DELETE /aaa",
            "GET /blocklist",
            "GET /abnormality/bloodPressure/case/:caseId",
            "GET /ownership/consent",
            "GET /follow",
            "DELETE /vitals/subject",
            "PUT /aaa/password",
            "PUT /aaa/unitMeta/:unitId",
            "GET /aaa/group",
            "GET /ownership/myfollow",
            "GET /vitals/report/amount",
            "GET /abnormality/subject",
            "GET /vitals/user/:userId/subject/:subjectId/ecg",
            "GET /vitals/report/amountByAge",
            "GET /vitals/provider/:userId/subject/:subjectId/bloodGlucose",
            "DELETE /ownership/request",
            "POST /vitals/subject/:subjectId/ecg",
            "GET /vitals/provider/:userId/subject/:subjectId/bloodPressure",
            "PUT /vitals/subject/:subjectId",
            "DELETE /aaa/tenant",
            "GET /aaa/subTenant/:tenantId",
            "DELETE /blocklist/:sequence",
            "DELETE /aaa/role",
            "GET /aaa/unitMeta",
            "POST /vitals/device",
            "POST /vitals/subject/:subjectId/bodyInfo",
            "GET /abnormality/bloodPressure/case/:caseId/log/:logId",
            "GET /vitals/subject/:subjectId/ecg",
            "POST /vitals/subject",
            "POST /blocklist/:userId",
            "POST /hrv/subject/:subjectId/hrv",
            "GET /hrv/subject/:subjectId/hrv",
            "GET /hrv/user/:userId/subject/:subjectId/hrv",
            "GET /hrv/provider/:userId/subject/:subjectId/hrv"
        ]
    }

    res = requests.put(url, data=json.dumps(body), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    print(res.text)

    print('+--------------------------------------------+')
    print(body.get('userId'))
    print(soup)
    print('+=============================================+')


creat_tenant()
