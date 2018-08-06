import pandas
import requests
from bs4 import BeautifulSoup

url = "https://www.caac.ccu.edu.tw/apply107/system/107ColQry_forapply_4hgd9/ShowSchool.php"

payload = {'option': 'SCHNAME', 'SubSchName': '%E4%BE%9D%E5%AD%B8%E6%A0%A1%E5%90%8D%E7%A8%B1%E6%9F%A5%E8%A9%A2'}


res = requests.post(url,data=payload)

soup = BeautifulSoup(res.text, "html.parser")


# 抓取網址
# url = "http://localhost:63342/imget/school.html?_ijt=14n42u2q8339kj1tbk9jhklpip"
# # Table所在網頁前面
url2 = "https://www.caac.ccu.edu.tw/apply107/system/107ColQry_forapply_4hgd9/"
# res = requests.get(url)
# 編碼
# res.encoding = "utf-8"
# soup = BeautifulSoup(res.text, 'html.parser')
# # 取得連結
a = soup.find_all('a')
#
for link in a:
    href = link.get("href")
    name = str(link).split(">")[1]
    n = name.split("<")[0]

    h = url2 + href
    dfs = pandas.read_html(h)
    cur = dfs[0]

    writer = pandas.ExcelWriter(n + '.xlsx')
    cur.to_excel(writer, 'Sheet5')
    writer.save()