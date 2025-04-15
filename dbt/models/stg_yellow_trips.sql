SELECT 
    tpep_pickup_datetime,
    PULocationID,
    fare_amount,
    passenger_count
FROM {{ source('nyc_taxi', 'raw_rides') }}
WHERE fare_amount > 0 
