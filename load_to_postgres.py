from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LoadToPostgres").getOrCreate()

top_customers = spark.read.parquet("lakehouse/gold/top_customers")

top_customers.write.format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/ecommerce") \
    .option("dbtable", "top_customers") \
    .option("user", "admin") \
    .option("password", "admin") \
    .mode("overwrite") \
    .save()

print("Loaded Gold tables into Postgres")
