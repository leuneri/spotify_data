

import boto3
s3 = boto3.resource("s3")
bucket = s3.Bucket("spotify-data-leuneri")
bucket.upload_file(Key="spotify_data.json", Filename="./spotify_data.json")



















# import json
# import boto3
# import access_keys
# import os
# import pathlib


# session = boto3.Session( 
#          aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), 
#          aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
# s3_client = boto3.client("s3")
# bucket_name = "spotify-tracks-leuneri"
# object_name = "spotify_data.json"
# file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "spotify_data.json")

# response = s3_client.upload_file(file_name, bucket_name, object_name)