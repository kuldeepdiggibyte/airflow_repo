from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators import PythonOperator

default_args = {
    'owner':'Kuldeep',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

def greet(name,age):
    print(f"hello world, my name is {name},"
          f"and i am {age} years old!")

def sum():
    a = 4
    b = 3
    print(a+b)

with DAG(
    default_args=default_args,
    dag_id="python_operator_v21",
    description='this is python operator',
    start_date=datetime(2024,4,5)
) as dag:

    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs = {'name':'Kuldeep','age':21}
    )

    task2 = PythonOperator(
        task_id="sum",
        python_callable=sum
    )
    task1>>task2