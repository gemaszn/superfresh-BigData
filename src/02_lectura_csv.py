from pyspark.sql import SparkSession

spark = SparkSession.builder \
   .appName("LecturaCSV") \
   .master("local[*]") \
   .getOrCreate()

df = spark.read.csv("data/raw/train.csv", header=True, inferSchema=True)

print("Esquema:")
df.printSchema()

print("Primeras filas:")
df.show(10)

spark.stop()
