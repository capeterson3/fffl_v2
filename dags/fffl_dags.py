# PATH=$PATH:~/mnt/c/Users/Chris/Documents/Fantasy
# export PYTHONPATH=/mnt/c/Users/Chris/Documents/Fantasy/fffl

import sys, os

# from dotenv import load_dotenv

# load_dotenv()

# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# print("###############################path is set to: " + os.getenv("PYTHONPATH"))
from src import fffl

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["capeterson3@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

print("running fffl_dags...")

dag = DAG(
    "fffl_update",
    default_args=default_args,
    description="Update FFFL Scores",
    schedule_interval="* * * * *",
)

update_scores = PythonOperator(
    task_id="update_scoreboards",
    python_callable=fffl.updateScoreboards,
    op_kwargs={"year": 2019},
    dag=dag,
)

parse_scores = PythonOperator(
    task_id="parse_scores",
    python_callable=fffl.parse_scores,
    op_kwargs={"year": 2019, "week": 1},
    dag=dag,
)

update_scores >> parse_scores
