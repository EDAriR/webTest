import requests
from bs4 import BeautifulSoup

url = "http://localhost:8080/pointMonthlyReport?hospitalSequence=1&&monthlyDifference=-1"

headers = {
    'Authorization': 'web 69458ac2-9257-45b8-bca4-edc9d281298c'
}

body = {
  'loginId': 'sincerered',
  'password': '1060821',
  'device': 'WEB',
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print(res.status_code)
print(soup)