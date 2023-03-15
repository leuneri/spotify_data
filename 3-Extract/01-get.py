import boto3
import pandas as pd
import pathlib
import json
s3 = boto3.resource('s3')
bucket = s3.Bucket('spotify-data-leuneri')
obj = s3.Bucket('spotify-data-leuneri').Object('spotify_data.json').get()
response = obj['Body']

json_data = json.loads(response.read().decode('utf-8'))
print(json_data)
# print(type(obj))
# print(obj)
with open("extracted_data.json", "w") as outfile:
    json.dump(json_data, outfile)