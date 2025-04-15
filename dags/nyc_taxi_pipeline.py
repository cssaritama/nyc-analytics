from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

default_args = {
    'owner': 'cssaritama',
    'start_date': datetime(2023, 1, 1),
    'vars': {
        'data_lake_bucket': 'nyc-taxi-data-lake-2025'
    }
}

with DAG(
    'nyc_taxi_pipeline',
    default_args=default_args,
    schedule_interval='@monthly',
) as dag:

    ingest_to_bq = GCSToBigQueryOperator(
        task_id='ingest_to_bq',
        bucket='{{ var.value.data_lake_bucket }}',
        source_objects=['raw/yellow_tripdata_2023-*.parquet'], 
        destination_project_dataset_table='nyc_taxi.raw_rides',
        source_format='PARQUET',
        write_disposition='WRITE_TRUNCATE',
    )
