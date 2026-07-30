import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

# Load model
model = joblib.load("customer_churn_model.pkl")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict churn risk.")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure Months", 0, 100, 12)
phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total = st.number_input("Total Charges", min_value=0.0, value=1000.0)

# Prediction
if st.button("Predict Churn"):

    data = pd.DataFrame({
        "Gender": [gender],
        "Senior Citizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "Tenure Months": [tenure],
        "Phone Service": [phone],
        "Multiple Lines": [multiple],
        "Internet Service": [internet],
        "Online Security": [security],
        "Online Backup": [backup],
        "Device Protection": [device],
        "Tech Support": [tech],
        "Streaming TV": [tv],
        "Streaming Movies": [movies],
        "Contract": [contract],
        "Paperless Billing": [paperless],
        "Payment Method": [payment],
        "Monthly Charges": [monthly],
        "Total Charges": [total]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Low Risk of Churn\n\nProbability: {probability:.2%}")
