from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

default_args = {
    'owner': 'cssaritama',
    'start_date': datetime(2023, 1, 1),
    'retries': 2
}

with DAG(
    'nyc_taxi_prod',
    default_args=default_args,
    schedule_interval='@daily',
    tags=['production']
) as dag:

    load_to_bq = GCSToBigQueryOperator(
        task_id='load_daily_data',
        bucket='nyc-taxi-prod-cssaritama', 
        source_objects=['raw/yellow_tripdata_2023-*.parquet'],
        destination_project_dataset_table='nyc_taxi_prod.raw_trips',
        source_format='PARQUET',
        write_disposition='WRITE_TRUNCATE',
        time_partitioning={'type': 'DAY'},
        cluster_fields=['PULocationID']
    )
