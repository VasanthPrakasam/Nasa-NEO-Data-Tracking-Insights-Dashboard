# 🌌 NASA NEO Tracking & Insights Dashboard

<div align="center">

![NASA NEO Dashboard](https://img.shields.io/badge/NASA-NEO%20Tracker-blue?style=for-the-badge&logo=nasa)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-purple?style=for-the-badge&logo=plotly)

**🚀 Advanced Space Object Monitoring & Analysis**

*Explore asteroid data, approach speeds, distances, and hazard insights using SQL-powered queries*

[🎮 Live Demo](#-deployment-options) • [📖 Documentation](#-features) • [🛠️ Installation](#-installation) • [🤝 Contributing](#-contributing)

</div>

---

## 📊 Dashboard Overview

<div align="center">

| 🌑 **Total Asteroids** | 🚀 **Close Approaches** | ⚠️ **Potentially Hazardous** | 📊 **Hazard Rate** |
|:---:|:---:|:---:|:---:|
| Real-time count from database | Documented approach events | Risk assessment metrics | Statistical analysis |

</div>

This comprehensive **Near-Earth Object (NEO) tracking dashboard** transforms raw astronomical data into actionable insights, making complex space data accessible to researchers, educators, and space enthusiasts alike.

## 🎯 Core Purpose

The dashboard serves as an interactive tool for analyzing NASA's asteroid database, focusing on:

- 🌍 **Close approach events** to Earth and other celestial bodies
- ⚠️ **Hazard assessment** of potentially dangerous asteroids  
- 📈 **Statistical analysis** of asteroid characteristics and behavior patterns
- ⏰ **Temporal tracking** of asteroid movements over time

## ✨ Features

### 🏠 **Overview Metrics Dashboard**
Real-time statistics displayed at the top of the dashboard:

```
🌑 Total Asteroids Tracked    🚀 Close Approaches Recorded
⚠️ Potentially Hazardous      📊 Hazard Rate Percentage
```

### 🔍 **Categorized Query System**
20+ predefined queries organized into logical categories:

<details>
<summary>📈 <strong>Statistical Analysis</strong></summary>

- Approach frequency analysis per asteroid
- Average velocity calculations  
- Monthly approach distribution patterns
- Top 10 fastest asteroids identification

</details>

<details>
<summary>⚠️ <strong>Hazard Assessment</strong></summary>

- Identification of frequently approaching hazardous asteroids
- Comparative analysis between hazardous vs. non-hazardous objects
- Risk-based distance measurements
- Hazardous asteroid counting and classification

</details>

<details>
<summary>🏃‍♂️ <strong>Speed & Motion Analysis</strong></summary>

- Fastest recorded asteroid approaches
- High-velocity object identification (>50,000 km/h)
- Velocity distribution patterns
- Motion trend analysis

</details>

<details>
<summary>📏 <strong>Distance & Size Analysis</strong></summary>

- Closest approach records
- Size-based asteroid classification
- Proximity measurements in various units (AU, Lunar Distance, km)
- Diameter-based sorting and analysis

</details>

<details>
<summary>📅 <strong>Temporal Analysis</strong></summary>

- Time-based approach patterns
- Historical trend analysis
- Seasonal variation detection
- Monthly approach statistics

</details>

### 🎛️ **Advanced Interactive Filtering System**

Customize your asteroid search with multiple parameters:

| Filter Type | Description |
|-------------|-------------|
| 📅 **Date Filters** | Filter approaches by specific time periods |
| 🌍 **Distance Filters** | AU (Astronomical Units) and LD (Lunar Distance) |
| 🚀 **Velocity Filters** | Speed-based filtering in km/h |
| 📏 **Size Filters** | Diameter-based asteroid selection |
| ⚠️ **Hazard Classification** | Toggle between hazardous/non-hazardous objects |

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- SQLite database with asteroid data
- Internet connection for external dependencies

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/your-username/nasa-neo-dashboard.git
cd nasa-neo-dashboard

# Install required packages
pip install -r requirements.txt

# Run the application
streamlit run nasa_dashboard.py
```

### Requirements.txt
```txt
streamlit>=1.28.0
pandas>=1.3.0
sqlite3
plotly>=5.0.0
datetime
```

## 🚀 Deployment Options

### 1. **Local Development**
```bash
streamlit run nasa_dashboard.py
```

### 2. **Google Colab** 🔥
```python
# Get external IP (this will be your password)
!wget -q -O - ipv4.icanhazip.com

# Install required packages
!pip install streamlit plotly

# Launch the app
!streamlit run nasa_project.py & npx localtunnel --port 8501
```

**Steps:**
1. ✅ Enter `y` when prompted
2. 🔗 Copy the generated link (e.g., `https://fruity-aliens-unite.loca.lt/`)
3. 🌐 Open in browser
4. 🔑 Enter the IP address as password
5. 🎉 Access your dashboard!

### 3. **Streamlit Cloud**
- Fork this repository
- Connect to Streamlit Cloud
- Deploy with one click

### 4. **Docker**
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "nasa_dashboard.py"]
```

## 📚 Key Terminology

| Term | Definition |
|------|------------|
| **NEO** | Near-Earth Objects - asteroids/comets with orbits close to Earth |
| **AU** | Astronomical Unit - Earth-Sun distance (~150 million km) |
| **LD** | Lunar Distance - Earth-Moon distance (~384,400 km) |
| **PHA** | Potentially Hazardous Asteroid - objects >140m diameter approaching within 0.05 AU |
| **Magnitude (H)** | Asteroid brightness measure (lower = brighter/larger) |
| **Miss Distance** | Closest approach distance during flyby |

## 🎯 Use Cases

### 👨‍🔬 **For Researchers & Scientists**
- **Risk Assessment**: Identify potentially hazardous asteroids with frequent approaches
- **Pattern Recognition**: Discover seasonal or cyclical approach patterns  
- **Comparative Analysis**: Study differences between hazardous and non-hazardous objects
- **Historical Analysis**: Track asteroid behavior over time

### 👨‍🏫 **For Educators & Students**
- **Interactive Learning**: Explore real NASA data through user-friendly interface
- **Statistical Understanding**: Learn about asteroid distributions and characteristics
- **Visual Analytics**: See data patterns through automatically generated charts
- **Hands-on SQL**: Understand database queries through predefined examples

### 🌟 **For Space Enthusiasts**
- **Current Awareness**: Track recent and upcoming asteroid approaches
- **Size Comparisons**: Understand asteroid sizes and relative danger levels
- **Speed Analysis**: Discover fastest-moving objects in our solar system
- **Proximity Awareness**: Learn about objects passing closer than the Moon

## 🏗️ Technical Architecture

### Database Structure
```sql
-- Asteroids Table
asteroids (
    id, name, estimated_diameter_min_km, estimated_diameter_max_km,
    is_potentially_hazardous_asteroid, absolute_magnitude_h
)

-- Close Approach Table  
close_approach (
    neo_reference_id, close_approach_date, relative_velocity_kmph,
    miss_distance_km, miss_distance_lunar, astronomical, orbiting_body
)
```

### Enhanced Features
- 📊 **Automatic Chart Generation**: Creates relevant visualizations based on query results
- 🎨 **Interactive Plotly Charts**: Bar charts for counts, histograms for distributions
- ⚡ **Real-time Filtering**: Updates results instantly as filters change
- 📱 **Responsive Design**: Adapts to different screen sizes and devices

## 🎨 Visual Enhancements

- 🌈 **Gradient Backgrounds**: Modern, professional appearance
- 🎯 **Color-coded Sections**: Easy navigation and visual organization
- ⚡ **Interactive Elements**: Hover effects and responsive components
- 📋 **Categorized Sidebar**: Organized query selection for better UX
- 📊 **Statistical Summaries**: Quick insights from filtered results

## 📸 Screenshots

<div align="center">

### Main Dashboard
![Dashboard Overview](screenshot-placeholder-1.png)

### Query Categories
![Query System](screenshot-placeholder-2.png)

### Interactive Filters
![Filter System](screenshot-placeholder-3.png)

</div>

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

### Areas for Contribution
- 🐛 Bug fixes and improvements
- 📊 New visualization types
- 🔍 Additional query templates
- 📚 Documentation enhancements
- 🎨 UI/UX improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🏛️ **NASA** for providing comprehensive NEO data
- 🚀 **Streamlit** team for the amazing framework
- 📊 **Plotly** for interactive visualization capabilities
- 🌟 **Open Source Community** for continuous inspiration

## 📞 Contact

- 👤 **Author**: Vasanth P
- 📧 **Email**: i.vasanth.prakasam@gmail.com
- 🐙 **GitHub**: [@your-username]([https://github.com/VasanthPrakasam/])
- 💼 **LinkedIn**: [Your Profile]([https://www.linkedin.com/in/vasanth-prakasam-a490b0334/])

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ for space exploration and data science

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=your-username.nasa-neo-dashboard)

</div>
