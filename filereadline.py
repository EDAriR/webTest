import requests

file = open('/home/ed/Downloads/原民會刪除使用者/20180920fail_user.csv')

seq = []
for line in file.readlines():
    line = line.replace('\n', '')
    if line != '':
        seq.append(line)

print(seq)
a = 0
sql = 'DELETE FROM users where sequence = '
for i in seq:
    sql = sql + str(i) + ' or sequence = '

print(sql)
#     a = a + 1
#     url = "http://172.17.4.102:8984/solr/syntron/update?commit=true&stream.body=<delete><query>id:SolrBloodPressureHeartBeat" + str(i) + "</query></delete>"
#     res = requests.get(url)
#     print(res.text)
#
# print(a)
