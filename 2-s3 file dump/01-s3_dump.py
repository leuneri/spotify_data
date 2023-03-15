import boto3
s3 = boto3.resource("s3")
bucket = s3.Bucket("spotify-data-leuneri")
bucket.upload_file(Key="spotify_data.json", Filename="./spotify_data.json")
