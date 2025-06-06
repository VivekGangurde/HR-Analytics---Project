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
        # Manual encoding
        input_data["BusinessTravel"] = {"Travel_Rarely": 0, "Travel_Frequently": 1, "Non-Travel": 2}[input_data["BusinessTravel"]]
        input_data["Department"] = {"Human Resources": 0, "Research & Development": 1, "Sales": 2}[input_data["Department"]]
        input_data["EducationField"] = {"Life Sciences": 0, "Medical": 1, "Marketing": 2, "Technical Degree": 3, "Human Resources": 4, "Other": 5}[input_data["EducationField"]]
        input_data["Gender"] = {"Male": 0, "Female": 1}[input_data["Gender"]]
        input_data["JobRole"] = {"Sales Executive": 0, "Research Scientist": 1, "Laboratory Technician": 2,
                                 "Manufacturing Director": 3, "Healthcare Representative": 4, "Manager": 5,
                                 "Sales Representative": 6, "Research Director": 7, "Human Resources": 8}[input_data["JobRole"]]
        input_data["MaritalStatus"] = {"Single": 0, "Married": 1, "Divorced": 2}[input_data["MaritalStatus"]]
        input_data["OverTime"] = {"No": 0, "Yes": 1}[input_data["OverTime"]]

        try:
            response = requests.post("https://hr-analytics-backend.onrender.com/predict", json=input_data)
            if response.status_code == 200:
                result = response.json()
                prediction = "Yes" if result["prediction"] == 1 else "No"
                probability = result["probability"] * 100
                st.success(f"Prediction: {prediction} — Probability: {probability:.2f}%")
            else:
                st.error("API returned an error.")
        except Exception as e:
            st.error(f"Error contacting API: {e}")
