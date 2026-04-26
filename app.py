import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.title("Sleep Quality Prediction App")

st.markdown("""
This app predicts sleep quality using coffee intake, caffeine consumption,
lifestyle, and health indicators. The model is intended for prediction only,
not causal or medical diagnosis.
""")

st.sidebar.header("User Inputs")

age = st.sidebar.slider("Age", min_value=18, max_value=80, value=30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
country = st.sidebar.selectbox("Country", ["USA", "UK", "Canada", "Australia", "Germany", "France", "India", "China", "Japan", "Brazil"])
coffee_intake = st.sidebar.slider("Coffee Intake (cups/day)", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
caffeine_mg = st.sidebar.slider("Caffeine Intake (mg/day)", min_value=0, max_value=800, value=180)
sleep_hours = st.sidebar.slider("Sleep Hours", min_value=3.0, max_value=12.0, value=7.0, step=0.5)
bmi = st.sidebar.slider("BMI", min_value=15.0, max_value=45.0, value=24.0, step=0.1)
heart_rate = st.sidebar.slider("Heart Rate", min_value=45, max_value=130, value=72)
stress_level = st.sidebar.selectbox("Stress Level", ["Low", "Medium", "High"])
physical_activity = st.sidebar.slider("Physical Activity Hours", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
health_issues = st.sidebar.selectbox("Health Issues", ["None", "Diabetes", "Hypertension", "Heart Disease", "Other"])
occupation = st.sidebar.selectbox("Occupation", ["Student", "Office Worker", "Healthcare", "Education", "Service", "Other"])
smoking = st.sidebar.selectbox("Smoking", ["Yes", "No"])
alcohol = st.sidebar.selectbox("Alcohol Consumption", ["Yes", "No"])

model = joblib.load("model.pkl")

input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Country": [country],
    "Coffee_Intake": [coffee_intake],
    "Caffeine_mg": [caffeine_mg],
    "Sleep_Hours": [sleep_hours],
    "BMI": [bmi],
    "Heart_Rate": [heart_rate],
    "Stress_Level": [stress_level],
    "Physical_Activity_Hours": [physical_activity],
    "Health_Issues": [health_issues],
    "Occupation": [occupation],
    "Smoking": [smoking],
    "Alcohol_Consumption": [alcohol]
})

prediction = model.predict(input_data)[0]
prediction_proba = model.predict_proba(input_data)[0]
classes = model.named_steps["model"].classes_

st.subheader("Prediction Result")
st.metric("Predicted Sleep Quality", prediction)

confidence = prediction_proba.max()
st.metric("Model Confidence", f"{confidence:.1%}")

st.markdown("""
The confidence score is the model's predicted probability for the selected class.
It should be interpreted as model uncertainty, not medical certainty.
""")

proba_df = pd.DataFrame({
    "Sleep Quality": classes,
    "Predicted Probability": prediction_proba
})

st.subheader("Predicted Probability by Sleep Quality Class")

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(proba_df["Sleep Quality"], proba_df["Predicted Probability"])
ax.set_ylabel("Predicted Probability")
ax.set_ylim(0, 1)
ax.set_title("Model Prediction Probabilities")

st.pyplot(fig)

st.subheader("Input Summary")
st.dataframe(input_data)
