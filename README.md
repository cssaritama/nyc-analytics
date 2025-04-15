# NYC Taxi Analytics (2023)
Pipeline to analyze NYC taxi trips using real 2023 data.

## Architecture
- **Data Lake**: GCS (`nyc-taxi-data-lake-2025-cssaritama`)
- **Data Warehouse**: BigQuery (`nyc_taxi_analytics.raw_rides`)


## How to Run
1. **Infrastructure**:
   ```bash
   cd terraform && terraform apply -var="project_id=nyc-taxi-123456"  
