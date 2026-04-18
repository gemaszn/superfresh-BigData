import pandas as pd
import joblib
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Leyendo datos...")
df = pd.read_csv("data/processed/train_limpio.csv")

# Tomar una muestra para que el entrenamiento sea rápido
print("Tomando muestra...")
df = df.sample(n=50000, random_state=42)

# Convertir variables categóricas a numéricas
print("Creando variables dummy...")
df = pd.get_dummies(df, columns=["family", "store_nbr"], drop_first=True)

# Variables predictoras y objetivo
X = df.drop(columns=["sales", "date"], errors="ignore")
y = df["sales"]

print("Separando train/test...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
print("Entrenando modelo...")
modelo = RandomForestRegressor(
    n_estimators=30,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

modelo.fit(X_train, y_train)

print("Haciendo predicciones...")
pred = modelo.predict(X_test)

mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

os.makedirs("models", exist_ok=True)

joblib.dump(modelo, "models/random_forest.pkl")
joblib.dump(list(X.columns), "models/columnas_modelo.pkl")

print("Modelo guardado correctamente")