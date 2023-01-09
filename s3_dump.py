import logging
import boto3
from botocore.exceptions import ClientError
import os

session = boto3.session(
      region_name = 'us-west-2', 
      aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), 
      aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))

myclient = session.resource('s3')

bucket_name = "spotify-tracks-leuneri"
file_name = "spotify_data.json"

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file(file_name, bucket_name)





















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