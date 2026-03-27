import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.set_page_config(page_title="Respiratory Monitor", page_icon="🫁")

st.title("🫁 AI Respiratory Health Monitoring System")
st.markdown("### Enter Patient Details")


co2 = st.slider("CO2 Level (ppm)", 400, 3000)
spo2 = st.slider("SpO2 (%)", 80, 100)
breath = st.slider("Breathing Rate", 10, 30)

st.markdown("### 📊 Patient Data Visualization")

import pandas as pd

data = pd.DataFrame({
    "Parameter": ["CO2", "SpO2", "Breathing"],
    "Value": [co2, spo2, breath]
})

st.bar_chart(data.set_index("Parameter"))

if st.button("Check Condition"):
    result = model.predict([[co2, spo2, breath]])

    st.markdown("## Result:")
    
    if result[0] == "Critical":
        st.error("🚨 Critical Condition! Seek medical help immediately.")
    elif result[0] == "Moderate":
        st.warning("⚠️ Moderate Risk. Monitor patient closely.")
    else:
        st.success("✅ Normal Condition. Patient is stable.")