# ability to access things in s3 environment
import boto3
import pandas
import access_keys

# low-level functional client
client = boto3.client(
    's3',
    aws_access_key_id = access_keys.access_key,
    aws_secret_access_key = access_keys.secret_access_key,
    region_name = 'us-west-2'   
)

# high-level functional client
resource = boto3.resource(
    's3',
    aws_access_key_id = access_keys.access_key,
    aws_secret_access_key = access_keys.secret_access_key,
    region_name = 'us-west-2' 
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()

# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')