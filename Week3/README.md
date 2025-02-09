-- create external table

Create or Replace External table `my-project-57990-1714709310544.zoomcamp.external_yellow_tripdata`
Options (
  format = 'parquet',
  uris = ['gs://de-zoomcamp-hmw3-2025/yellow-trip-data/yellow_tripdata_2024-*.parquet']
);

-- used web ui to create bigquery regular table


--create external partitioned and clustered table

Create or replace table my-project-57990-1714709310544.zoomcamp.external_yellow_tripdata_clustered_partitioned
partition by DATE(tpep_dropoff_datetime)
cluster by VendorID AS
Select  * from my-project-57990-1714709310544.zoomcamp.external_yellow_tripdata;


-- create partitioned and clustered bigquery regular table

Create or replace table my-project-57990-1714709310544.zoomcamp.yellow_tripdata_clustered_partitioned
partition by DATE(tpep_dropoff_datetime)
cluster by VendorID AS
Select  * from my-project-57990-1714709310544.zoomcamp.yellow_tripdata;


-- qn1

select count(*) from my-project-57990-1714709310544.zoomcamp.external_yellow_tripdata;


-- qn2

select count(distinct PULocationID) from my-project-57990-1714709310544.zoomcamp.yellow_tripdata;
select count(distinct PULocationID) from my-project-57990-1714709310544.zoomcamp.external_yellow_tripdata;


-- qn4

select count(*) from my-project-57990-1714709310544.zoomcamp.external_yellow_tripdata where fare_amount=0;


--qn6

select distinct VendorID from my-project-57990-1714709310544.zoomcamp.yellow_tripdata_clustered_partitioned 
where date(tpep_dropoff_datetime)>= '2024-03-01' and date(tpep_dropoff_datetime)<= '2024-03-15';

select distinct VendorID from my-project-57990-1714709310544.zoomcamp.yellow_tripdata 
where date(tpep_dropoff_datetime)>= '2024-03-01' and date(tpep_dropoff_datetime)<= '2024-03-15';


-- bonus

select count(*) from my-project-57990-1714709310544.zoomcamp.yellow_tripdata;

