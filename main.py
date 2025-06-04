#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import xgboost as xgb

app = FastAPI()

# Load model
model = xgb.XGBClassifier()
model.load_model("model1.json")

# Define input schema
class HRData(BaseModel):
    Age: int
    BusinessTravel: str
    DailyRate: int
    Department: str
    DistanceFromHome: int
    Education: int
    EducationField: str
    EnvironmentSatisfaction: int
    Gender: str
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobRole: str
    JobSatisfaction: float
    MaritalStatus: str
    MonthlyIncome: float
    MonthlyRate: int
    NumCompaniesWorked: int
    OverTime: str
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
async def welcome():
    return {"message": "Welcome to HR Analytics API"}

@app.post("/predict")
async def predict(input: HRData):
    input_df = pd.DataFrame([input.dict()])
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    return {
        "prediction": int(prediction[0]),
        "probability": float(probability[0][1])
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
