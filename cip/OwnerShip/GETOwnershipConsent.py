import json

import requests
from bs4 import BeautifulSoup


def get_ownership(authorization, search):

    url = "http://localhost:8083/cip/ownership/consent?"

    headers = {
        'Authorization': authorization
    }

    print('搜尋多筆同意授權 [GET /ownership/consent]')

    res = requests.get(url + search,headers = headers)

    soup1 = BeautifulSoup(res.text, "html.parser")

    print(soup1)
    print('+===============================================================+')