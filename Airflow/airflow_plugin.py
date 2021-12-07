import sys
sys.path.append("[/home/lucasquemelli/datapipeline/airflow/plugins]")

from airflow.plugins_manager import AirflowPlugin
from operators.twitter_operator import TwitterOperator

class AluraAirflowPlugin(AirflowPlugin):
    name = "alura"
    operators = [TwitterOperator]