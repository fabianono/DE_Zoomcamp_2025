SQL Answers for:

Question 3:
select count(*) from green_taxi_data where lpep_pickup_datetime < '2019-11-01' and lpep_pickup_datetime >= '2019-10-01'and lpep_dropoff_datetime< '2019-11-01'and trip_distance <= 1

select count(*) from green_taxi_data where lpep_pickup_datetime < '2019-11-01' and lpep_pickup_datetime >= '2019-10-01'and lpep_dropoff_datetime< '2019-11-01'and trip_distance > 1 and trip_distance <= 3

select count(*) from green_taxi_data where lpep_pickup_datetime < '2019-11-01' and lpep_pickup_datetime >= '2019-10-01'and lpep_dropoff_datetime< '2019-11-01'and trip_distance > 3 and trip_distance <= 7

select count(*) from green_taxi_data where lpep_pickup_datetime < '2019-11-01' and lpep_pickup_datetime >= '2019-10-01'and lpep_dropoff_datetime< '2019-11-01'and trip_distance > 7 and trip_distance <= 10

select count(*) from green_taxi_data where lpep_pickup_datetime < '2019-11-01' and lpep_pickup_datetime >= '2019-10-01'and lpep_dropoff_datetime< '2019-11-01'and trip_distance > 10


Question 4:
select lpep_pickup_datetime from green_taxi_data where trip_distance = 
    (
        select max(trip_distance) from green_taxi_data
    )

Question 5:
SELECT 
    taxi_zones."Zone", 
    PU_Table.zone_PU_sum 
FROM 
    taxi_zones 
INNER JOIN (
    SELECT 
        "PULocationID", 
        SUM(total_amount) AS zone_PU_sum 
    FROM 
        green_taxi_data 
    WHERE 
        green_taxi_data.lpep_pickup_datetime::date = '2019-10-18'
    GROUP BY 
        "PULocationID"
    HAVING 
        SUM(total_amount) > 13000
) AS PU_Table 
ON 
    PU_Table."PULocationID" = taxi_zones."LocationID"
ORDER BY 
    PU_Table.zone_PU_sum DESC
LIMIT 3;


Question 6:
SELECT 
    do_table."Zone" AS dropoff_location, 
    green_taxi_data.tip_amount 
FROM 
    taxi_zones do_table
INNER JOIN 
    green_taxi_data 
    ON do_table."LocationID" = green_taxi_data."DOLocationID"
INNER JOIN 
    taxi_zones pu_table 
    ON pu_table."LocationID" = green_taxi_data."PULocationID"
WHERE 
    pu_table."Zone" = 'East Harlem North'
ORDER BY 
    green_taxi_data.tip_amount DESC
LIMIT 1;
