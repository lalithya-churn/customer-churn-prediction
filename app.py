import streamlit as st
import pandas as pd
import pickle

# ==============================
# Load saved objects
# ==============================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

# ==============================
# Define numerical columns
# (same as training)
# ==============================
numerical_cols = [
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="Customer Churn Prediction")

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict churn")

# User Inputs
senior = st.selectbox("Senior Citizen (0 = No, 1 = Yes)", [0, 1])
tenure = st.number_input("Tenure (Months)", 0, 72, 1)
monthly = st.number_input("Monthly Charges", 0.0, value=50.0)
total = st.number_input("Total Charges", 0.0, value=50.0)

# ==============================
# Prediction
# ==============================
if st.button("Predict Churn"):

    # 1️⃣ Create empty dataframe with ALL trained features
    input_df = pd.DataFrame(0, index=[0], columns=features)

    # 2️⃣ Fill only numerical values from user
    input_df["SeniorCitizen"] = senior
    input_df["tenure"] = tenure
    input_df["MonthlyCharges"] = monthly
    input_df["TotalCharges"] = total

    # 3️⃣ Scale ONLY numerical columns
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

    # 4️⃣ Predict
    prediction = model.predict(input_df)[0]

    # 5️⃣ Show result
    if prediction == 1:
        st.error("❌ Customer is likely to churn")
    else:
        st.success("✅ Customer is not likely to churn")
