import sys
sys.path.append("[/home/lucasquemelli/datapipeline/airflow/plugins]")

from datetime import datetime
from os.path import join
from pathlib import Path

from airflow.models import DAG
from airflow.operators.alura import TwitterOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.utils.dates import days_ago

ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(6),
}

#BASE_FOLDER = "/home/lucasquemelli/datapipeline/datalake/{stage}/twitter_aluraonline/{partition}"

#PARTITION_FOLDER = "extract_date={{ ds }}"

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"

with DAG(dag_id="twitter_dag",
         default_args=ARGS,
         schedule_interval="0 9 * * *",
         max_active_runs=1) as dag:
    twitter_operator = TwitterOperator(
        task_id="twitter_aluraonline",
        query="AluraOnline",
        file_path="/home/lucasquemelli/datapipeline/datalake/bronze/twitter_aluraonline/extract_date={{ ds }}",
        start_time=(
            "{{"
            f"execution_date.strftime('{TIMESTAMP_FORMAT}')"
            "}}"
        ),
        end_time=(
            "{{"
            f"next_execution_date.strftime('{TIMESTAMP_FORMAT}')"
            "}}"
        )
    )

    twitter_transform = SparkSubmitOperator(
        task_id = "transformation_twitter_aluraonline",
        application = "/home/lucasquemelli/datapipeline/spark/transformation_final_version.py",
        name = "twitter_transformation",
        application_args = [
            "--src",
            "/home/lucasquemelli/datapipeline/datalake/bronze/twitter_aluraonline/extract_date={{ ds }}",
            "--dest",
            "/home/lucasquemelli/datapipeline/datalake/silver/twitter_aluraonline",
            "--process_date",
            "{{ ds }}",
        ]
    )

    twitter_operator >> twitter_transform