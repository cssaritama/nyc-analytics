SELECT 
    PULocationID,
    AVG(fare_amount) AS avg_fare
FROM {{ ref('stg_yellow_trips') }}
GROUP BY 1
