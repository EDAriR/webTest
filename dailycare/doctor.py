import login

import json
import requests
from bs4 import BeautifulSoup

authorization = login.authorization
api = "doctor"

headers = {
    'content-type': 'multipart/form-data; boundary=boundary',
    'authorization': authorization
}

body = {
    "hospitalSequence": 1,
    "role": "CASEMANAGER",
    "emailId": "robert06@gmail.com ",
    "password": "1qaz2wsx",
    "name": "doctor1",
    "mobilePhone": "0912345678",
    "signature": "xxxx.jpg",
    "transferService": "true",
    "interpretationService": "true",
    "status": "ENABLED"
}

boundary = 'kerker';
doctorBody = '';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="hospitalSequence"\r\n\r\n';
doctorBody += '2' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="role"\r\n\r\n';
doctorBody += 'DOCTOR' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="emailId"\r\n\r\n';
doctorBody += 'sin@mail.com' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="password"\r\n\r\n';
doctorBody += 'aaaaaaaa' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="name"\r\n\r\n';
doctorBody += 'kerker' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="mobilePhone"\r\n\r\n';
doctorBody += '1111111111' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="signature"; filename="foo.jpg"\r\n';
doctorBody += 'Content-Type: text/plain\r\n\r\n';
doctorBody += 'sin@mail.com' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="transferService"\r\n\r\n';
doctorBody += 'true' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="interpretationService"\r\n\r\n';
doctorBody += 'true' + '\r\n';
doctorBody += '--' + boundary + '\r\n';
doctorBody += 'Content-Disposition: form-data; name="status"\r\n\r\n';
doctorBody += 'ENABLED' + '\r\n';

print(doctorBody)
res = requests.post(login.url + api, data=doctorBody, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")
print(res.status_code)

if (res.status_code == 200):
    print("create CASEMANAGER Ok")

print(soup)