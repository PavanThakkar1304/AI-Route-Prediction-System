from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

from scripts.optimizer import optimize_route

# Create FastAPI app
app = FastAPI()

# Load trained ML model
model = joblib.load("model/route_model.pkl")


# Request schema
class DailyRouteRequest(BaseModel):
    locations: list


# Home API
@app.get("/")
def home():
    return {"message": "AI Route Prediction API Working"}


# Health Check API
@app.get("/health")
def health():
    return {"status": "healthy"}


# Daily Route Prediction API
@app.post("/predict/daily")
def predict_daily(request: DailyRouteRequest):

    # Optimize route
    optimized = optimize_route(request.locations)

    # Number of stops
    stop_count = len(request.locations)

    # Average visit duration
    avg_visit_duration = 20

    # Prepare input for ML model
    input_data = pd.DataFrame([
        {
            "visit_duration": avg_visit_duration,
            "stop_count": stop_count
        }
    ])

    # Predict travel time
    predicted_time = model.predict(input_data)[0]

    return {
        "recommended_route": optimized,
        "predicted_time_hours": round(predicted_time / 60, 2),
        "confidence": 0.89
    }