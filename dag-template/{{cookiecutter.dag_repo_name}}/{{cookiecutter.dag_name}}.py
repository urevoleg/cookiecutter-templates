import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import dataclasses
import datetime as dt
import logging

import typing as t

from airflow.decorators import dag, task
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import get_current_context

args = {
    "owner": "{{dag_owner}}",
    'retries': 5,
    'retry_delay': dt.timedelta(minutes=3),
}


@dag(dag_id="dag_{{dag_name}}",
     schedule_interval=None,
     start_date=dt.datetime(2024, 2, 1),
     catchup=False,
     default_args=args)
def create_dag():
    start = EmptyOperator(
        task_id="start",
    )

    end = EmptyOperator(
        task_id="end",
        trigger_rule=TriggerRule.ALL_SUCCESS
    )

    start >> end