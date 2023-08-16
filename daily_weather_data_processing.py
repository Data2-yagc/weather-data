from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "daily_weather_data_processing",
    default_args={
        "depends_on_past": False,
        "email": ["hei.tahiry@gmail"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="DAG to run daily weather data processing",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 8, 12),
    catchup=False,
    tags=["data_processing"],
) as dag:

    t1 = BashOperator(
        task_id="run_jupyter_script",
        bash_command="jupyter nbconvert --to notebook --execute /Users/tahiry/Tana_Weather.ipynb",
    )

    dag.doc_md = dedent(
        """\
    #### DAG Documentation
    This DAG runs a Jupyter Notebook script daily to fetch and transform weather data.
    """
    )

    t1.doc_md = dedent(
        """\
    #### Task Documentation
    This task executes the Jupyter Notebook script.
    """
    )

