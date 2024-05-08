from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime


def test():
    print("This is kuldeep")


with DAG(
        dag_id="kuldeep-dag",
        start_date=datetime(2024, 5, 8),
        schedule_interval='@daily',
        catchup=False
) as dag:
    sample = PythonOperator(
        task_id="kuldeep-1",
        python_callable=test
    )



