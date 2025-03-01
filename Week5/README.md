Completed Week 5 in google cloud VM

---
SQL used:

Question3:
Select count(*) from yellow
where date(yellow.tpep_pickup_datetime) = '2024-10-15' and date(yellow.tpep_dropoff_datetime) = '2024-10-15';

Question4:
SELECT MAX(TIMESTAMPDIFF(SECOND, tpep_pickup_datetime, tpep_dropoff_datetime)) / 3600 AS max_duration_in_hours
FROM yellow;

Question6:
select count(yellow.PULocationID), zones.zone from yellow
inner join zones on zones.LocationID = yellow.PULocationID
group by zones.zone order by count(PULocationID);