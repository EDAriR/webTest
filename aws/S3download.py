import boto3


AWS_ACCESS_KEY_ID = 'AKIAJCEFVSCYK4MC4MYA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_BUCKET_NAME = 'ploan'

session = boto3.Session(
   aws_access_key_id=AWS_ACCESS_KEY_ID,
   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

KEY = 'ccds.war'
FILE_NAME = 'ccds.war'
s3 = session.resource('s3')
s3.Bucket(AWS_BUCKET_NAME).download_file(KEY, FILE_NAME)