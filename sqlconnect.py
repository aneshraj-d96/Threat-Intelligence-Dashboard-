import pandas as pd
import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",       # or your DB host
    user="root",
    password="root_",
    database="projects"
)

cursor = conn.cursor()

# Load CSV
df = pd.read_csv('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\Threat (cybersecurity)\\cleaned_threat_data.csv')

# Convert timestamp to datetime format (if needed)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS threat_data (
        threat_id INT PRIMARY KEY,
        timestamp DATETIME,
        source VARCHAR(255),
        threat_type VARCHAR(255),
        severity VARCHAR(50),
        ip_address VARCHAR(50),
        location VARCHAR(255),
        action_taken VARCHAR(255),
        response_time_sec INT
    )
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO threat_data (
            threat_id, timestamp, source, threat_type, severity,
            ip_address, location, action_taken, response_time_sec
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row['threat_id']),
        row['timestamp'].to_pydatetime() if pd.notnull(row['timestamp']) else None,
        row['source'],
        row['threat_type'],
        row['severity'],
        row['ip_address'],
        row['location'],
        row['action_taken'],
        int(row['response_time_sec'])
    ))

conn.commit()
print("Threat data imported successfully!")

