#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import pandas as pd
import json
import uvicorn

app = FastAPI()

model = load('my-model2')

class user_input(BaseModel):
    JobSatisfaction     : int
    PerformanceRating   : int
    StandardHours       : int
    Job level           : int
    OverTime            : int
    PercentSalaryHike   : int
    YearsAtCompany      : int    
    WorkLifeBalance     : int
    YearsSinceLastPromotion: int
    Department          : str
    MonthlyIncome       : str

def predict(data):
    Department = ['Human Resources', 'Research & Development', 'Sales']
    data[-2] = Department.index(data[-2])
    MonthlyIncome = ['0', '50000', '5000']
    data[-1] = MonthlyIncome.index(data[-1])

    columns = ['JobSatisfaction', 'PerformanceRating', 
                'StandardHours', 'Job level', 'YearsAtCompany', 
                'WorkLifeBalance', 'YearsSinceLastPromotion','Department', 'MonthlyIncome']
    #d = dict(zip(columns, data))
    
    prediction = model.predict( pd.DataFrame([data], columns= columns))
                                 
    
    proba = model.predict_proba(pd.DataFrame([data], columns= columns))
                                             
    return prediction, proba


@app.get('/')
async def welcome():
    return f'Welcome to HR api'


@app.post('/predict')
async def func(Input:user_input):
    data = [Input.JobSatisfaction, Input.PerformanceRating, Input.BusinessTravel, Input.StandardHours, Input.Job level, Input.YearsAtCompany, Input.WorkLifeBalance, Input.YearsSinceLastPromotion, Input.Department,Input.MonthlyIncome]
    
 
    pred, proba = predict(data)
    output = {'prediction':int(pred[0]), 'probability':float(proba[0][1])}
    
    return json.dumps(output)
if __name__ == "__main__":
    uvicorn.run("hr_analytics_api:app", host="0.0.0.0", port=8000, log_level="info", reload=True)


# In[ ]:




