import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details to predict heart disease risk")

# Load model trained on YOUR dataset
model = joblib.load("heart_disease_nb.pkl")

# INPUTS — MATCH DATASET
age = st.number_input("Age", min_value=1, max_value=120, value=30)

bp_level = st.selectbox(
    "Blood Pressure Level",
    [0, 1, 2],
    format_func=lambda x: {0: "Low", 1: "Normal", 2: "High"}[x]
)

cholesterol = st.selectbox(
    "Cholesterol",
    [0, 1],
    format_func=lambda x: {0: "Normal", 1: "High"}[x]
)

glucose = st.number_input(
    "Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, bp_level, cholesterol, glucose]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Heart Diseas Detected")
    else:
        st.success("✅ No Heart Disease Detected")