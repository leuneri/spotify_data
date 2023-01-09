import boto3
import pandas as pd
import pathlib

s3 = boto3.resource('s3')
bucket = s3.Bucket('spotify-data-leuneri')
obj = s3.Bucket('spotify-data-leuneri').Object('spotify_data.json').get()
data = pd.read_json(obj['Body']) 

