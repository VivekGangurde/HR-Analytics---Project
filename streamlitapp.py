#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import requests
import json


st.title('HR-analytics App') #title to be shown
st.image('office.jpg') #add an image
st.header('Enter the employee data:') #header to be shown in app

JobSatisfaction = st.number_input('Job Satisfaction',min_value=0.00, max_value=1.00)
PerformanceRating = st.number_input('Performance Score',min_value=0.00, max_value=1.00)
StandardHours = st.number_input('Standard Hours',min_value=1)
Joblevel = st.slider('Job level', min_value=0, max_value=320)
YearsAtCompany = st.number_input(label = 'Number of years at company', min_value=0)
WorkLifeBalance = st.selectbox('Work Life Balance', [1,0], index = 1)
YearsSinceLastPromotion = st.selectbox('Promotion in last  years yes=1/no=0', [1,0], index=1)
Department = st.selectbox('Department', ['Human Resources', 'Research & Development', 'Sales'])
MonthlyIncome = st.selectbox('Salary Band', ['low', 'medium', 'high',])

names = ['JobSatisfaction', 'PerformanceRating', 'StandardHours',
       'Joblevel', 'YearsAtCompany', 'WorkLifeBalance',
       'YearsSinceLastPromotion', 'Department', 'MonthlyIncome']
params = [JobSatisfaction, PerformanceRating, StandardHours,
       Joblevel, YearsAtCompany, WorkLifeBalance,
       YearsSinceLastPromotion, Department, MonthlyIncome]
input_data = dict(zip(names, params))
output_ = None
if st.button('Predict'):
    try:
        # Use json= instead of data= with json.dumps
        output_ = requests.post(url='http://localhost:8000/predict', json=input_data)
        
        # Check if request was successful
        if output_ is not None and output_.status_code == 200:
            ans = output_.json()  # no need to eval
            
            output = 'Yes' if ans['prediction'] == 1 else 'No'
            if output == 'Yes':
                st.success("The employee might leave the company with a probability of {(ans['probability'])*100:.2f}%")
            else:
                st.success("The employee might not leave the company with a probability of {(1 - ans['probability'])*100:.2f}%")
        else:
            st.error("Failed to get a valid response from the server.")
            
    except Exception as e:
        st.error("Error connecting to API server: {e}")

# In[ ]:




