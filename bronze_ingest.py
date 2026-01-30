from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BronzeIngest").getOrCreate()
orders = spark.read.option("header", True).csv("data/raw/orders.csv")
orders.write.mode("overwrite").parquet("lakehouse/bronze/orders")
print("Bronze batch ingestion complete")
