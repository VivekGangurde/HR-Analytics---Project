#!/usr/bin/env python
# coding: utf-8

# # HR Analytics

import numpy as np
import pandas as pd
import pickle
from pickle import dump
from pickle import load
import streamlit as st
import xgboost





def main():
    st.header('Employee Turnover Predicton')
    st.subheader('(Please fill in the Employee details accordingly)')
    def input_features() :
        st.sidebar.header('Sliders to change the variables.')
        Age = st.sidebar.slider('Age of employee', 18,65,30)
        
        
        Department = st.selectbox('Department', ['Human Resources', 'Research & Development','Sales',])
        if Department == "Human Resources" :
            Department = 1
        
        elif Department == "Research & Development" :
           Department = 2
           
        else :
            Department = 3
        
        DistanceFromHome = st.sidebar.slider('Distance from home(km)',0,50,5)
        
        EducationField = st.selectbox('Education Field',['Human Resources','Marketing','Technical Degree','Life Sciences','Medical', 'Other'])
        if EducationField == "Human Resources"  :
            EducationField = 1
            
        elif EducationField == "Life Sciences" :
           EducationField = 2
           
        elif EducationField == "Marketing" :
           EducationField = 3
        
        elif EducationField == "Medical" :
           EducationField = 4
           
        elif EducationField == "Other" :
            EducationField = 5
        
        else :
            EducationField = 6
        
        EmployeeNumber = st.sidebar.slider('Number of people in the team', 1, 3000, 100)
        if EmployeeNumber <1495 :
            EmployeeNumber = 0
        else:
            EmployeeNumber = 1
            
        EnvironmentSatisfaction = st.selectbox('Environment Satisfaction',['Low', 'Medium','High','Very High'])
        if EnvironmentSatisfaction == "Low" :
            EnvironmentSatisfaction = 1
        elif EnvironmentSatisfaction == "Medium":
            EnvironmentSatisfaction = 2
        elif EnvironmentSatisfaction == "High":
            EnvironmentSatisfaction = 3
        else :
            EnvironmentSatisfaction = 4
            
            
        JobLevel = st.selectbox('Job Level',['Low', 'Medium','High','Very High'])
        if JobLevel == "Low" :
            JobLevel = 1
        elif JobLevel == "Medium":
            JobLevel = 2
        elif JobLevel == "High":
            JobLevel = 3
        else :
            JobLevel = 4
         
        Education = st.selectbox('Job Level',['Low', 'Medium','High'])
        if Education == "Low" :
            Education = 1
        elif Education == "Medium":
            Education = 2
        elif Education == "High":
            Education = 3
        else :
            JobLevel = 4
            
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        if Gender == "Male" :
            Gender = 1
        else :
            Gender = 0
            
        JobInvolvement = st.selectbox('Job Involvement',['Low', 'Medium','High','Very High'])
        if JobInvolvement == "Low":
            JobInvolvement = 1
        elif JobInvolvement == "Medium":
            JobInvolvement = 2
        elif JobInvolvement == "High":
            JobInvolvement = 3
        else :
            JobInvolvement = 4
        

        JobRole = st.selectbox('Job Role', ['Research Director','Manager','Healthcare Representative','Manufacturing Director',
                                            'Laboratory Technician','Research Scientist','Sales Executive','Human Resources','Sales Representative'])
       
        if JobRole == "ResearHealthcare Representative" :
            JobRole = 1
        elif JobRole == "Human Resources" :
            JobRole = 2
        elif JobRole == "Laboratory Technician" :
            JobRole = 3
        elif JobRole == "Manager"  :
            JobRole = 4
        elif JobRole == "Manufacturing Director" :
            JobRole = 5
        elif JobRole == "Research Director" :
             JobRole = 6
        elif JobRole == "Research Scientist" :
              JobRole = 7
        elif JobRole == "Sales Executive" :
              JobRole = 8
        
        else :
            JobRole = 9
            
        JobSatisfaction = st.selectbox('Job Satisfaction', ['Low','Medium', 'High','Very High'])
        if JobSatisfaction == "Low" :
            JobSatisfaction = 1
        elif JobSatisfaction == "Medium" or "High" :
            JobSatisfaction = 2
        else :
            JobSatisfaction = 3
            
        MaritalStatus = st.selectbox('Marital Status',['Married','Divorced','Single'])
        if MaritalStatus == "Divorced"  :
            MaritalStatus = 1
        elif MaritalStatus == "Married" :
               MaritalStatus = 2
        else :
            MaritalStatus = 3
            
        MonthlyIncome = st.sidebar.slider('Monthly Income', 0, 50000, 5000)
        
        NumCompaniesWorked = st.number_input('Number of companies worked',0.,10.,step = 1.)
        if NumCompaniesWorked <=4 :
            NumCompaniesWorked = 0
        else :
            NumCompaniesWorked = 1
            
        OverTime = st.selectbox("Does the employee work overtime?",['No', 'Yes'])
        if OverTime == "No" :
            OverTime = 0
        else :
            OverTime = 1
            
        StockOptionLevel = st.selectbox('Stock of employee in the company', ["No stocks", "Moderate stocks", "Lots of stocks"])
        if StockOptionLevel == "No stocks" :
            StockOptionLevel = 0 
        elif StockOptionLevel == "Moderate stocks" :
            StockOptionLevel = 1 
        else :
            StockOptionLevel = 2
            
        TotalWorkingYears = st.number_input("Total experience of employee",0.,45.,step = 1.)
        
        TrainingTimesLastYear = st.number_input("Number of times employee did training",0.,9., step = 1.)
        
        YearsAtCompany = st.number_input("Number of years spent in company",0.,50., step = 1.)
        
        YearsSinceLastPromotion = st.number_input("Number of years Since Last Promotion",0.,20., step = 1.)
        
        PercentSalaryHike = st.number_input("Salary Hike %",0.,30., step = 1.)
        
        YearsInCurrentRole = st.number_input("Number of years in current role",0.,30., step = 1.)
        
        YearsWithCurrManager = st.number_input("Years with current manager",0.,20., step = 1.)
        if YearsWithCurrManager == 0 :
            YearsWithCurrManager = 0 
        elif YearsWithCurrManager < 12 :
            YearsWithCurrManager = 1
        else :
            YearsWithCurrManager = 2
            
        WorkLifeBalance = st.selectbox("WorkLifeBalance", ["Poor","Bad","Good", "Better", "Best"])
        if WorkLifeBalance == "Poor" :
            WorkLifeBalance = 1
        elif WorkLifeBalance == "Bad" :
            WorkLifeBalance = 2
        elif WorkLifeBalance == "Good" :
            WorkLifeBalance =3
        elif WorkLifeBalance == "Better":
            WorkLifeBalance = 4
        else :
            WorkLifeBalance = 5
            
        inp = ['Age','DistanceFromHome','Education','EmployeeNumber',
       'EnvironmentSatisfaction','Gender','JobInvolvement','JobLevel',
       'JobSatisfaction','MonthlyIncome','NumCompaniesWorked','OverTime',
       'PercentSalaryHike','StockOptionLevel','TotalWorkingYears',
       'TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany',
       'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager',
       'Department','EducationField','JobRole','MaritalStatus']
        
        return inp
    
    input_features = input_features()
    model = pickle.load(open('model.pkl','rb'))
    ans = model.predict_proba([df])[0][0]
    ans = round(100*ans,2)
    st.subheader('The probability of employee being Left the Company is {ans} %.')
    
if __name__ == "__main__" :
    main()
