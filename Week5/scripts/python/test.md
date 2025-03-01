/home/fabianphng/scripts/python/05-spark-cluster.py \
    --input_green=/home/fabianphng/data-engineering-zoomcamp/05-batch/data/pq/green/2020/* \
    --input_yellow=/home/fabianphng/data-engineering-zoomcamp/05-batch/data/pq/yellow/2020/* \
    --output=/home/fabianphng/data-engineering-zoomcamp/05-batch/data/report/2020/


URL="spark://de-zoomcamp.us-central1-c.c.my-project-57990-1714709310544.internal:7077"

spark-submit \
    --master="${URL}" \
    /home/fabianphng/scripts/python/05-spark-cluster.py \
        --input_green=/home/fabianphng/data-engineering-zoomcamp/05-batch/data/pq/green/2021/* \
        --input_yellow=/home/fabianphng/data-engineering-zoomcamp/05-batch/data/pq/yellow/2021/* \
        --output=/home/fabianphng/data-engineering-zoomcamp/05-batch/data/report/2021/

gcloud dataproc jobs submit pyspark \
    --cluster=de-zoomcamp-cluster \
    --region=us-central1 \
    gs://de-zoomcamp-05/code/05-spark-cluster.py \
    -- \
        --input_green=gs://de-zoomcamp-05/pq/green/2020/*/ \
        --input_yellow=gs://de-zoomcamp-05/pq/yellow/2020/*/ \
        --output=gs://de-zoomcamp-05/report-2020

gcloud dataproc jobs submit pyspark \
    --cluster=de-zoomcamp-cluster \
    --region=us-central1 \
    --jars=gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.23.2.jar \
    gs://de-zoomcamp-05/code/05-spark-cluster-bigquery.py \
    -- \
        --input_green=gs://de-zoomcamp-05/pq/green/2020/*/ \
        --input_yellow=gs://de-zoomcamp-05/pq/yellow/2020/*/ \
        --output=zoomcamp.report-2020