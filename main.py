#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries:

# In[62]:

# # HR Analytics

import numpy as np
import pandas as pd
import pickle
from pickle import dump
from pickle import load
import streamlit as st
from xgboost import XGBClassifier





# Load the saved model

xgb_clf = XGBClassifier()
xgb_clf = pickle.load(open('test.pkl','rb'))




# Streamlit app title
st.title("Model Prediction App - Employee Turnover")

# Sidebar with input widgets
st.sidebar.header("User Input Features")

# Example input features (replace with your actual feature names)
Jobsatisfaction = st.sidebar.slider("JobSatisfaction", min_value=1.0, max_value=4.0, value=0.01)
PerformanceRating = st.sidebar.slider("PerformanceRating", min_value=3.0, max_value=4.0, value=0.01)
WorkLifeBalance = st.sidebar.slider("WorkLifeBalance", min_value=1, max_value=4, value=1)
HourlyRate = st.sidebar.slider("HourlyRate", min_value=30, max_value=200, value=1)
TotalWorkingYears = st.sidebar.slider("TotalWorkingYears", min_value=0, max_value=50, value=1)
DistanceFromHome = st.sidebar.slider("DistanceFromHome", min_value=1, max_value=40, value=1)
YearsSinceLastPromotion = st.sidebar.slider("YearsSinceLastPromotion", min_value=0, max_value=15, value=1)

# feature department: category options
dept_options = ['Sales',
                'Human Resources',      
                'Research & Development',         
                ]

# feature salary: category options
salary_options = ["low", "medium", "high"]

# Allow the user to select a category
selected_dept = st.sidebar.selectbox("Selected departament:", dept_options)

# Allow the user to select a category
selected_salary = st.sidebar.selectbox("Selected salary", salary_options)

# Collect user inputs into a dictionary
user_input = {
    'Jobsatisfaction': Jobsatisfaction,
    'PerformanceRating': PerformanceRating,
    'WorkLifeBalance': WorkLifeBalance,
    'HourlyRate': HourlyRate,
    'TotalWorkingYears': TotalWorkingYears,
    'DistanceFromHome': DistanceFromHome,
    'YearsSinceLastPromotion': YearsSinceLastPromotion,
    'selected_dept': selected_dept,
    'selected_salary': selected_salary
}

st.sidebar.write(user_input)

# Convert user inputs into a format that the model expects
input_data = [Jobsatisfaction,
              PerformanceRating, 
              WorkLifeBalance, 
              HourlyRate, 
              TotalWorkingYears, 
              DistanceFromHome,
              YearsSinceLastPromotion,
              selected_dept,
              selected_salary
              ]

# Make predictions using the XgBoost model
prediction = xgb_clf.predict([input_data])[0]

# Display the prediction
st.subheader("Employees turnover: Stay or Left")

# add a color according with the result:
if prediction == 0:
    prediction = 'stay'
    background_color = "green" #background color based on the result
else:
    prediction = 'left'
    background_color = "red"

# Content to be centered
content_to_center = """
<div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
    <div style="text-align: center;">
        <h2>Your Content Goes Here</h2>
        <p>This is an example of a centered page in Streamlit.</p>
    </div>
</div>
"""

# Use st.markdown to apply HTML and CSS styling
styled_text = f"""
    <div style="text-align:center; padding:10px; background-color:{background_color};">
        <h2 style="color:white;">{prediction}</h2>
    </div>
    """

st.markdown(styled_text, unsafe_allow_html=True)