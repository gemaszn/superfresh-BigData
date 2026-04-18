import pandas as pd
import joblib
from sqlalchemy import create_engine, URL

usuario = "postgres"
password = "TU_PASSWORD"
host = "localhost"
puerto = "5432"
basedatos = "superfresh_db"

url = URL.create(
    "postgresql+psycopg2",
    username=usuario,
    password=password,
    host=host,
    port=puerto,
    database=basedatos,
)

engine = create_engine(url)

print("Leyendo datos limpios...")
df_original = pd.read_csv("data/processed/train_limpio.csv")

print("Preparando variables...")
df_modelo = pd.get_dummies(df_original, columns=["family", "store_nbr"], drop_first=True)

print("Cargando modelo...")
modelo = joblib.load("models/random_forest.pkl")
columnas_modelo = joblib.load("models/columnas_modelo.pkl")

print("Generando predicciones...")
X = df_modelo.drop(columns=["sales", "date"], errors="ignore")
X = X.reindex(columns=columnas_modelo, fill_value=0)

df_original["prediccion_sales"] = modelo.predict(X)

print("Guardando en PostgreSQL...")
df_original.to_sql("predicciones", engine, if_exists="replace", index=False)

print("Predicciones guardadas en PostgreSQL")