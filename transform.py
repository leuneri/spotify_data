import json
from pyspark.sql import SparkSession
import get

spark = SparkSession.builder.appName("JSON Processing").getOrCreate()
df = spark.read.json("./extracted_data.json")
df.show()

