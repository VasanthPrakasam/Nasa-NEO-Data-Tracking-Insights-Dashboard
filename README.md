🚀 STREAMLIT UI DASHBOARD – 
COMPLETE WORKFLOW EXPLANATION
✅ 1. Set Up & Imports
At the beginning of your Streamlit file (.py or notebook cell):

python
Copy
Edit
import streamlit as st
import sqlite3
import pandas as pd
streamlit: for creating the web UI

sqlite3: to connect with the local SQL database

pandas: to display query results as tables and manage dataframes

✅ 2. Page Setup & Aesthetic
python
Copy
Edit
st.set_page_config(page_title="NASA NEO Dashboard", layout="wide")
st.title("🌌 NASA NEO Tracking & Insights Dashboard")
st.caption("Explore asteroid data, approach speeds, distances, and hazard insights using SQL-powered queries.")
Sets the title, layout, and purpose of the dashboard

layout="wide" gives the UI more horizontal space for filters and tables

✅ 3. Database Connection
python
Copy
Edit
conn = sqlite3.connect('nasa_neo.db')
cursor = conn.cursor()
Establishes a live connection to your local SQLite database

All queries are executed through this connection

✅ 4. Dropdown to Select SQL Query
In the sidebar:

python
Copy
Edit
st.sidebar.header("🧮 Query & Filters")
query_option = st.sidebar.selectbox("Select a Query", list(queries.keys()))
Uses selectbox() to allow users to choose from 15+ predefined analytical queries

queries is a Python dictionary with SQL query strings as values

Based on the selection, the corresponding SQL query runs

Example queries dictionary:

python
Copy
Edit
queries = {
    "1. Count asteroid approaches": "SELECT name, COUNT(*) AS total_approaches FROM close_approach JOIN asteroids ON close_approach.neo_reference_id = asteroids.id GROUP BY name ORDER BY total_approaches DESC",
    "2. Top 10 fastest asteroids": "SELECT name, MAX(relative_velocity_kmph) AS top_speed FROM close_approach JOIN asteroids ON close_approach.neo_reference_id = asteroids.id GROUP BY name ORDER BY top_speed DESC LIMIT 10",
    ...
}
✅ 5. Query Execution & Result Display
python
Copy
Edit
def show_query(sql_query):
    df = pd.read_sql_query(sql_query, conn)
    st.dataframe(df)
Executes the SQL using pandas.read_sql_query

Displays results using st.dataframe() (which is scrollable, sortable)

Then:

python
Copy
Edit
show_query(queries[query_option])
Dynamically executes and displays results for the selected query

✅ 6. Dynamic Filter Panel (Very Important Section)
Below the predefined query section, you built a custom filter area to interactively filter asteroids:

python
Copy
Edit
st.subheader("📌 Filter Asteroid Approaches")
Then added Streamlit widgets:

📆 Date Filter:
python
Copy
Edit
selected_date = st.date_input("Select Close Approach Date (after)", value=datetime.date(2000, 1, 1))
📏 Distance & Speed Sliders:
python
Copy
Edit
min_au = st.slider("Minimum Astronomical Units (AU)", 0.00, 1.00, 0.00)
max_au = st.slider("Maximum Astronomical Units (AU)", 0.00, 1.00, 1.00)

min_ld = st.slider("Minimum Lunar Distance (LD)", 0.00, 100.00, 0.00)
max_ld = st.slider("Maximum Lunar Distance (LD)", 0.00, 100.00, 100.00)

min_velocity = st.slider("Minimum Relative Velocity (km/h)", 0.00, 100000.00, 0.00)
max_velocity = st.slider("Maximum Relative Velocity (km/h)", 0.00, 100000.00, 100000.00)
⚠️ Hazardous Filter:
python
Copy
Edit
hazard_filter = st.selectbox("Potentially Hazardous?", ["Both", "True", "False"])
✅ 7. Filtered Query Generation
You dynamically generated a SQL query based on all filter values:

python
Copy
Edit
filter_query = f"""
SELECT a.name, c.close_approach_date, c.relative_velocity_kmph, 
       c.astronomical, c.miss_distance_km, c.miss_distance_lunar, 
       a.estimated_diameter_max_km, a.is_potentially_hazardous_asteroid 
FROM close_approach c
JOIN asteroids a ON c.neo_reference_id = a.id
WHERE c.close_approach_date >= '{selected_date}'
  AND c.astronomical BETWEEN {min_au} AND {max_au}
  AND c.miss_distance_lunar BETWEEN {min_ld} AND {max_ld}
  AND c.relative_velocity_kmph BETWEEN {min_velocity} AND {max_velocity}
"""

if hazard_filter != "Both":
    filter_query += f" AND a.is_potentially_hazardous_asteroid = {hazard_filter}"
The SQL query is automatically modified based on user inputs

Final result is displayed using show_query(filter_query)

✅ 8. Final Table Output
python
Copy
Edit
st.markdown("### Filtered Results")
show_query(filter_query)
The result reflects only asteroids that satisfy the selected filters

Automatically updates when the user modifies any filter slider/dropdown

🌟 Additional Touches You May Have Used
Used icons and emojis to make UI engaging (e.g., 🌌, 📌, 🚀)

Used st.columns() to align filters in side-by-side layout (helps save space)

May have used st.markdown() with custom HTML/CSS for headings
