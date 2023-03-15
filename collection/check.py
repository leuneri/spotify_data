import boto3

# Checks for if the bucket exists in my AWS account
s3 = boto3.resource('s3')
bucket = s3.Bucket('spotify-data-leuneri')

if bucket.creation_date:
   print("The bucket exists")
else:
   print("The bucket does not exist")
