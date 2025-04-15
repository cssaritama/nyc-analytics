# NYC Taxi Analytics Dashboard
End-to-end data pipeline for analyzing NYC taxi trips.

## Pipeline Architecture
1. **Data Lake**: GCS (raw Parquet files).
2. **Data Warehouse**: BigQuery (partitioned by date).
3. **Transformations**: dbt.
4. **Dashboard**: Looker Studio.

## How to Run
1. **Infra**: `cd terraform && terraform apply`.
2. **Airflow**: Upload `dags/nyc_taxi_pipeline.py` to Composer.
3. **dbt**: Run `dbt run` inside `dbt/` folder.
