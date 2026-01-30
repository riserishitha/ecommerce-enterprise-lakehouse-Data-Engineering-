from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
spark = SparkSession.builder.appName("GoldAggregations").getOrCreate()
orders = spark.read.parquet("lakehouse/silver/orders_cleaned")
revenue = orders.groupBy("category").agg(sum("payment_value").alias("total_revenue"))
top_customers = orders.groupBy("customer_id").agg(sum("payment_value").alias("total_spent")) \
    .orderBy("total_spent", ascending=False).limit(10)
revenue.write.mode("overwrite").parquet("lakehouse/gold/revenue_by_category")
top_customers.write.mode("overwrite").parquet("lakehouse/gold/top_customers")
print("Gold analytics generated")
