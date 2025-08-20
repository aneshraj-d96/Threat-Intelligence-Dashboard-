# app.py
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\Threat (cybersecurity)\\threat_severity_model.pkl')

st.title("Threat Intelligence Dashboard")
st.subheader("Predict Critical Threats")

# Inputs
response_time = st.slider("Response Time (sec)", 1, 600, 60)
source = st.selectbox("Source", ["Firewall", "IDS", "SIEM", "Endpoint", "Threat Feed"])
threat_type = st.selectbox("Threat Type", ["Malware", "Phishing", "DDoS", "Ransomware", "SQL Injection", "Zero-Day"])
action_taken = st.selectbox("Action Taken", ["Blocked", "Quarantined", "Escalated", "Ignored"])

# Prepare input
input_dict = {
    "response_time_sec": response_time,
    f"source_{source}": 1,
    f"threat_type_{threat_type}": 1,
    f"action_taken_{action_taken}": 1
}

# Fill missing columns
model_features = model.feature_names_in_
input_df = pd.DataFrame([{col: input_dict.get(col, 0) for col in model_features}])

# Predict
if st.button("Predict Threat Severity"):
    prediction = model.predict(input_df)[0]
    result = "Critical" if prediction == 1 else "Non-Critical"
    st.success(f" Predicted Severity: {result}")


