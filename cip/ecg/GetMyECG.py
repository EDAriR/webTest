import json

import requests
from bs4 import BeautifulSoup


# 搜尋多筆心電圖 [GET /vitals/subject/:subjectId/ecg]
def getECG(authorization, subjectId):
    headers = {
        'Authorization': authorization
    }

    url = "http://localhost:8083/cip/vitals/"

    res = requests.post(url + 'subject/'+ subjectId + '/ecg')

    soup1 = BeautifulSoup(res.text, "lxml")

    print(soup1)
    return soup1