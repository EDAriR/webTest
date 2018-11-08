import threading
import time
import json
import requests

url = 'http://localhost:8083/syncare/healthIdCard'
headers = {
    'Content-Type': 'application/json'
}


def thread_job():
    body = {
        "userId": "EA23456898",
        "password": "1qaz2wsx",
        "confirmPassword": "1qaz2wsx",
        "email": "222@ggg.com",
        "cardIds": ["223456789106"],
        "userName": "zc23456898"
    }

    aaa_body = {
        "account": "EA23456898",
        "password": "1qaz2wsx",
        "userAgent": "WEB"
    }

    aaa = 'http://localhost:8080/aaa'
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.status_code)
    res = requests.post(aaa, data=json.dumps(aaa_body), headers=headers)
    print(r.status_code)
    print(res.text)


def t2_job():
    body = {
        "userId": "EB23456898",
        "password": "1qaz2wsx",
        "confirmPassword": "1qaz2wsx",
        "email": "222@ggg.com",
        "cardIds": ["223456789107"],
        "userName": "zc23456898"
    }

    aaa_body = {
        "account": "EB23456898",
        "password": "1qaz2wsx",
        "userAgent": "WEB"
    }

    aaa = 'http://localhost:8080/aaa'
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.status_code)
    res = requests.post(aaa, data=json.dumps(aaa_body), headers=headers)
    print(res.text)


def t3_job():
    body = {
        "userId": "EC23456898",
        "password": "1qaz2wsx",
        "confirmPassword": "1qaz2wsx",
        "email": "222@ggg.com",
        "cardIds": ["223456789108"],
        "userName": "zc23456898"
    }

    aaa_body = {
        "account": "EC23456898",
        "password": "1qaz2wsx",
        "userAgent": "WEB"
    }

    aaa = 'http://localhost:8080/aaa'
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.status_code)
    res = requests.post(aaa, data=json.dumps(aaa_body), headers=headers)
    print(res.text)


def main():
    thread1 = threading.Thread(target=thread_job, name='T1')
    thread1.start()

    thread2 = threading.Thread(target=t2_job, name='T2')
    thread2.start()

    thread2 = threading.Thread(target=t3_job, name='T3')
    thread2.start()

    print('all done')


if __name__ == '__main__':
    main()
