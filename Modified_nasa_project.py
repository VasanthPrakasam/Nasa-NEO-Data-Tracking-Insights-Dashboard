
import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd
from datetime import datetime

# Streamlit UI setup
st.set_page_config(layout='wide')

# Title and intro
st.title("🌌 NASA NEO Tracking & Insights Dashboard")
st.markdown("<h1 style='text-align: left; color: #FF5733; font-size: 35px; '> NASA NEO Tracking & Insights Dashboard  </h1>",unsafe_allow_html=True)
# Sidebar
st.sidebar.title("Menu")

# Top-Level Navigation
section = st.sidebar.radio("Select Section:", ["Home","CRUD Operations", "Filters", "📊 Queries"])
# Display Image Only on Home Page
if section == "Home":
  image = Image.open("/content/dh6w_sbm8_210607.jpg")
  st.image(image, caption="Welcome!", use_container_width=True)
  st.markdown("<h3 style='text-align: center; color: lightblue;'>Let's Explore the Features! Select an option from the sidebar to get started!</h3>", unsafe_allow_html=True)

# Connect to the database
conn = sqlite3.connect("Asteroid_Data.db")
cursor = conn.cursor()

# Helper function to run and display SQL queries
def show_query(query):
    df = pd.read_sql_query(query, conn)
    st.dataframe(df)

# CRUD Operations Section
if section == "CRUD Operations":
    st.sidebar.subheader("CRUD Operations")
    menu = ["View Asteroids", "View Close Approaches"]
    choice = st.sidebar.selectbox("Select Table", menu)

    if choice == "View Asteroids":
        st.subheader("View All Asteroids")
        query = "SELECT * FROM asteroids"
        show_query(query)
    elif choice == "View Close Approaches":
        st.subheader("View All Close Approaches")
        query = "SELECT * FROM close_approach"
        show_query(query)


# 🎛️ Main Filter Panel
if section == "Filters":
    with st.expander("🔧 Filter Settings", expanded=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            mag_range = st.slider("Absolute Magnitude (H)", 10.0, 35.0, (15.0, 30.0))
            au_range = st.slider("Astronomical Unit", 0.0, 1.5, (0.05, 1.0))
            hazardous_only = st.checkbox("☄️ Only Hazardous Asteroids")

        with col2:
            diam_range = st.slider("Estimated Diameter (km)", 0.0, 1.0, (0.01, 0.5))
            start_date = st.date_input("Start Date", datetime(2024, 1, 1))
            end_date = st.date_input("End Date", datetime(2024, 12, 31))

        with col3:
            vel_range = st.slider("Velocity (kmph)", 0.0, 150000.0, (10000.0, 50000.0))

    # SQL Filter Query
    filters = f'''
    SELECT a.name, a.absolute_magnitude_h, a.estimated_diameter_min_km,
           a.estimated_diameter_max_km, a.is_potentially_hazardous_asteroid,
           ca.close_approach_date, ca.relative_velocity_kmph,
           ca.astronomical, ca.miss_distance_km
    FROM asteroids a
    JOIN close_approach ca ON a.id = ca.neo_reference_id
    WHERE
        a.absolute_magnitude_h BETWEEN {mag_range[0]} AND {mag_range[1]} AND
        a.estimated_diameter_min_km >= {diam_range[0]} AND
        a.estimated_diameter_max_km <= {diam_range[1]} AND
        ca.relative_velocity_kmph BETWEEN {vel_range[0]} AND {vel_range[1]} AND
        ca.astronomical BETWEEN {au_range[0]} AND {au_range[1]} AND
        ca.close_approach_date BETWEEN "{start_date}" AND "{end_date}"
    '''
    if hazardous_only:
        filters += " AND a.is_potentially_hazardous_asteroid = 1"

    st.success("🔍 Showing Filtered Results")
    show_query(filters)

# Queries Section
if section == "📊 Queries":
    st.sidebar.header("📊 Queries")
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
    st.subheader(f"📌 Result: {query_option}")
    show_query(queries[query_option])


# Launch instructions for Colab
st.markdown("""
---
### 🔗 Thank you For Visting Us!
---
""")
