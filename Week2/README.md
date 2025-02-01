Sql queries used:

Qns 3:
select count(unique_row_id) from yellow_tripdata where filename like '%2020%'

Qns4:
select count(unique_row_id) from green_tripdata where filename like '%2020%'

Qns5:
select count(unique_row_id) from yellow_tripdata where filename = 'yellow_tripdata_2021-03.csv'