from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

model = joblib.load("km_model.pkl")
scaler = joblib.load("scaler_customer.pkl")

app = FastAPI(title="Customer Segmentation API")

class CustomerData(BaseModel):
    age: float
    annual_income: float
    spending_score: float


@app.get("/")
def home():
    return {"message": "KMeans Clustering API is running 🚀"}


@app.post("/predict")
def predict_cluster(data: CustomerData):
    input_data = np.array([[data.age, data.annual_income, data.spending_score]])

    scaled_data = scaler.transform(input_data)

    cluster = model.predict(scaled_data)

    return {
        "predicted_cluster": int(cluster[0])
    }

import requests

