import json

import requests
from bs4 import BeautifulSoup

# 搜尋多筆提供者之受測者心電圖 [GET /vitals/provider/:userId/subject/:subjectId/ecg]
# 搜尋多筆使用者之受測者心電圖 [GET /vitals/user/:userId/subject/:subjectId/ecg]
def getECG(authorization, userId, subjectId):
    headers = {
        'Authorization': authorization
    }

    url = "http://localhost:8083/cip/vitals/"

    res = requests.post(url + 'user/' + userId + '/subject/' + subjectId + '/ecg')

    soup1 = BeautifulSoup(res.text, "lxml")

    print('[GET /vitals/user/:userId/subject/:subjectId/ecg]')
    print(soup1)
    return soup1