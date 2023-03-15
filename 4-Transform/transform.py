import json
from pyspark.sql import SparkSession
import os
pwd = str(os.getcwd())
pwd = pwd[:-11] + "3-Extract"
spark = SparkSession.builder.appName("JSON Processing").getOrCreate()
df = spark.read.json(pwd + "\extracted_data.json")
df.show()

