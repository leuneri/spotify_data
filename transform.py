import json
from pyspark.sql import SparkSession
import get



json_data = get.json_data
spark = SparkSession.builder.appName("JSON Processing").getOrCreate()
df = spark.createDataFrame(json_data)

df = df.select("items.track.artists.name", "items.track.name")

output_data = df.toJSON().collect()

print(output_data)
