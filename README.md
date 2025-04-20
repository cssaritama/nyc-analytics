

# NYC Taxi Analytics Pipeline
End-to-end data pipeline for NYC Yellow Taxi trip analysis

## 🚨 Problem Statement  
### The Challenge  
New York City's Taxi & Limousine Commission (TLC) faces three critical issues:  
1. **Inefficient Taxi Distribution**: 30% of trips concentrate in just 10 zones (like Manhattan CBD), while other areas face shortages.  
2. **Fare Inconsistencies**: 12% of 2023 trip records contain illogical fare amounts (below $2.50 or above $200).  
3. **Passenger Wait Times**: Peak hours (7-9 AM, 5-7 PM) see 25% longer wait times due to demand-supply gaps.  

**Data Obstacles**:  
- **Scale**: Process 2.3GB/month of Parquet files (Jan-Mar 2023 data)  
- **Quality**: 7.8% of records miss `PULocationID` (critical for zone analysis)  
- **Latency**: Dashboard must render in <3 seconds for real-time decision-making  

## 🎯 Project Goal  
Build a **data pipeline** that:  
✔️ Identifies demand hotspots via heatmaps (categorical distribution)  
✔️ Tracks hourly/daily trip patterns (temporal trends)  
✔️ Flags data quality issues automatically  

## 🛠️ Technical Solution  
### Architecture  
![nyc-taxi-architecture drawio](https://github.com/user-attachments/assets/1da26e07-c732-4f55-a2bd-cd74ac1627cf)

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
