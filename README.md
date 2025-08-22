# 🛡️ Threat Intelligence Dashboard

A full-stack analytics solution designed to monitor, analyze, and respond to cybersecurity threats across global networks. This project processes over **200,000+ threat logs** to uncover patterns in attack types, severity levels, response actions, and geographic distribution—empowering SOC teams with predictive insights and real-time dashboards.

---

## 🚗 GitHub Repository  
🔗 [Threat-Intelligence-Dashboard](https://github.com/aneshraj-d96/Threat-Intelligence-Dashboard-)

---

## 🧠 Project Overview

Cybersecurity operations demand rapid, data-driven decision-making. This project delivers an end-to-end threat intelligence platform that enables:

- 📊 Real-time visibility into global threat activity  
- 🔍 Predictive modeling for severity classification  
- 📍 Location-based threat mapping  
- 📈 Response time optimization and SOC performance tracking  

---

## 🎯 Key Objectives

- Clean and preprocess multi-source threat logs  
- Engineer features for severity modeling and dashboarding  
- Build classification models to predict threat severity  
- Deploy interactive dashboards for SOC and executive teams  

---

## 📁 Project Structure

| File Name                          | Description                                                       |
|-----------------------------------|-------------------------------------------------------------------|
| `threat_data.csv`                 | Raw dataset with 200K+ threat logs                                |
| `cleaned_threat_data.csv`         | Preprocessed dataset with engineered features                     |
| `threat_severity_model.pkl`       | Trained model for predicting threat severity                      |
| `threat_intelligence.sql`         | SQL queries for filtering and aggregating threat data             |
| `sqlconnect.py`                   | Python script for SQL database connection                         |
| `app.py`                          | Streamlit app for dashboard deployment                            |
| `Threat Intelligence.ipynb`       | Jupyter notebook with EDA, modeling, and insights                 |
| `Threat Intelligence Dashboard.pbix` | Power BI report visualizing threat trends and severity         |

---

## 🧹 Data Preprocessing

- Converted `timestamp` to datetime format  
- Extracted time-based features (`hour`, `day`, `month`)  
- Encoded categorical variables (`source`, `threat_type`, `severity`, `location`, `action_taken`)  
- Removed duplicates and handled missing values  
- Normalized `response_time_sec` for modeling  

---

## 📈 Exploratory Data Analysis

- 🌍 Threat type distribution across global locations  
- 🔥 Severity trends by source and attack type  
- ⏱️ Response time analysis by action taken  
- 🧠 Correlation between threat severity and response strategy  
- 🕒 Time-of-day impact on threat frequency  

---

## 🤖 Modeling Approach

- **Target Variable**: `severity`  
- **Algorithms Used**: Random Forest, Logistic Regression  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score  
- **Top Features**: `response_time_sec`, `threat_type`, `source`, `location`, `action_taken`  

---

## 📊 Dashboard Overview

### 🟢 Streamlit Dashboard  
Interactive dashboard for SOC teams and analysts:

- 🌍 Location-wise threat distribution  
- 🧨 Threat type and severity analysis  
- ⏱️ Response time trends by action  
- 🔐 Predictive insights on threat severity  

![Streamlit Preview](https://image2url.com/images/1755861692729-707e352e-950e-447c-8d17-363b4a29c2ac.png)  
![Streamlit Preview](https://image2url.com/images/1755861741278-3347be40-d57a-4333-a33b-8dcc9630dfcb.png)

---

### 🔷 Power BI Dashboard  
Executive-level reporting for strategic planning:

- 📊 Severity heatmaps by region  
- 📍 Threat volume by source and type  
- ⏱️ Response time benchmarking  
- 📅 Monthly threat trends and escalation metrics  

---

## 🚀 Deployment

- Model serialized using `joblib` as `threat_severity_model.pkl`  
- Dashboard deployed via **Streamlit Cloud**  
- SQL integration for dynamic threat filtering  
- Power BI report created for SOC and executive teams  

---

## 🧠 Business Impact

- Improves threat visibility across geographies  
- Reduces response time through severity prediction  
- Enables proactive defense strategies  
- Supports SOC and executive decision-making with real-time analytics  

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
 
🔗 [GitHub Profile](https://github.com/aneshraj-d96)
