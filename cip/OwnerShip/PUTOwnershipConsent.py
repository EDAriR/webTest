import json

import requests
from bs4 import BeautifulSoup


def agree_ownership(authorization, ownershipId):

    url = "http://localhost:8083/cip/ownership/consent/"

    headers = {
        'Authorization': authorization
    }

    print('修改同意授權 [PUT /ownership/consent/:ownershipId]')

    res = requests.put(url + ownershipId, headers = headers)

    soup1 = BeautifulSoup(res.text, "html.parser")

    print(soup1)
    print('+===============================================================+')