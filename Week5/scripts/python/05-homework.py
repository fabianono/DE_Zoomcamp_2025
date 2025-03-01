#!/usr/bin/env python


from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext



creds = '/home/fabianphng/.google/cred/gcpcred.json'

conf = SparkConf() \
    .setMaster('spark://de-zoomcamp.us-central1-c.c.my-project-57990-1714709310544.internal:7077') \
    .setAppName('homework_5') \
    .set("spark.jars","/home/fabianphng/lib/gcs-connector-hadoop3-2.2.5.jar") \
    .set("spark.hadoop.google.cloud.auth.service.account.enable","true") \
    .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile",creds)



sc = SparkContext(conf = conf)

hadoop_conf = sc._jsc.hadoopConfiguration()

hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", creds)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")



spark = SparkSession.builder \
    .config(conf=sc.getConf()) \
    .getOrCreate()


df_yellow = spark.read.option("header","true").parquet('/home/fabianphng/data-engineering-zoomcamp/05-batch/data/hmwk/yellow_tripdata_2024-10.parquet')

df_yellow.repartition(4).write.parquet('/home/fabianphng/data-engineering-zoomcamp/05-batch/data/hmwk/repartitioned')






