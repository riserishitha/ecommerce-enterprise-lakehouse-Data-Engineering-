from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("KafkaOrdersStream").getOrCreate()

schema = StructType() \
    .add("order_id", StringType()) \
    .add("customer_id", StringType()) \
    .add("category", StringType()) \
    .add("payment_value", DoubleType())

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "new_orders") \
    .load()

parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

query = parsed.writeStream.format("parquet") \
    .option("checkpointLocation", "lakehouse/checkpoints/orders") \
    .option("path", "lakehouse/bronze/stream_orders") \
    .outputMode("append") \
    .start()

query.awaitTermination()
