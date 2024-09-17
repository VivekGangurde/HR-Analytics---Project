#!/usr/bin/env python
# coding: utf-8

# In[287]:


#!/usr/bin/env python
# coding: utf-8

# In[94]:


#!/usr/bin/env python
# coding: utf-8

# # HR Analytics

import numpy as np
import pandas as pd
import pickle
from pickle import dump
from pickle import load
import streamlit as st
import sklearn as skl
import xgboost
from sklearn.linear_model import LogisticRegression






def main():
    st.header('Employee Turnover Predicton')
    st.subheader('(Please fill in the Employee details accordingly)')

def input_features() :
        st.sidebar.header('Sliders to change the variables.')
        Age= st.sidebar.slider('Age of employee', 18,65,30)

        Department = st.selectbox('Department', ['Sales', 'Human Resources', 'Research & Development'])
        
        if Department == "Sales" or "Human Resources" :
                            Department = 0
        else :
                            Department = 1

        
        EducationField = st.selectbox('Education Field',['Human Resources','Marketing','Technical Degree',
                        'Life Sciences','Medical', 'Other'])
        if EducationField == "Human Resources" or "Marketing" or "Technical Degree" :
                edu_field = 1
        else :
                edu_field = 0          
  
        
        employeenumber = st.sidebar.slider('Number of people in the team', 1, 3000, 100)

        if employeenumber <1495 :
                employeenumber = 0
        else:
                employeenumber = 1
                
                       

        EnvironmentSatisfaction = st.selectbox('Environment Satisfaction',['Low', 'Medium','High','Very High'])
            
        if EnvironmentSatisfaction == "Low" :
                    env_sat = 1
        elif EnvironmentSatisfaction == "Medium":
                    env_sat = 2
        elif EnvironmentSatisfaction == "High":
                    env_sat = 3
        else :
                    env_sat = 4
            
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        
        if Gender == "Male" :
                gender = 1
        else :
                gender = 0

        Jobinvolvement = st.selectbox('Job Involvement',['Low', 'Medium','High','Very High'])
        
        if Jobinvolvement == "Low":
                    job_inv = 1
        elif Jobinvolvement == "Medium":
                    job_inv = 2
        elif Jobinvolvement == "High":
                    job_inv = 3
        else :
                    job_inv = 4
        
        JobRole = st.selectbox('Job Role', ['Research Director','Manager','Healthcare Representative','Manufacturing Director',
                                'Laboratory Technician','Research Scientist','Sales Executive','Human Resources',
                                'Sales Representative'])
        
        if JobRole == "Research Director" :
                    jobrole = 0
        elif JobRole == "Manager" or "Healthcare Representative" or "Manufacturing Director":
                    jobrole = 1
        elif JobRole == "Laboratory Technician" :
                    jobrole = 3
        elif JobRole == "Research Scientist" or "Sales Executive" :
                    jobrole = 2
        elif JobRole == "Human Resources" :
                    jobrole = 4
        else :
                    jobrole = 5
            
        JobSatisfaction = st.selectbox('Job Satisfaction', ['Low','Medium', 'High','Very High'])

        if JobSatisfaction == "Low" :
                    job_sat = 1
        elif JobSatisfaction == "Medium" or "High" :
                    job_sat = 2
        else :
                    job_sat = 3

        MaritalStatus = st.selectbox('Marital Status',['Married','Divorced','Single'])
            
        if MaritalStatus == "Married" or "Divorced" :
                    mar_stat = 0
        else :
                    mar_stat = 1

        MonthlyIncome = st.sidebar.slider('Monthly Income', 0, 50000, 5000)
            

        NumCompaniesWorked = st.number_input('Number of companies worked',0.,10.,step = 1.)
        
        if NumCompaniesWorked <=4 :
                    num_com = 0
        else :
                    num_com = 1

        OverTime = st.selectbox("Does the employee work overtime?",['No', 'Yes'])
            
        if OverTime == "No" :
                    overtime = 0
        else :
                    overtime = 1

        StockOptionLevel = st.selectbox('Stock of employee in the company', ["No stocks", "Moderate stocks", 
                                "Lots of stocks"])
            
        if StockOptionLevel == "No stocks" :
                    stocks = 0 
        elif StockOptionLevel == "Moderate stocks" :
                    stocks = 1 
        else :
                    stocks = 2

        BusinessTravel = st.selectbox('Buisness Travel Status', ["Non-Travel", "Travel Frequently", "Travel Rarely"])
        
        if BusinessTravel == "Non-Travel" :
                    Travel = 0 
        elif BusinessTravel == "Travel Frequently" :
                    Travel = 1 
        else :
                    Travel = 2          

        DistanceFromHome = st.sidebar.slider('Distance from home(km)', 0,50,5)
            
        PercentSalaryHike = st.number_input("Salary Hike %",0.,30.,step = 1.) 

        PerformanceRating = st.number_input(" Performance Rating",0.,4.,step = 1.) 

        RelationshipSatisfaction = st.number_input(" Relation Satisfaction",0.,5.,step = 1.) 

        Education = st.number_input("Education Level",0.,5.,step = 1.) 

        JobLevel = st.number_input("Job Level",0.,5.,step = 1.)

        TotalWorkingYears = st.number_input("Total experience of employee",0.,45.,step = 1.)

        TrainingTimesLastYear = st.number_input("Number of times employee did training",0.,9., step = 1.)

        YearsAtCompany = st.number_input("Number of years spent in company",0.,50., step = 1.)

        YearsInCurrentRole = st.number_input("Number of years in current role",0.,30., step = 1.)

        YearsSinceLastPromotion = st.number_input("Year Since Last Promotion",0.,20., step = 1.)

        DailyRate = st.number_input("Daily Rate of work",0.,1600., step = 1.)

        MonthlyRate = st.number_input("Monthly Rate of work",0.,40000., step = 1.)

        HourlyRate = st.number_input("Hourly Rate of employee",0.,200., step = 1.)

        YearsWithCurrManger = st.number_input("Years with current manager",0.,20., step = 1.)


        WorkLifeBalance = st.selectbox("WorkLifeBalance", ["Poor","Bad","Good", "Better", "Best"])
            
        if WorkLifeBalance == "Poor" :
                    WLB_Score = 1
        elif WorkLifeBalance == "Bad" :
                    WLB_Score = 2
        elif WorkLifeBalance == "Good" :
                    WLB_Score =3
        elif WorkLifeBalance == "Better":
                    WLB_Score = 4
        else :
                    WLB_Score = 5
                
        inp =[Age,DailyRate,DistanceFromHome,Education,employeenumber,EnvironmentSatisfaction,
                    Gender,HourlyRate,Jobinvolvement,JoblLevel,JobSatisfaction,MonthlyIncome,MonthlyRate,
                    NumCompaniesWorked,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,
                    StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,
                    YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManger,BusinessTravel_Non-Travel,
                    BusinessTravel_Travel_Frequently,BusinessTravel_Travel_Rarely,Department_HumanResources,
                    Deparment_Reseearch & Development,Department_Sales,EducationField_HumanResources,
                    Educationfield_LifeSciences,Educationfield_Marketing,EducationField_Medical,EducationField_Other,
                    EducationField_TechnicalDegree,JobRole_HealthcareRepresentative,JobRole_HumanResources,
                    JobRole_LaboratoryTechnician,JobRole_Manager,JobRole_ManufacturingDirector,JobRole_ResearchDirector,
                    JobRole_ResearchScientist,JobRole_SalesExecutive,JobRole_SalesRepresentative,MaritalStatus_Divorced,
                    MaritalStatus_Married,MaritalStatus_Single]

        return inp

        df= input_features()
        model = pickle.load(open('test.pkl','rb'))
        ans = model.predict_proba([df])[0][0]
        ans = round(100*ans,2)  
        st.subheader('The probability of employee being Left the Company is {ans} %.')
    
if __name__ == "__main__" : 
    main()
                    


