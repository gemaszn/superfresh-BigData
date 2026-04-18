import pandas as pd
from sqlalchemy import create_engine

usuario = "postgres"
password = "TU_PASSWORD"
host = "localhost"
puerto = "5432"
basedatos = "superfresh_db"

engine = create_engine(
    f"postgresql+psycopg2://{usuario}:{password}@{host}:{puerto}/{basedatos}"
)

df = pd.read_csv("data/processed/train_limpio.csv")
df.to_sql("train_limpio", engine, if_exists="replace", index=False)

print("Tabla train_limpio cargada correctamente en PostgreSQL")