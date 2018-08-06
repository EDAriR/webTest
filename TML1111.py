import requests
from bs4 import BeautifulSoup
import json

import pandas

res = requests.get('https://pages.tmall.com/wow/act/18132/industry-100720')
soup = BeautifulSoup(res.text, 'html.parser')
j_array = []
for jdata in soup.select('.J_dynamic_data') :

    if jdata.text.strip() != '':

        jd = json.loads(jdata.text.strip())
        if isinstance(jd, dict) and jd.get('items'):
            df = pandas.DataFrame(jd['items'])
        if isinstance(jd, list):
            df = pandas.DataFrame(jd)

        j_array.append(jd)
