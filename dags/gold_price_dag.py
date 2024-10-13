from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.operators.compute import ComputeEngineStartInstanceOperator, ComputeEngineStopInstanceOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime, timedelta
from data_sources import fetch_gold_price as api_fetch_gold_price
from pubsub_producer import publish_to_pubsub
import os
import sys



from data_sources import fetch_gold_price as api_fetch_gold_price
from pubsub_producer import publish_to_pubsub

PROJECT_ID = 'de-goldprice'
ZONE = 'us-west1-a'  # Replace with your actual zone
INSTANCE_NAME = 'spark-instance'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'gold_price_pipeline',
    default_args=default_args,
    description='A DAG for the Gold Price pipeline',
    schedule_interval=timedelta(days=1),
)

def fetch_gold_price(**kwargs):
    date_str = kwargs['ds']  # Airflow provides the execution date as 'ds'
    gold_price_data = api_fetch_gold_price(date_str)
    if gold_price_data:
        # Publish to Pub/Sub
        publish_to_pubsub('gold-prices', gold_price_data)
        return "Gold price data fetched and published successfully"
    else:
        raise ValueError("Failed to fetch gold price data")

fetch_task = PythonOperator(
    task_id='fetch_gold_price',
    python_callable=fetch_gold_price,
    dag=dag,
)

start_instance = ComputeEngineStartInstanceOperator(
    task_id='start_instance',
    project_id=PROJECT_ID,
    zone=ZONE,
    instance_name=INSTANCE_NAME,
    dag=dag,
)

run_clean_transform = SSHOperator(
    task_id='run_clean_transform',
    ssh_hook='spark_instance_ssh_hook',
    command='spark-submit /path/to/clean_transform.py',
    dag=dag,
)

run_load_to_bigquery = SSHOperator(
    task_id='run_load_to_bigquery',
    ssh_hook='spark_instance_ssh_hook',
    command='spark-submit /path/to/load_to_bigquery.py',
    dag=dag,
)

stop_instance = ComputeEngineStopInstanceOperator(
    task_id='stop_instance',
    project_id=PROJECT_ID,
    zone=ZONE,
    instance_name=INSTANCE_NAME,
    dag=dag,
)

fetch_task >> start_instance >> run_clean_transform >> run_load_to_bigquery >> stop_instance