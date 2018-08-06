str = '''
INSERT INTO "point_used_backup" ("sequence", "create_date", "class", "description", "point", "user_sequence", "user_id", "user_name", "interpretation_hospital_sequence", "interpretation_hospital_name", "interpretation_doctor_id", "interpretation_doctor_name", "transfer_hospital_name", "transfer_doctor_name", "report_create_time", "hospital_sequence") VALUES
(43,	'2017-12-04 03:29:44.805',	'DOWNLOAD',	'MEASUREMENT_REPORT',	2,	1,	'sincerered',	'sincerered',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	1),
(44,	'2017-12-04 03:31:11.035',	'DOWNLOAD',	'MEASUREMENT_REPORT',	2,	1,	'sincerered',	'sincerered',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	1),
(45,	'2017-12-08 04:19:04.214',	'UPLOAD',	'ECG',	12,	1,	'sincerered',	'sincerered',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	1),
(46,	'2017-12-08 04:19:04.326',	'INTERPRETATION',	'DOCTOR',	11,	1,	'sincerered',	'sincerered',	1,	'達楷',	'doctor',	'dd1',	NULL,	NULL,	NULL,	1),
(47,	'2017-12-08 04:19:04.331',	'UPLOAD',	'ECG',	12,	1,	'sincerered',	'sincerered',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	1),
(65,	'2017-12-08 04:19:04.494',	'INTEGRATIONREPORT',	'批次報告',	5,	1,	'sincerered',	'sincerered',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	1),
(66,	'2017-12-08 04:20:20.982',	'UPLOAD',	'ECG',	12,	1,	'sincerered',	'sincerered',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	1),
(67,	'2017-12-08 04:20:20.986',	'INTERPRETATION',	'DOCTOR',	11,	1,	'sincerered',	'sincerered',	1,	'達楷',	'doctor',	'dd1',	NULL,	NULL,	NULL,	1);
'''

seqCreater = '''nextval('replace_sequence_seq')'''
table = str.split("\"")
print(table[1])

print(seqCreater.replace("replace",table[1]))
print(str.replace('"',''))

print('===================================================')

str2 = '交易日期,交易時間,交易序號,交易類型,交易類型描述,扣點點數,用戶ID,用戶姓名,判讀醫院,判讀醫生,轉介醫院,轉介醫師,發票號碼'

for s in str2.split(',',-1):
    print(s)
print()