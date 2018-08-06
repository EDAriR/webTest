import json

import requests
import time

targets = ['6188', '5478', '6488'] #關注的股票代碼

endpoint = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp'

timestamp = int(time.time() * 1000 + 1000)

channels = '|'.join('otc_{}.tw'.format(target_otc) for target_otc in targets)
query_url = '{}?&ex_ch={}&json=1&delay=0&_={}'.format(endpoint, channels,
timestamp)

headers = {'Accept-Language': 'zh-TW'}

req = requests.session()
req.get('http://mis.twse.com.tw/stock/index.jsp', headers=headers)

response = req.get(query_url)
content = json.loads(response.text) # 註解1
data = content['msgArray']   # 需要的訊息被包在'msgArray'裡面

print(data)