#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import requests

st.title("HR Analytics App")
st.header("Enter Employee Data")

# Collect all required inputs
input_data = {
    "Age": st.number_input("Age", min_value=18, max_value=60),
    "BusinessTravel": st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]),
    "DailyRate": st.number_input("Daily Rate", min_value=100, max_value=1500),
    "Department": st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"]),
    "DistanceFromHome": st.number_input("Distance From Home", min_value=1, max_value=30),
    "Education": st.selectbox("Education Level", [1, 2, 3, 4, 5]),
    "EducationField": st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"]),
    "EnvironmentSatisfaction": st.selectbox("Environment Satisfaction", [1, 2, 3, 4]),
    "Gender": st.selectbox("Gender", ["Male", "Female"]),
    "HourlyRate": st.number_input("Hourly Rate", min_value=20, max_value=100),
    "JobInvolvement": st.selectbox("Job Involvement", [1, 2, 3, 4]),
    "JobLevel": st.slider("Job Level", 1, 5),
    "JobRole": st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"]),
    "JobSatisfaction": st.slider("Job Satisfaction", 0.0, 1.0),
    "MaritalStatus": st.selectbox("Marital Status", ["Single", "Married", "Divorced"]),
    "MonthlyIncome": st.number_input("Monthly Income", min_value=1000.0),
    "MonthlyRate": st.number_input("Monthly Rate", min_value=1000),
    "NumCompaniesWorked": st.number_input("Number of Companies Worked", min_value=0),
    "OverTime": st.selectbox("OverTime", ["Yes", "No"]),
    "PercentSalaryHike": st.number_input("Percent Salary Hike", min_value=0),
    "PerformanceRating": st.slider("Performance Rating", 0.0, 1.0),
    "RelationshipSatisfaction": st.selectbox("Relationship Satisfaction", [1, 2, 3, 4]),
    "TotalWorkingYears": st.number_input("Total Working Years", min_value=0),
    "TrainingTimesLastYear": st.number_input("Training Times Last Year", min_value=0),
    "WorkLifeBalance": st.selectbox("Work Life Balance", [1, 2, 3, 4]),
    "YearsAtCompany": st.number_input("Years at Company", min_value=0),
    "YearsInCurrentRole": st.number_input("Years in Current Role", min_value=0),
    "YearsSinceLastPromotion": st.number_input("Years Since Last Promotion", min_value=0),
    "YearsWithCurrManager": st.number_input("Years With Current Manager", min_value=0)
}

if st.button("Predict"):
    with st.spinner("Predicting..."):
        try:
            API_URL = "https://hr-backend.onrender.com/predict"  # Change this to your actual backend URL on Render
           response = requests.post("https://hr-backend.onrender.com/predict", json=input_data)
            
            if response.status_code == 200:
                result = response.json()
                prediction = "Yes" if result["prediction"] == 1 else "No"
                probability = result["probability"] * 100
                st.success(f"Prediction: {prediction} — Probability: {probability:.2f}%")
            else:
                st.error("API returned an error.")
        except Exception as e:
            st.error(f"Error contacting API: {e}")
