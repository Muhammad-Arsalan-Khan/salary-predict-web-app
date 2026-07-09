import streamlit as st
import pandas as pd
import pickle

# ---- Page setup ----
st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")
st.title("💰 Salary Prediction Web App")
st.write("Enter your work experience and education level to get a salary prediction.")

# ---- Model load karein (ek dafa cache ho jayega) ----
@st.cache_resource
def load_model():
    with open('salary_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# ---- User inputs ----
experience = st.number_input(
    "Years of Experience",
    min_value=0.0, max_value=50.0, value=1.0, step=0.5
)

education = st.selectbox(
    "Education Level",
    options=["Bachelor's", "Master's", "PhD"]
)

education_map = {"Bachelor's": 1, "Master's": 2, "PhD": 3}

# ---- Predict button ----
if st.button("Predict Salary"):
    input_data = pd.DataFrame({
        "Years of Experience": [experience],
        "Education Level": [education_map[education]]
    })
    predicted_salary = model.predict(input_data)[0]

    st.success(f"Predicted Salary: **${predicted_salary:,.2f}**")

st.divider()
st.caption("Model: Linear Regression | Features: Experience, Education Level")
