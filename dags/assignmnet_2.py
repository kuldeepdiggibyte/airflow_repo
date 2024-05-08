from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators import BashOperator


default_args = {
    'owner':'kuldeep',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id = "bash_dag_v2",
    default_args=default_args,
    description="this is from bash dag",
    start_date=datetime(2024, 5, 1),
    schedule_interval='@daily'
) as dag:

    task1 = BashOperator(
        task_id='first_bash',
        bash_command="echo hello world, this is my first task!"

    )

    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo hey, I am task 2 and will be running after my task first"
    )
    task3 = BashOperator(
        task_id = "third_task",
        bash_command = "echo hey, I am task3 and will be running after task 1 "
    )

task1.set_downstream(task2)
task1.set_downstream(task3)

