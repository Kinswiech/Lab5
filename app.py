from fastapi import FastAPI, HTTPException
from sklearn.linear_model import LinearRegression
import numpy as np
import os

app = FastAPI()

API_KEY = os.environ.get("MY_API_KEY", "brak_klucza")

model = LinearRegression()
model.fit(np.array([[30], [50], [80]]), np.array([150000, 250000, 400000]))

@app.get("/predict")
def predict(powierzchnia: float):
    predykcja = model.predict([[powierzchnia]])
    return {"predykcja_ceny": float(predykcja[0]), "debug_key": API_KEY}