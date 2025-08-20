-- #1: Average Response Time by Severity Level
SELECT 
    severity,
    ROUND(AVG(response_time_sec), 2) AS avg_response_time_sec,
    COUNT(*) AS total_threats
FROM threat_data
GROUP BY severity
ORDER BY avg_response_time_sec DESC;

-- #2: Top 5 Locations with Most Threats
SELECT 
    location,
    COUNT(*) AS threat_count
FROM threat_data
GROUP BY location
ORDER BY threat_count DESC
LIMIT 5;

-- #3: Threat Type Distribution
SELECT 
    threat_type,
    COUNT(*) AS occurrences
FROM threat_data
GROUP BY threat_type
ORDER BY occurrences DESC;

-- #4: Monthly Trend of Threats
SELECT 
    DATE_FORMAT(timestamp, '%Y-%m') AS month,
    COUNT(*) AS threat_count
FROM threat_data
GROUP BY month
ORDER BY month;

-- #5: High Severity Threats with Long Response Times
SELECT 
    threat_id,
    timestamp,
    source,
    response_time_sec
FROM threat_data
WHERE severity = 'High' AND response_time_sec > 300
ORDER BY response_time_sec DESC;

-- #6: Effectiveness of Actions Taken
SELECT 
    action_taken,
    COUNT(*) AS total_actions,
    ROUND(AVG(response_time_sec), 2) AS avg_response_time
FROM threat_data
GROUP BY action_taken
ORDER BY avg_response_time;

