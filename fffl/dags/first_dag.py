from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

args = {
    "owner": "Airflow",
    "start_date": days_ago(1),
}

dag = DAG(dag_id="first_dag", default_args=args, schedule_interval="* * * * *")

task_one = BashOperator(
    task_id="one_and_only_task", bash_command="echo Hello World", dag=dag
)

task_one
