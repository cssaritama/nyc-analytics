SELECT 
    PULocationID,
    AVG(fare_amount) AS avg_fare,
    COUNT(*) AS total_trips
FROM {{ ref('stg_yellow_trips') }}
GROUP BY 1
