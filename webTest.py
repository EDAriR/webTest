import json

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
    'content-type': 'application/json'
}
'''
{
    "authorization":"web 6fc53cac-4a3a-44f9-888f-0e10d77ccb21",
    "userRole":"USER",
    "userSequence":1
}
    'Content-Type': 'application/json'  
'''
url = "http://localhost:8080/aaa"

body = {
  'loginId': 'sincerered',
  'password': '1060821',
  'device': 'WEB',
}

res = requests.post(url, data = json.dumps(body), headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

# a = soup.findAll("div", {"class": "thumbnailWithOverlay"})

# for image in a:https://web.sun2u.com/Login
#     # image = urlopen(a['src'])
#     name = a['href'].split('/')[0]
print(res.status_code)
print(soup)
authorization = soup.string.split(':')[1].split(' ')[1].split('\"')
'''
# 編碼
res.encoding = "utf-8"
a = soup.findAll("a", {"class": "qa-item-subject-link"})
span = soup.select('span[class^=hl]')
author = soup.select('div[class^=author]')
date = soup.select('div[class^=date]')
title = soup.select('div[class^=title]')
for s in span:
    i=0
    j=i+1
    print(s)
    print("--------")
    print(title[j])
    print("--------")
    print(span[j])
    print("--------")'''

'''for image in images:
    img = urlopen(image['href'])
    name = image['href'].split('/')[3]
    with open('./images/' + str(name), 'wb') as f:
        f.write(img.read())'''
