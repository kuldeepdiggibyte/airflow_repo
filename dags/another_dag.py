from airflow import DAG

from airflow.operators import BashOperator

from datetime import datetime

# Define your another_dag DAG

with DAG(

        dag_id='another_dag',

        description='Another DAG triggered by main_dag',

        schedule_interval=None,  # This DAG won't be scheduled independently

        start_date=datetime(2024, 5, 1),

        catchup=False

) as dag:

    # Define tasks for another_dag

    bash_task = BashOperator(

        task_id="bash_task",

        bash_command='echo "Hello World"',

    )