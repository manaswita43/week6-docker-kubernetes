from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("models/model.joblib")

@app.get("/")
def home():
    return {"message": "Iris Prediction API is live!"}

@app.post("/predict/")
def predict(features: list):
    prediction = model.predict([np.array(features)])
    return {"prediction": prediction.tolist()}
