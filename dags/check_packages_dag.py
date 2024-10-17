import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
import subprocess
import sys

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'check_packages',
    default_args=default_args,
    description='Check installed packages in Composer environment',
    schedule_interval=None,
)

def check_packages():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'check'])
        print("All packages are compatible.")
    except subprocess.CalledProcessError:
        print("There are package compatibility issues.")
        raise

check_packages_task = PythonOperator(
    task_id='check_packages_task',
    python_callable=check_packages,
    dag=dag,
)