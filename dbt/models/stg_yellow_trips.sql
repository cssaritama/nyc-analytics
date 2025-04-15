SELECT 
    tpep_pickup_datetime,
    PULocationID,
    fare_amount
FROM {{ source('nyc_taxi', 'raw_rides') }}
