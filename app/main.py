from fastapi import FastAPI, Body
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("models/model.joblib")

@app.get("/")
def home():
    return {"message": "Iris Prediction API is live!"}

@app.post("/predict/")
def predict(features: list = Body(...)):
    """
    Expects JSON body like:
    [[5.1, 3.5, 1.4, 0.2]]
    """
    features_array = np.array(features)
    prediction = model.predict(features_array)
    return {"prediction": prediction.tolist()}
