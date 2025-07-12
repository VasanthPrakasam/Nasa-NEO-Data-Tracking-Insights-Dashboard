
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Streamlit UI setup
st.set_page_config(layout='wide')

# Title and intro
st.title("🌌 NASA NEO Tracking & Insights Dashboard")
st.markdown("""
Explore asteroid data, approach speeds, distances, and hazard insights using SQL-powered queries.
""")

# Connect to the database
conn = sqlite3.connect("Asteroid_Data.db")
cursor = conn.cursor()

# Helper function to run and display SQL queries
def show_query(query):
    df = pd.read_sql_query(query, conn)
    st.dataframe(df)

# Sidebar filters
st.sidebar.header("📊 Query & Filters")
query_option = st.sidebar.selectbox("Select a Query", [
    "1. Count asteroid approaches",
    "2. Average velocity per asteroid",
    "3. Top 10 fastest asteroids",
    "4. Hazardous asteroids > 3 approaches",
    "5. Month with most approaches",
    "6. Fastest ever approach",
    "7. Sort by max estimated diameter",
    "8. Closest approach getting nearer over time",
    "9. Closest approach date & distance",
    "10. Velocity > 50,000 km/h",
    "11. Approaches per month",
    "12. Brightest asteroid (lowest magnitude)",
    "13. Hazardous vs Non-hazardous count",
    "14. Asteroids < 1 LD",
    "15. Asteroids < 0.05 AU",
    "Bonus 1: Orbiting bodies (non-Earth)",
    "Bonus 2: Avg miss distance by hazard type",
    "Bonus 3: Top 5 closest approaches",
    "Bonus 4: Count of hazardous asteroids",
    "Bonus 5: Frequent <1 LD asteroids"
])

# All Queries defined here -- Chatgpt suggestions i don't know what it means
queries = {
    "1. Count asteroid approaches": '''
        SELECT neo_reference_id, COUNT(*) AS approach_count
        FROM close_approach
        GROUP BY neo_reference_id
        ORDER BY approach_count DESC
    ''',
    "2. Average velocity per asteroid": '''
        SELECT neo_reference_id, AVG(relative_velocity_kmph) AS avg_velocity
        FROM close_approach
        GROUP BY neo_reference_id
        ORDER BY avg_velocity DESC
    ''',
    "3. Top 10 fastest asteroids": '''
        SELECT neo_reference_id, MAX(relative_velocity_kmph) AS max_velocity
        FROM close_approach
        GROUP BY neo_reference_id
        ORDER BY max_velocity DESC
        LIMIT 10
    ''',
    "4. Hazardous asteroids > 3 approaches": '''
        SELECT ca.neo_reference_id, COUNT(*) AS approach_count
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        WHERE a.is_potentially_hazardous_asteroid = 1
        GROUP BY ca.neo_reference_id
        HAVING COUNT(*) > 3
    ''',
    "5. Month with most approaches": '''
        SELECT strftime('%Y-%m', close_approach_date) AS month, COUNT(*) AS count
        FROM close_approach
        GROUP BY month
        ORDER BY count DESC
        LIMIT 1
    ''',
    "6. Fastest ever approach": '''
        SELECT neo_reference_id, MAX(relative_velocity_kmph) AS fastest_speed
        FROM close_approach
        ORDER BY fastest_speed DESC
        LIMIT 1
    ''',
    "7. Sort by max estimated diameter": '''
        SELECT id, name, estimated_diameter_max_km
        FROM asteroids
        ORDER BY estimated_diameter_max_km DESC
    ''',
    "8. Closest approach getting nearer over time": '''
        SELECT *
        FROM close_approach
        ORDER BY neo_reference_id, close_approach_date
    ''',
    "9. Closest approach date & distance": '''
        SELECT a.name, ca.close_approach_date, MIN(ca.miss_distance_km) AS closest_approach
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        GROUP BY a.id
        ORDER BY closest_approach ASC
    ''',
    "10. Velocity > 50,000 km/h": '''
        SELECT DISTINCT a.name, ca.relative_velocity_kmph
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        WHERE ca.relative_velocity_kmph > 50000
    ''',
    "11. Approaches per month": '''
        SELECT strftime('%Y-%m', close_approach_date) AS month, COUNT(*) AS total
        FROM close_approach
        GROUP BY month
        ORDER BY total DESC
    ''',
    "12. Brightest asteroid (lowest magnitude)": '''
        SELECT id, name, absolute_magnitude_h
        FROM asteroids
        ORDER BY absolute_magnitude_h ASC
        LIMIT 1
    ''',
    "13. Hazardous vs Non-hazardous count": '''
        SELECT is_potentially_hazardous_asteroid, COUNT(*) AS count
        FROM asteroids
        GROUP BY is_potentially_hazardous_asteroid
    ''',
    "14. Asteroids < 1 LD": '''
        SELECT a.name, ca.close_approach_date, ca.miss_distance_lunar
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        WHERE ca.miss_distance_lunar < 1
        ORDER BY ca.miss_distance_lunar
    ''',
    "15. Asteroids < 0.05 AU": '''
        SELECT a.name, ca.close_approach_date, ca.astronomical
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        WHERE ca.astronomical < 0.05
        ORDER BY ca.astronomical
    ''',
    "Bonus 1: Orbiting bodies (non-Earth)": '''
        SELECT orbiting_body, COUNT(*) AS count
        FROM close_approach
        WHERE orbiting_body != 'Earth'
        GROUP BY orbiting_body
        ORDER BY count DESC
    ''',
    "Bonus 2: Avg miss distance by hazard type": '''
        SELECT a.is_potentially_hazardous_asteroid, AVG(ca.miss_distance_km) AS avg_miss_distance
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        GROUP BY a.is_potentially_hazardous_asteroid
    ''',
    "Bonus 3: Top 5 closest approaches": '''
        SELECT a.name, ca.close_approach_date, ca.miss_distance_km
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        ORDER BY ca.miss_distance_km ASC
        LIMIT 5
    ''',
    "Bonus 4: Count of hazardous asteroids": '''
        SELECT COUNT(DISTINCT id) AS hazardous_asteroid_count
        FROM asteroids
        WHERE is_potentially_hazardous_asteroid = 1
    ''',
    "Bonus 5: Frequent <1 LD asteroids": '''
        SELECT ca.neo_reference_id, a.name, COUNT(*) AS close_pass_count
        FROM close_approach ca
        JOIN asteroids a ON ca.neo_reference_id = a.id
        WHERE ca.miss_distance_lunar < 1
        GROUP BY ca.neo_reference_id
        HAVING COUNT(*) > 1
        ORDER BY close_pass_count DESC
    '''
}

# Run selected query
st.subheader(query_option)
show_query(queries[query_option])

# 🔍 Advanced Filters Section
st.header("📌 Filter Asteroid Approaches")

# User input widgets
selected_date = st.date_input("Select Close Approach Date (after)", datetime(2000, 1, 1))
min_au = st.slider("Minimum Astronomical Units (AU)", 0.0, 1.0, 0.0, 0.01)
max_au = st.slider("Maximum Astronomical Units (AU)", 0.0, 1.0, 0.05, 0.01)
min_ld = st.slider("Minimum Lunar Distance (LD)", 0.0, 100.0, 0.0, 1.0)
max_ld = st.slider("Maximum Lunar Distance (LD)", 0.0, 100.0, 10.0, 1.0)
min_velocity = st.slider("Minimum Relative Velocity (km/h)", 0.0, 100000.0, 0.0, 1000.0)
max_velocity = st.slider("Maximum Relative Velocity (km/h)", 0.0, 100000.0, 50000.0, 1000.0)
min_diameter = st.slider("Minimum Estimated Diameter (km)", 0.0, 50.0, 0.0, 0.1)
max_diameter = st.slider("Maximum Estimated Diameter (km)", 0.0, 50.0, 5.0, 0.1)
hazardous = st.selectbox("Hazardous?", ["Both", "Yes", "No"])

# Filter query
filter_query = f'''
SELECT a.name, ca.close_approach_date, ca.relative_velocity_kmph, ca.miss_distance_km, ca.miss_distance_lunar,
       a.estimated_diameter_min_km, a.estimated_diameter_max_km, a.is_potentially_hazardous_asteroid
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
WHERE date(ca.close_approach_date) >= date('{selected_date}')
  AND ca.miss_distance_km BETWEEN {min_au} AND {max_au}
  AND ca.miss_distance_lunar BETWEEN {min_ld} AND {max_ld}
  AND ca.relative_velocity_kmph BETWEEN {min_velocity} AND {max_velocity}
  AND a.estimated_diameter_max_km BETWEEN {min_diameter} AND {max_diameter}
'''
if hazardous == "Yes":
    filter_query += " AND a.is_potentially_hazardous_asteroid = 1"
elif hazardous == "No":
    filter_query += " AND a.is_potentially_hazardous_asteroid = 0"

st.subheader("Filtered Results")
show_query(filter_query)

# Launch instructions for Colab
st.markdown("""
---
### 🔗 Launch from Google Colab
python
!wget -q -O - ipv4.icanhazip.com   # this command will generate a password for you (copy that)
!streamlit run nasa_project.py & npx localtunnel --port 8501

Then when prompted:
- Enter y to proceed
- A link like https://fruity-aliens-unite.loca.lt/ will be generated
- Paste it in your browser
- It will ask for a password (paste the one copied earlier)
- You’ll be redirected to your Streamlit app ✅
---
""")
