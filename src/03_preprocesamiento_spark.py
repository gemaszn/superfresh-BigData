from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, year, month, dayofmonth, dayofweek, when

spark = SparkSession.builder \
    .appName("Preprocesamiento") \
    .master("local[*]") \
    .getOrCreate()

# Leer el CSV principal
df = spark.read.csv("data/raw/train.csv", header=True, inferSchema=True)

# Eliminar filas con valores nulos
df = df.dropna()

# Convertir la columna date a tipo fecha
df = df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

# Crear variables de tiempo
df = df.withColumn("year", year(col("date")))
df = df.withColumn("month", month(col("date")))
df = df.withColumn("day", dayofmonth(col("date")))
df = df.withColumn("day_of_week", dayofweek(col("date")))

# Crear variable fin de semana
df = df.withColumn(
    "fin_de_semana",
    when(col("day_of_week").isin([1, 7]), 1).otherwise(0)
)

# Mostrar resultado
print("Primeras filas del dataset transformado:")
df.show(10)

# Guardar CSV limpio
df.toPandas().to_csv("data/processed/train_limpio.csv", index=False)

print("Archivo limpio guardado en data/processed/train_limpio.csv")

spark.stop()