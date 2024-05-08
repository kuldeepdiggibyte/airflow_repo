from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import BashOperator

default_args = {
    'owner': 'kuldeep',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
        dag_id="question_5",
        default_args=default_args,
        description="This is the first dag",
        start_date=datetime(2024, 5, 6, 2),
        schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world, this is the first task",
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo hey, I am task2 and will be running after task 1"
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo hey, I am the task3 and will run after the task2"
    )

    task4 = BashOperator(
        task_id="fourth_task",
        bash_command="echo hey, I am the task4 and will run after the task3"
    )

    # Task dependency method1
    task1.set_upstream(task2)
    task1.set_downstream(task3)
    task3.set_downstream(task4)
