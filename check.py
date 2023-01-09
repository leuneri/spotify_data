import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('spotify-data-leuneri')

if bucket.creation_date:
   print("The bucket exists")
else:
   print("The bucket does not exist")
