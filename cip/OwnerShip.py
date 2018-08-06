import json

import requests
from bs4 import BeautifulSoup

from cip.OwnerShip import POSTOwnershipRequest, GETOwnershipRequest, DELETEOwnershipRequest, PUTOwnershipConsent, \
    GETOwnershipConsent, DELETEOwnershipConsent
from cip.OwnerShip.GETOwnershipRequest import get_ownership
from cip.OwnerShip.POSTOwnershipRequest import add_ownership

url = "http://localhost:8083/cip/ownership"

systemAdminheaders = {
    'Authorization': 'WEB b78f214a-0e9c-49b3-b892-ddf99000468a'
}
firend01headers = {
    'Authorization': 'WEB dd284456-39e0-4df4-ae51-55240e51773f'
}
firend02headers = {
    'Authorization': 'WEB dd284456-39e0-4df4-ae51-55240e51773f'
}

'''
新增請求授權 [POST /ownership/request]
POSTOwnershipRequest
搜尋多筆請求授權 [GET /ownership/request]
GETOwnershipRequest
批次刪除請求授權 [DELETE /ownership/request]
DELETEOwnershipRequest
'''

'''
systemAdmin
"WEB 9c6e36e0-4731-403e-b96e-0ee02395b795"
+=============================================+
friend01
"WEB f2498903-4658-4335-898a-a5cd22b644ba"
+=============================================+
friend02
"WEB f2498903-4658-4335-898a-a5cd22b644ba"
+=============================================+

'''

add_ownership('WEB 9c6e36e0-4731-403e-b96e-0ee02395b795', 'friend01')
# get_ownership('WEB 9c6e36e0-4731-403e-b96e-0ee02395b795', '')
# DELETEOwnershipRequest.delete_ownership('', '')


'''
修改同意授權 [PUT /ownership/consent/:ownershipId]
PUTOwnershipConsent
搜尋多筆同意授權 [GET /ownership/consent]
GETOwnershipConsent
批次刪除同意授權 [DELETE /ownership/consent]
DELETEOwnershipConsent

'''

# PUTOwnershipConsent.add_ownership('', '')
# GETOwnershipConsent.get_ownership('', '')
# DELETEOwnershipConsent.delete_ownership('', '')
