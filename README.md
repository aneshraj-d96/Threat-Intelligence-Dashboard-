# 🛡️ Threat Intelligence Dashboard

An interactive analytics platform designed to monitor, analyze, and respond to cybersecurity threats across global networks. This project processes 200K+ threat logs to uncover patterns in attack types, severity levels, response actions, and geographic distribution.

---

## 🧠 Project Overview

Cybersecurity teams rely on real-time insights to mitigate risks and respond effectively. This dashboard analyzes threat intelligence data to identify attack trends, optimize response strategies, and visualize threat severity across geographies.

### 🔍 Key Objectives
- Clean and preprocess threat log data  
- Analyze threat types, severity, and response times  
- Build predictive models for severity classification  
- Deploy interactive dashboard and Power BI visuals for SOC teams  

---

## 📁 Project Structure

| File Name                    | Description                                                       |
|-----------------------------|-------------------------------------------------------------------|
| `threat_data.csv`           | Raw dataset with 200K+ threat logs                                |
| `cleaned_threat_data.csv`   | Preprocessed dataset with engineered features                     |
| `threat_severity_model.pkl` | Trained model for predicting threat severity                      |
| `threat_intelligence.sql`   | SQL queries for filtering and aggregating threat data             |
| `sqlconnect.py`             | Python script for SQL database connection                         |
| `app.py`                    | Streamlit app for dashboard deployment                            |
| `Threat Intelligence.ipynb` | Jupyter notebook with EDA, modeling, and insights                 |
| `Threat Intelligence Dashboard.pbix` | Power BI report visualizing threat trends and severity         |

---

## 🧹 Data Preprocessing

- Converted `timestamp` to datetime format  
- Extracted time-based features (hour, day, month)  
- Encoded categorical variables (`source`, `threat_type`, `severity`, `location`, `action_taken`)  
- Removed duplicates and handled missing values  
- Normalized `response_time_sec` for modeling  

---

## 📈 Exploratory Data Analysis

- Threat type distribution across global locations  
- Severity trends by source and attack type  
- Response time analysis by action taken  
- Correlation between threat severity and response strategy  
- Time-of-day impact on threat frequency  

---

## 🤖 Modeling Approach

- **Target Variable**: `severity`  
- **Algorithms Used**: Random Forest, Logistic Regression  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score  
- **Feature Importance**: `response_time_sec`, `threat_type`, `source`, `location`, `action_taken`  

---

## 📊 Dashboard Overview

Built using **Streamlit**, the dashboard includes:

- 🌍 Location-wise threat distribution  
- 🧨 Threat type and severity analysis  
- ⏱️ Response time trends by action  
- 🔐 Predictive insights on threat severity  
- 📊 Power BI visuals for executive reporting  

> _Add your hosted dashboard screenshot or link here once available._

---

## 🚀 Deployment

- Model serialized with `joblib` as `threat_severity_model.pkl`  
- Dashboard deployed via **Streamlit Cloud**  
- SQL integration for dynamic threat filtering  
- Power BI report created for SOC and executive teams  

---

## 🧠 Business Impact

- Enhances threat visibility across geographies  
- Improves response time and prioritization  
- Supports SOC decision-making with predictive insights  
- Enables proactive defense strategies through data-driven intelligence  

---

## 🛠️ Tech Stack

- **Python**: Pandas, NumPy, Scikit-learn, Streamlit  
- **SQL**: Data extraction and filtering  
- **Visualization**: Matplotlib, Seaborn, Power BI  
- **Deployment**: Streamlit Cloud, GitHub  
- **Presentation**: Power BI Dashboard (.pbix)  

---

## 📌 Future Enhancements

- Integrate real-time threat feed ingestion  
- Add NLP-based classification for threat descriptions  
- Enable geospatial heatmaps of attack origins  
- Expand dashboard to include SOC alerting and escalation metrics  

---

## 👤 Author

**Anesh Raj**  
Data Analyst | Data Scientist | Business Analyst  
Focused on multi-industry impact through predictive modeling and dashboarding.  
📍 Chennai, India
