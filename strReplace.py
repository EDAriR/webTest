str = '''

'''

seqCreater = '''nextval('replace_sequence_seq')'''
table = str.split("\n")

s = []
for t in table:
    if t !='':
        s.append(t)
print('===================================================')
print(s)

str2 = '交易日期,交易時間,交易序號,交易類型,交易類型描述,扣點點數,用戶ID,用戶姓名,判讀醫院,判讀醫生,轉介醫院,轉介醫師,發票號碼'

