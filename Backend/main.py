from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
import os

app = FastAPI()

# Load pre-trained model
model = XGBClassifier()
model.load_model("xgb_model.json")

# Define input schema using Pydantic
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
async def predict(data: HRData):
    try:
        input_df = pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)

        return {
            "prediction": int(prediction[0]),
            "probability": float(probability[0][1])
        }
    except Exception as e:
        print(f"Prediction error: {e}")
        return {"error": "Prediction failed", "details": str(e)}

# Single entry point for deployment (Render, local, etc.)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
