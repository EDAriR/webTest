import json

import requests
from bs4 import BeautifulSoup


def delete_ownership(authorization, ownershipIds):

    url = "http://localhost:8083/cip/ownership/request?ownershipIds="

    headers = {
        'Authorization': authorization
    }

    print('批次刪除請求授權 [DELETE /ownership/request]')

    res = requests.delete(url + ownershipIds,headers = headers)

    soup1 = BeautifulSoup(res.text, "html.parser")

    print(soup1)
    print('+===============================================================+')