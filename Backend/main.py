#!/usr/bin/env python
# coding: utf-8
from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
from xgboost import XGBClassifier
import os

# Add slowapi for rate limiting
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

# Configure limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded. Please wait and try again."}
    )

# Load model
model = XGBClassifier()
model.load_model("xgb_model.json")

# Input schema
class HRData(BaseModel):
    Age: int
    BusinessTravel: int
    DailyRate: int
    Department: int
    DistanceFromHome: int
    Education: int
    EducationField: int
    EnvironmentSatisfaction: int
    Gender: int
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobRole: int
    JobSatisfaction: float
    MaritalStatus: int
    MonthlyIncome: float
    MonthlyRate: int
    NumCompaniesWorked: int
    OverTime: int
    PercentSalaryHike: int
    PerformanceRating: float
    RelationshipSatisfaction: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int

@app.get("/")
async def home():
    return {"message": "Welcome to HR Analytics Prediction API"}

@app.post("/predict")
@limiter.limit("5/minute")  # Allow 5 requests per minute per IP
async def predict(data: HRData, request: Request):
    try:
        input_df = pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)

        return {
            "prediction": int(prediction[0]),
            "probability": float(probability[0][1])
        }
    except Exception as e:
        return {"error": "Prediction failed", "details": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
