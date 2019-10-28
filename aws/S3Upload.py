import os
import boto3

# AWS_ACCESS_KEY_ID = os.environ['aws_access_key']
# AWS_SECRET_ACCESS_KEY = os.environ['aws_secret_access_key']
# AWS_BUCKET_NAME = os.environ['bucket_name']


AWS_ACCESS_KEY_ID = 'AKIAJCEFVSCYK4MC4MYA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_BUCKET_NAME = 'ploan'
session = boto3.Session(
   aws_access_key_id=AWS_ACCESS_KEY_ID,
   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

def upload_file_to_s3(complete_file_path):

   if complete_file_path is None:
       raise ValueError("Please enter a valid and complete file path")

   session = boto3.Session(
       aws_access_key_id=AWS_ACCESS_KEY_ID,
       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
   )
   s3 = session.resource('s3')
   data = open(os.path.normpath(complete_file_path), 'rb')
   file_basename = os.path.basename(complete_file_path)
   s3.Bucket(AWS_BUCKET_NAME).put_object(Key=file_basename, Body=data)
   print('Upload File success')



