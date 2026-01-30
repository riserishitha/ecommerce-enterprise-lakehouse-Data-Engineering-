from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("SilverTransform").getOrCreate()
orders = spark.read.parquet("lakehouse/bronze/orders")
cleaned = orders.dropDuplicates().filter(col("payment_value").isNotNull())
cleaned.write.mode("overwrite").parquet("lakehouse/silver/orders_cleaned")
print("Silver layer ready")
