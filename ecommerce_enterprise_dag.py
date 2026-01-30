from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {"start_date": datetime(2025, 1, 1)}

with DAG("enterprise_ecommerce_pipeline",
         schedule_interval="@daily",
         default_args=default_args,
         catchup=False) as dag:

    bronze = BashOperator(
        task_id="batch_ingestion",
        bash_command="spark-submit jobs/bronze_ingest.py"
    )

    silver = BashOperator(
        task_id="transform_clean",
        bash_command="spark-submit jobs/silver_transform.py"
    )

    gold = BashOperator(
        task_id="analytics_layer",
        bash_command="spark-submit jobs/gold_aggregations.py"
    )

    warehouse = BashOperator(
        task_id="load_postgres",
        bash_command="spark-submit jobs/load_to_postgres.py"
    )

    bronze >> silver >> gold >> warehouse
