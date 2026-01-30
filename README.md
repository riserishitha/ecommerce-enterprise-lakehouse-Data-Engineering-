# Enterprise E-Commerce Data Lakehouse

This is a full enterprise-grade Data Engineering project.

## Features
- Batch ingestion (CSV/JSON)
- Kafka streaming ingestion (new orders)
- PySpark ETL Bronze → Silver → Gold layers
- Gold analytics exposed to Postgres Warehouse
- Grafana dashboard ready
- Docker Compose deployment

## Run the Pipeline

```bash
docker-compose up -d
docker exec -it spark bash

spark-submit jobs/bronze_ingest.py
spark-submit jobs/silver_transform.py
spark-submit jobs/gold_aggregations.py
spark-submit jobs/load_to_postgres.py
```

## Streaming Orders

```bash
spark-submit jobs/stream_kafka_orders.py
```

Grafana runs at: http://localhost:3000
