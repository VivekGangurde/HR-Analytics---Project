#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = load('my-model2')

class HRData(BaseModel):
    JobSatisfaction     : float
    PerformanceRating   : float
    StandardHours       : int
    Joblevel            : int
    OverTime            : int
    PercentSalaryHike   : int
    YearsAtCompany      : int    
    WorkLifeBalance     : int
    YearsSinceLastPromotion: int
    Department          : str
    MonthlyIncome       : str

# Load model 
model = joblib.load("model1.pkl")

# Convert categorical inputs (example; adjust according to your model)
def preprocess_input(data: HRData):
    department_map = {'Human Resources': 0, 'Research & Development': 1, 'Sales': 2}
    income_map = {'low': 0, 'medium': 1, 'high': 2}
    return np.array([[
        data.JobSatisfaction,
        data.PerformanceRating,
        data.StandardHours,
        data.Joblevel,
        data.YearsAtCompany,
        data.WorkLifeBalance,
        data.YearsSinceLastPromotion,
        department_map[data.Department],
        income_map[data.MonthlyIncome]
    ]])

@app.post("/predict")
def predict():
    return {
        "prediction": 1,
        "probability": 0.85
    }
  "JobSatisfaction": 0.7,
  "PerformanceRating": 0.8,
  "StandardHours": 40,
  "Joblevel": 2,
  "YearsAtCompany": 5,
  "WorkLifeBalance": 1,
  "YearsSinceLastPromotion": 0,
  "Department": "Sales",
  "MonthlyIncome": "medium"
}
{
  "prediction": 1,
  "probability": 0.76
}
def predict(data: HRData):
    input_array = preprocess_input(data)
    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0][1]
    return {"prediction": int(prediction), "probability": float(probability)}

uvicorn main:app --reload --host 0.0.0.0 --port 8000





# In[ ]:




