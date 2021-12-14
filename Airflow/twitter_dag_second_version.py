import sys
sys.path.append("[/home/lucasquemelli/datapipeline/airflow/plugins]")

from datetime import datetime
from os.path import join
from airflow.models import DAG
from airflow.operators.alura import TwitterOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

with DAG(dag_id="twitter_dag", start_date=datetime.now()) as dag:
    twitter_operator = TwitterOperator(
        task_id = "twitter_aluraonline",
        query = "AluraOnline",
        file_path =join(
            "/home/lucasquemelli/datapipeline/datalake",
            "twitter_aluraonline",
            "extract_date={{ ds }}",
            "AluraOnline_{{ ds_nodash }}.json"
        )
    )

    twitter_transform = SparkSubmitOperator(
        task_id = "transformation_twitter_aluraonline",
        application = "/home/lucasquemelli/datapipeline/spark/transformation_final_version.py",
        name = "twitter_transformation",
        application_args = [
            "--src",
            "/home/lucasquemelli/datapipeline/datalake/bronze/twitter_aluraonline/extract_date=2021-12-05",
            "--dest",
            "/home/lucasquemelli/datapipeline/datalake/silver/twitter_aluraonline",
            "--process_date",
            "{{ ds }}",
        ]
    )