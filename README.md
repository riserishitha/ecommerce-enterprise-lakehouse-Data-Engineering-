# 🛒 Enterprise E-Commerce Data Lakehouse Pipeline

This project demonstrates an **enterprise-grade Data Engineering Lakehouse architecture** for an e-commerce platform, supporting both **batch and real-time streaming ingestion**.

It showcases modern tools like **PySpark, Kafka, Airflow, PostgreSQL, Grafana, and Docker**.

---

## 🚀 Key Features

- Batch ingestion of historical order data (CSV/JSON)
- Real-time streaming ingestion of new orders using Apache Kafka
- Lakehouse architecture with **Bronze → Silver → Gold** layered design
- Data transformation and analytics using **PySpark + Spark SQL**
- Workflow orchestration with **Apache Airflow DAGs**
- Curated Gold datasets loaded into **PostgreSQL Data Warehouse**
- Dashboard-ready outputs using **Grafana**
- Fully containerized deployment with **Docker Compose**

---

## ⚙️ Technologies Used

| Component         | Tool |
|------------------|------|
| Processing Engine | PySpark |
| Streaming         | Kafka + Spark Structured Streaming |
| Storage Format    | Parquet (Lakehouse Layers) |
| Orchestration     | Apache Airflow |
| Data Warehouse    | PostgreSQL |
| Visualization     | Grafana |
| Deployment        | Docker Compose |

---

## ▶️ How to Run the Project

```bash
docker-compose up -d

Run Batch ETL Pipeline
docker exec -it spark bash

spark-submit jobs/bronze_ingest.py
spark-submit jobs/silver_transform.py
spark-submit jobs/gold_aggregations.py
spark-submit jobs/load_to_postgres.py
