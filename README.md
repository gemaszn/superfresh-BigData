# Proyecto SuperFresh

Proyecto de predicción de ventas para la cadena de supermercados SuperFresh, desarrollado para el módulo de Sistemas de Big Data.

## Objetivo
Construir un sistema capaz de:
- procesar datos históricos de ventas con PySpark,
- almacenar datos procesados en PostgreSQL,
- entrenar un modelo de predicción de ventas,
- generar predicciones,
- exponerlas mediante una API con FastAPI,
- visualizar resultados en Power BI.

## Tecnologías usadas
- Python
- PySpark
- PostgreSQL
- SQLAlchemy
- scikit-learn
- FastAPI
- Power BI

## Estructura del proyecto
```text
proyecto_superfresh/
├── api/
│   └── main.py
├── data/
│   ├── processed/
│   └── raw/
├── models/
├── screenshots/
├── src/
│   ├── 01_prueba_spark.py
│   ├── 02_lectura_csv.py
│   ├── 03_preprocesamiento_spark.py
│   ├── 04_cargar_postgresql.py
│   ├── 05_entrenar_modelo.py
│   ├── 06_generar_predicciones.py
│   └── 07_comparacion_modelos.py
├── requirements.txt
└── README.md
```

## Flujo del proyecto
Comprobar que Spark funciona.
Leer el dataset train.csv.
Limpiar y transformar los datos.
Guardar el dataset limpio en PostgreSQL.
Entrenar un modelo Random Forest.
Generar predicciones y guardarlas en PostgreSQL.
Publicar una API para consultar predicciones.
Visualizar resultados en Power BI.

## Ejecución
1. Activar entorno virtual
venv\Scripts\activate
2. Instalar dependencias
pip install -r requirements.txt
3. Ejecutar scripts
python .\src\01_prueba_spark.py
python .\src\02_lectura_csv.py
python .\src\03_preprocesamiento_spark.py
python .\src\04_cargar_postgresql.py
python .\src\05_entrenar_modelo.py
python .\src\06_generar_predicciones.py
python .\src\07_comparacion_modelos.py
4. Ejecutar la API
uvicorn api.main:app --reload
Endpoints de la API
GET / → comprobar funcionamiento
POST /predict → obtener una predicción de ventas
Dataset principal

Se ha trabajado principalmente con:
train.csv

## Resultados
El modelo principal utilizado ha sido Random Forest, evaluado con métricas:
MAE
RMSE
R²

Además, se ha comparado con un modelo de regresión lineal.

## Visualización
Se ha desarrollado un dashboard en Power BI con:
evolución temporal de ventas y predicciones,
ventas por familia de producto,
ventas por tienda,
tarjetas KPI,
filtros por tienda, familia y mes.

## Autor
Gema del Carmen Sánchez Navarro
