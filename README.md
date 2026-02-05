Customer Churn Prediction System
🔍 Project Overview

This project predicts whether a customer is likely to churn (leave the service) using Machine Learning.
A Streamlit web application is used for user-friendly prediction.

🎯 Objective
To help businesses identify customers who are at risk of leaving and take preventive actions.

🛠 Technologies Used
*Python
*Pandas, NumPy
*Scikit-learn
*Streamlit
*Pickle
*GitHub

📊 Dataset
Telecom customer dataset containing:
Senior Citizen
Tenure
Monthly Charges
Total Charges
Contract, Services, Dependents, etc.
Categorical variables were converted using One-Hot Encoding.

🤖 Machine Learning Model
Algorithm used: Logistic Regression
Data was scaled using StandardScaler
Model, scaler, and feature names were saved using pickle

Saved files:
model.pkl
scaler.pkl
features.pkl

🚀 Streamlit Web App
The Streamlit app:
Takes customer inputs
Creates a full feature dataframe using saved feature names
Fills missing categorical features with 0
Applies the same scaler used during training
Predicts customer churn
This avoids feature mismatch errors during deployment.

⚠️ Key Challenge Faced
Feature mismatch error during prediction
Resolved by:
Loading features.pkl
Creating an empty dataframe with all trained features
Filling numeric inputs
Setting remaining features to zero

▶️ How to Run the App
pip install streamlit scikit-learn pandas numpy
streamlit run app.py

✅ Output

Displays whether the customer will churn or not
Clean UI with success/warning messages

👩‍💻 Developed by

Lalithya Shashidhar
BCA – Data Science Project
