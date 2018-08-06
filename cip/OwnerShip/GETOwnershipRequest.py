import json

import requests
from bs4 import BeautifulSoup


def get_ownership(authorization, search):

    url = "http://localhost:8083/cip/ownership/request?"

    headers = {
        'Authorization': authorization
    }

    print('搜尋多筆請求授權 [GET /ownership/request]')

    res = requests.get(url + search,headers = headers)

    soup1 = BeautifulSoup(res.text, "html.parser")

    if res.status_code == 200:
        print(soup1)
    else:
        print(res.status_code)
        print(res.text)

    print('+===============================================================+')