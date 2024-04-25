#!/usr/bin/env python
# coding: utf-8

# # HR Analytics

import pandas as pd
import streamlit as st
import numpy as np
from xgboost import XGBClassifier
from pickle import dump
from pickle import load


# Load the saved model
model = xgb_classifier()
model = load(open("test.pkl", "rb"))
prediction = model.predict(df)


# Streamlit app title
st.title("Model Prediction App - Employee Turnover")

# Sidebar with input widgets
st.sidebar.header("User Input Features")

# Example input features (replace with your actual feature names)
satisfaction = st.sidebar.slider("satisfaction", min_value=0.0, max_value=1.0, value=0.01)
evaluation = st.sidebar.slider("evaluation", min_value=0.0, max_value=1.0, value=0.01)
projectCount = st.sidebar.slider("projectCount", min_value=1, max_value=7, value=1)
averageMonthlyHours = st.sidebar.slider("averageMonthlyHours", min_value=96, max_value=310, value=1)
yearsAtCompany = st.sidebar.slider("yearsAtCompany", min_value=2, max_value=10, value=1)
workAccident = st.sidebar.slider("workAccident", min_value=0, max_value=1, value=1)
promotion = st.sidebar.slider("promotion", min_value=0, max_value=1, value=1)

# feature department: category options
dept_options = ['sales',
                'technical',     
                'support',    
                'IT',      
                'product_mng',
                'marketing',  
                'RandD',         
                'accounting',    
                'hr',            
                'management'
                ]

# feature salary: category options
salary_options = ["low", "medium", "high"]

# Allow the user to select a category
selected_dept = st.sidebar.selectbox("Selected departament:", dept_options)

# Allow the user to select a category
selected_salary = st.sidebar.selectbox("Selected salary", salary_options)

# Collect user inputs into a dictionary
user_input = {
    'satisfaction': satisfaction,
    'evaluation': evaluation,
    'projectCount': projectCount,
    'averageMonthlyHours': averageMonthlyHours,
    'yearsAtCompany': yearsAtCompany,
    'workAccident': workAccident,
    'promotion': promotion,
    'selected_dept': selected_dept,
    'selected_salary': selected_salary
}

st.sidebar.write(user_input)

# Convert user inputs into a format that the model expects
input_data = [satisfaction,
              evaluation, 
              projectCount, 
              averageMonthlyHours, 
              yearsAtCompany, 
              workAccident,
              promotion,
              selected_dept,
              selected_salary
              ]

# Make predictions using the CatBoost model
prediction = cat_model.predict([input_data])[0]

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

