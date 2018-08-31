import requests

a = 0
for i in range(47467, 47586):
    a = a + 1
    print(i)
    url = "http://172.17.4.102:8984/solr/syntron/update?commit=true&stream.body=<delete><query>id:SolrBloodPressureHeartBeat" + str(i) + "</query></delete>"
    res = requests.get(url)
    print(url)
    print(res.text)

print(a)


