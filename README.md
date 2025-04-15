# NYC Taxi Analytics Pipeline
End-to-end data pipeline for NYC Yellow Taxi trip analysis

## Architecture
- **Data Lake**: GCS (`nyc-taxi-data-lake-2025-cssaritama`)
- **Data Warehouse**: BigQuery (`nyc_taxi_prod`)
- **Dashboard**: [View Production Dashboard](https://lookerstudio.google.com/reporting/1a2b3c4d-5678-90ab-cdef-1234567890ab)

## Deployment
```bash
# 1. Set up infrastructure
cd terraform && terraform apply

# 2. Load sample data
gsutil cp data/sample_trips.parquet gs://nyc-taxi-data-lake-2025-cssaritama/raw/

# 3. Run transformations
cd dbt && dbt run --target prod
