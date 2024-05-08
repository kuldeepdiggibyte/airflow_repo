from airflow import DAG

from airflow.operators import TriggerDagRunOperator

from datetime import datetime

# Define your DAG

with DAG(

        dag_id='question_4',

        description='Main DAG that triggers another DAG',

        schedule_interval='@daily',

        start_date=datetime(2024, 5, 1),

        catchup=False

) as dag:

    # Define the TriggerDagRunOperator task

    trigger_task = TriggerDagRunOperator(

        task_id='trigger_another_dag',

        trigger_dag_id='another_dag',  # Specify the DAG to trigger

        execution_date="{{ execution_date }}",  # Use the same execution date as the current DAG

    )