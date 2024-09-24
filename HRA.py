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
            EducationField = 1
        else :
            EducationField = 0          
  
        
        employeenumber = st.sidebar.slider('Number of people in the team', 1, 3000, 100)

        if employeenumber <1495 :
                employeenumber = 0
        else:
                employeenumber = 1
                
                       

        EnvironmentSatisfaction = st.selectbox('Environment Satisfaction',['Low', 'Medium','High','Very High'])
            
        if EnvironmentSatisfaction == "Low" :
                    EnvironmentSatisfaction = 1
        elif EnvironmentSatisfaction == "Medium":
                    EnvironmentSatisfaction = 2
        elif EnvironmentSatisfaction == "High":
                    EnvironmentSatisfaction = 3
        else :
                    EnvironmentSatisfaction = 4
            
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        
        if Gender == "Male" :
                Gender = 1
        else :
                Gender = 0

        Jobinvolvement = st.selectbox('Job Involvement',['Low', 'Medium','High','Very High'])
        
        if Jobinvolvement == "Low":
                    Jobinvolvement = 1
        elif Jobinvolvement == "Medium":
                    Jobinvolvement = 2
        elif Jobinvolvement == "High":
                    Jobinvolvement = 3
        else :
                    Jobinvolvement = 4
        
        JobRole = st.selectbox('Job Role', ['Research Director','Manager','Healthcare Representative','Manufacturing Director',
                                'Laboratory Technician','Research Scientist','Sales Executive','Human Resources',
                                'Sales Representative'])
        
        if JobRole == "Research Director" :
                    JobRole = 0
        elif JobRole == "Manager" or "Healthcare Representative" or "Manufacturing Director":
                    JobRole = 1
        elif JobRole == "Laboratory Technician" :
                    JobRole = 3
        elif JobRole == "Research Scientist" or "Sales Executive" :
                    JobRole = 2
        elif JobRole == "Human Resources" :
                    JobRole = 4
        else :
                    JobRole = 5
            
        JobSatisfaction = st.selectbox('Job Satisfaction', ['Low','Medium', 'High','Very High'])

        if JobSatisfaction == "Low" :
                    JobSatisfaction = 1
        elif JobSatisfaction == "Medium" or "High" :
                    JobSatisfaction = 2
        else :
                    JobSatisfaction = 3

        MaritalStatus = st.selectbox('Marital Status',['Married','Divorced','Single'])
            
        if MaritalStatus == "Married" or "Divorced" :
                    MaritalStatus = 0
        else :
                    MaritalStatus = 1

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

        StockOptionLevel = st.selectbox('Stock of employee in the company', ["No stocks", "Moderate stocks", 
                                "Lots of stocks"])
            
        if StockOptionLevel == "No stocks" :
                    StockOptionLevel = 0 
        elif StockOptionLevel == "Moderate stocks" :
                    StockOptionLevel = 1 
        else :
                    StockOptionLevel = 2

                 

        DistanceFromHome = st.sidebar.slider('Distance from home(km)', 0,50,5)
            
        PercentSalaryHike = st.number_input("Salary Hike %",0.,30.,step = 1.) 

        PerformanceRating = st.number_input(" Performance Rating",0.,4.,step = 1.) 

        TotalWorkingYears = st.number_input("Total experience of employee",0.,45.,step = 1.)

        YearsAtCompany = st.number_input("Number of years spent in company",0.,50., step = 1.)

        YearsInCurrentRole = st.number_input("Number of years in current role",0.,30., step = 1.)

        YearsSinceLastPromotion = st.number_input("Year Since Last Promotion",0.,20., step = 1.)

        YearsWithCurrManger = st.number_input("Years with current manager",0.,20., step = 1.)


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
                
        inp =[Age,Department,EducationField,employeenumber,EnvironmentSatisfaction,Gender,Jobinvolvement,JobRole,JobSatisfaction,
              MaritalStatus,MonthlyIncome,NumCompaniesWorked,OverTime,StockOptionLevel,DistanceFromHome,PercentSalaryHike,
              TotalWorkingYears,YearsAtCompany,PerformanceRating,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManger,WorkLifeBalance]

        return inp

        df= input_features()
        model = pickle.load(open('model.pkl','rb'))
        ans = model.predict_proba([df])[0][0]
        ans = round(100*ans,2)  
        st.subheader('The probability of employee being Left the Company is {ans} %.')
    
if __name__ == "__main__" : 
    main()
                    


