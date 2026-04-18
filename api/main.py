from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API SuperFresh")

modelo = joblib.load("models/random_forest.pkl")
columnas_modelo = joblib.load("models/columnas_modelo.pkl")


class DatosEntrada(BaseModel):
    store_nbr: int
    family: str
    onpromotion: int
    anio: int
    mes: int
    dia: int
    dia_semana: int
    fin_de_semana: int


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}


@app.post("/predict")
def predict(data: DatosEntrada):
    df = pd.DataFrame([data.dict()])

    # Convertir igual que en el entrenamiento
    df = pd.get_dummies(df, columns=["family", "store_nbr"], drop_first=False)

    # Asegurar mismas columnas que el modelo
    for col in columnas_modelo:
        if col not in df.columns:
            df[col] = 0

    df = df.reindex(columns=columnas_modelo, fill_value=0)

    pred = modelo.predict(df)[0]

    return {"prediccion_sales": float(pred)}