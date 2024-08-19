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
        age = st.sidebar.slider('Age of employee', 18,65,30)
        
        dep = st.selectbox('Department', ['Sales', 'Human Resources', 'Research & Development'])
        if dep == "Sales" or "Human Resources" :
            dept = 0
        else :
            dept = 1
        
        distancefromhome = st.sidebar.slider('Distance from home(km)',0,50,5)
        
        efield = st.selectbox('Education Field',['Human Resources','Marketing','Technical Degree','Life Sciences','Medical', 'Other'])
        if efield == "Human Resources" or "Marketing" or "Technical Degree" :
            edu_field = 1
        else :
            edu_field = 0
        
        en = st.sidebar.slider('Number of people in the team', 1, 3000, 100)
        if en <1495 :
            employeenumber = 0
        else:
            employeenumber = 1
            
        envsat = st.selectbox('Environment Satisfaction',['Low', 'Medium','High','Very High'])
        if envsat == "Low" :
            env_sat = 1
        elif envsat == "Medium":
            env_sat = 2
        elif envsat == "High":
            env_sat = 3
        else :
            env_sat = 4
            
        gend = st.selectbox('Gender', ['Male', 'Female'])
        if gend == "Male" :
            gender = 1
        else :
            gender = 0
            
        involve = st.selectbox('Job Involvement',['Low', 'Medium','High','Very High'])
        if involve == "Low":
            job_inv = 1
        elif involve == "Medium":
            job_inv = 2
        elif involve == "High":
            job_inv = 3
        else :
            job_inv = 4
        
        role = st.selectbox('Job Role', ['Research Director','Manager','Healthcare Representative','Manufacturing Director','Laboratory Technician','Research Scientist','Sales Executive','Human Resources','Sales Representative'])
        if role == "Research Director" :
            jobrole = 0
        elif role == "Manager" or "Healthcare Representative" or "Manufacturing Director":
            jobrole = 1
        elif role == "Laboratory Technician" :
            jobrole = 3
        elif role == "Research Scientist" or "Sales Executive" :
            jobrole = 2
        elif role == "Human Resources" :
            jobrole = 4
        else :
            jobrole = 5
            
        jobsat = st.selectbox('Job Satisfaction', ['Low','Medium', 'High','Very High'])
        if jobsat == "Low" :
            job_sat = 1
        elif jobsat == "Medium" :
            job_sat = 2
        elif jobsat == "High":
            job_inv = 3
        else :
            job_sat = 4
            
        mar = st.selectbox('Marital Status',['Married','Divorced','Single'])
        if mar == "Married" or "Divorced" :
            mar_stat = 0
        else :
            mar_stat = 1
            
        income = st.sidebar.slider('Monthly Income', 0, 50000, 5000)
        
        num_worked = st.number_input('Number of companies worked',0.,10.,step = 1.)
        if num_worked <=4 :
            num_com = 0
        else :
            num_com = 1
            
        otime = st.selectbox("Does the employee work overtime?",['No', 'Yes'])
        if otime == "No" :
            overtime = 0
        else :
            overtime = 1
            
        sol = st.selectbox('Stock of employee in the company', ["No stocks", "Moderate stocks", "Lots of stocks"])
        if sol == "No stocks" :
            stocks = 0 
        elif sol == "Moderate stocks" :
            stocks = 1 
        else :
            stocks = 2
            
        total_exp = st.number_input("Total experience of employee",0.,45.,step = 1.)
        
        training = st.number_input("Number of times employee did training",0.,9., step = 1.)
        
        years_com = st.number_input("Number of years spent in company",0.,50., step = 1.)
        
        years_role = st.number_input("Number of years in current role",0.,30., step = 1.)
        
        ym = st.number_input("Years with current manager",0.,20., step = 1.)
        if ym == 0 :
            years_man = 0 
        elif ym < 12 :
            years_man = 1
        else :
            years_man = 2
            
        WLB = st.selectbox("WorkLifeBalance", ["Poor","Bad","Good", "Better", "Best"])
        if WLB == "Poor" :
            WLB_Score = 1
        elif WLB == "Bad" :
            WLB_Score = 2
        elif WLB == "Good" :
            WLB_Score =3
        elif WLB == "Better":
            WLB_Score = 4
        else :
            WLB_Score = 5
            
        inp = [age,dept,distancefromhome,edu_field, employeenumber,env_sat, gender,job_inv,jobrole,job_sat,mar_stat,income, num_com,overtime, stocks,total_exp,training,years_com,years_role,years_man,WLB_Score]
        
        return inp 
    df = input_features()
    model = pickle.load(open("test.pkl","rb"))
    ans = model.predict_proba(df)
    ans = round(100*ans,2)
    st.subheader('The probability of employee being Left the Company is {ans} %.')

if __name__ == "__main__" :
    main()
