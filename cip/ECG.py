import json

import requests
from bs4 import BeautifulSoup

from cip.ecg import AddECG, GetECGbyUserId, GetMyECG

url = "http://localhost:8083/cip/vitals"

authorization = ''
subjectId = ''
userId = ''
# 新增心電圖 [POST /vitals/subject/:subjectId/ecg]
AddECG.addECG(authorization, subjectId)
# 搜尋多筆心電圖 [GET /vitals/subject/:subjectId/ecg]
GetMyECG.getECG(authorization, subjectId)
# 搜尋多筆使用者之受測者心電圖 [GET /vitals/user/:userId/subject/:subjectId/ecg]
GetECGbyUserId.getECG(authorization, userId, subjectId)
# 搜尋多筆提供者之受測者心電圖 [GET /vitals/provider/:userId/subject/:subjectId/ecg]