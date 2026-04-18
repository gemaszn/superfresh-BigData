from pyspark.sql import SparkSession

spark = SparkSession.builder \
   .appName("PruebaSpark") \
   .master("local[*]") \
   .getOrCreate()

print("Spark funciona")
print("Version de Spark:", spark.version)

spark.stop()
