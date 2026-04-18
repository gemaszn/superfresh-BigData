import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Leyendo datos...")
df = pd.read_csv("data/processed/train_limpio.csv")

print("Tomando muestra...")
df = df.sample(n=10000, random_state=42)

print("Creando variables dummy...")
df = pd.get_dummies(df, columns=["family", "store_nbr"], drop_first=True)

X = df.drop(columns=["sales", "date"], errors="ignore")
y = df["sales"]

print("Separando train/test...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelos = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(
        n_estimators=20,
        max_depth=8,
        random_state=42,
        n_jobs=-1
    )
}

for nombre, modelo in modelos.items():
    print(f"Entrenando modelo: {nombre}")
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)

    print(f"Modelo: {nombre}")
    print(f"MAE: {mae}")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")
    print("-" * 30)