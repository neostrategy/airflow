from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Função Python simples
def tarefa_teste():
    print("Executando tarefa de teste no Airflow!")

# Definição da DAG
with DAG(
    dag_id="dag_teste_basico",
    description="Uma DAG simples para teste",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",  # Executa diariamente
    catchup=False,              # Não executa tarefas retroativas
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["teste", "basico"]
) as dag:

    inicio = DummyOperator(task_id="inicio")

    tarefa = PythonOperator(
        task_id="tarefa_de_teste",
        python_callable=tarefa_teste
    )

    fim = DummyOperator(task_id="fim")

    # Definindo a ordem das tarefas
    inicio >> tarefa >> fim
