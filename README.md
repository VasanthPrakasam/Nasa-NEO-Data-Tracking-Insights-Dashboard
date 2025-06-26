🚀 NASA Near-Earth Object (NEO) Tracking & Insights using Public API
A data science project that collects and analyzes Near-Earth Object asteroid data from NASA’s public API. It transforms raw astronomical data into structured insights using Python, SQL, and Streamlit for real-time dashboard interaction.

📌 Project Overview
This project focuses on:

Tracking asteroid close approaches to Earth

Analyzing impact threats based on size, velocity, and distance

Providing researchers and learners with a user-friendly dashboard to filter and view asteroid patterns

🧠 Skills Gained
REST API Integration and Pagination Handling

JSON Parsing & Structuring

Data Cleaning and Transformation

SQL Table Design and Querying

Interactive Streamlit Dashboard Development

Filtering astronomical data in real-time

🌍 Domain: Space Research & Astroinformatics
A project powered by NASA’s trusted API, useful for educators, astronomers, data scientists, and policy analysts in evaluating asteroid threat levels and orbital behaviors.

🔧 Step-by-Step Project Approach
✅ Step 1: Get NASA API Key
Registered on https://api.nasa.gov to receive a personal API key.

Constructed the API URL using:

bash
Copy
Edit
https://api.nasa.gov/neo/rest/v1/feed?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&api_key=YOUR_KEY
✅ Step 2: Data Extraction (Python + API)
Looping through NASA's paginated API using the next link.

Fetched 10,000 asteroid records in 7-day chunks.

Extracted key fields:

id, name, close_approach_date, relative_velocity_kmph, miss_distance_km, etc.

✅ Step 3: Data Cleaning & Preparation
Used Python to clean and format data:

Converted strings to proper data types (e.g., float, date).

Used .get() to handle missing/null fields.

Stored cleaned data in two lists: asteroids_data, close_approach_data

✅ Step 4: SQL Database Creation & Insertion
Used SQLite for ease of deployment in Colab.

Created 2 tables:

asteroids (general asteroid properties)

close_approach (event-specific data like distance, velocity)

Inserted cleaned JSON data into these SQL tables using parameterized INSERT statements.

✅ Step 5: Write Analytical SQL Queries
Implemented 15+ SQL queries to derive real-time scientific insights:

Top 10 fastest asteroids

Most frequent asteroid visits

Potentially hazardous asteroids with >3 approaches

Closest approaches by lunar distance / AU

Velocity > 50,000 km/h

Monthly asteroid approach trends

✅ Step 6: Build Streamlit UI Dashboard
Created sidebar with a selectbox() for query selection

Used sliders, date pickers, and dropdowns to filter:

Distance (AU/LD), Diameter, Speed, Hazardous State

Results are shown as live-updated tables from SQL database

📊 Sample Query Outputs
Query Example	Output Description
Top 10 Fastest Asteroids	Based on maximum relative_velocity_kmph
Asteroids with miss_distance_lunar < 1	Detected all asteroids that passed closer than the Moon
Hazardous Asteroids	Filtered True/False on hazard flag
Closest Approach Dates	Ordered results to show narrowing trajectory

📁 Folder Structure (Recommended)
bash
Copy
Edit
├── nasa_neo.db                     # SQLite Database
├── NASA_NEO_API_Extraction.ipynb  # Colab Notebook for Data Extraction
├── Streamlit_UI.py                # Streamlit Dashboard File
├── README.md                      # Project Summary
└── requirements.txt               # Libraries used (streamlit, pandas, sqlite3)
🛠 Tech Stack Used
Tool	Purpose
Python	API requests, data parsing, DB connection
SQLite	Lightweight relational database
SQL	Querying insights from structured tables
Streamlit	Interactive dashboard interface
NASA Open API	Data source

🎯 Business Use Cases
Asteroid Threat Monitoring – by size, speed, and approach frequency

Educational Resource – for learning SQL, APIs, and dashboards

Real-time Filtering – for space analysts to narrow down NEO threats

🧩 Key Learnings
Handling real-world API pagination

Transforming JSON into normalized relational structure

Writing advanced SQL queries for scientific insights

Streamlit UI helps non-programmers explore complex space data

📎 References
NASA API Docs: https://api.nasa.gov

Streamlit Docs: https://docs.streamlit.io

SQLite Tutorial: https://www.sqlitetutorial.net

✅ Created By: Vasanth Prakasam
🔍 Verified By: Nilofer Mubeen
📊 Approved By: Shadiya, Nehlath Harmain
