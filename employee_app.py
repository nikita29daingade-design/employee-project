# Import Required Libraries

import streamlit as st
import pandas as pd
import joblib

# Load Models

salary_model = joblib.load("salary_model.pkl")
promotion_model = joblib.load("promotion_model.pkl")

# Title

st.title("Employee Salary Prediction and Promotion Classification System")

st.write("Enter Employee Details")

# User Inputs

age = st.number_input("Age", 18, 60, 25)

gender = st.selectbox("Gender", ["Male", "Female"])

education = st.selectbox(
    "Education",
    ["Bachelor", "Master", "PhD"]
)

experience = st.number_input("Experience", 0, 30, 2)

department = st.selectbox(
    "Department",
    ["IT", "HR", "Finance", "Sales", "Marketing"]
)

jobrole = st.selectbox(
    "Job Role",
    [
        "Developer",
        "Software Engineer",
        "Team Lead",
        "HR Executive",
        "Recruiter",
        "HR Manager",
        "Analyst",
        "Senior Analyst",
        "Finance Manager",
        "Sales Executive",
        "Sales Manager",
        "Marketing Executive",
        "Marketing Manager"
    ]
)

city = st.selectbox(
    "City",
    ["Pune", "Mumbai", "Nagpur", "Nashik", "Aurangabad"]
)

performance = st.slider("Performance Score", 60, 100, 80)

# Prediction Button

if st.button("Predict"):

    input_data = pd.DataFrame({

        "Age":[age],
        "Gender":[gender],
        "Education":[education],
        "Experience":[experience],
        "Department":[department],
        "JobRole":[jobrole],
        "City":[city],
        "PerformanceScore":[performance]

    })

    salary = salary_model.predict(input_data)

    promotion = promotion_model.predict(input_data)

    st.success(f"Predicted Salary : ₹ {salary[0]:,.0f}")

    st.success(f"Promotion Status : {promotion[0]}")