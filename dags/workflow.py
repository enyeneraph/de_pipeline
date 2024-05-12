from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from pipeline.main import main

default_args={
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    dag_id = 'data_jobs',
    default_args=default_args,
    description='DE/DS Jobs Pipeline',
    schedule=None,
    template_searchpath="/opt/airflow/src/sql"
    # schedule_interval='@daily'
)

extract = PythonOperator(
    task_id="scraper", 
    python_callable=main,
    dag=dag
)

load = BashOperator(
    task_id="load",
    bash_command="$AIRFLOW_HOME/src/load.sh ",
    dag=dag
)

publish = BashOperator(
    task_id="publish",
    bash_command="$AIRFLOW_HOME/src/script.sh ",
    dag=dag
)


extract >> load >> publish


