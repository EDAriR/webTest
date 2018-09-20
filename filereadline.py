import requests

file = open('/home/ed/Downloads/dbsync/20180920body_info_min_seq.csv')

seq = []
for line in file.readlines():
    line = line.replace('\n', '')
    if line != '':
        seq.append(line)

print(seq)
a = 0
for i in seq:
    print('select * from body_info where sequence = ' + str(i) + ';')
#     a = a + 1
#     url = "http://172.17.4.102:8984/solr/syntron/update?commit=true&stream.body=<delete><query>id:SolrBloodPressureHeartBeat" + str(i) + "</query></delete>"
#     res = requests.get(url)
#     print(res.text)
#
# print(a)
