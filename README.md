# 🏡 User Housing Preferences Analysis Project  
### Azura PowerPI

A complete end-to-end Azure data engineering project analyzing Airbnb housing patterns using a modern **Medallion Architecture** and delivering insights through a fully interactive **Power BI dashboard**.

---

## 🚀 Tools and Technology

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Data Ingestion** | Azure Data Factory (ADF) | Pipeline Orchestration |
| **Data Storage** | Azure Data Lake Storage Gen2 | Bronze / Silver / Gold Layers |
| **Data Processing** | Azure Databricks (PySpark) | Cleaning, Transformation, Aggregation |
| **Data Visualization** | Microsoft Power BI | Dashboard & Analytics |

---

# 🏗️ Technical Architecture

This project follows a structured **Bronze → Silver → Gold** pipeline implemented on Microsoft Azure.  
Data was first collected through **web scraping** from Airbnb, then refined and visualized.

---

# 🥉 1. Bronze Layer — Raw Data Collection

- Raw Airbnb data was collected via **web scraping**.  
- Data included: listings, hosts, pricing, location metadata, availability calendars.  
- Ingested into Azure Data Lake Storage Gen2 using **Azure Data Factory**.  
- Stored exactly as received (no cleaning or transformation).

**🎯 Goal:** Preserve original source data.

---

# 🥈 2. Silver Layer — Data Cleaning & Standardization

Using **Azure Databricks + PySpark**, raw data was transformed into a clean dataset.

### Actions:
- Remove duplicates  
- Handle missing/invalid values  
- Standardize column names  
- Normalize schema  
- Join related datasets (listings, host details, pricing, etc.)  
- Enforce consistency across all tables  

**🎯 Goal:** Produce analytics-ready data.

---

# 🥇 3. Gold Layer — Curated Dataset for Power BI

Final modeling layer optimized for Power BI.

### Includes:
- Aggregated metrics (avg. price, occupancy rate, monthly reviews)  
- Host performance metrics  
- Location-based insights  
- Star-schema optimized tables  

**🎯 Goal:** Provide clean, structured data for dashboards & analysis.

---

# 📊 Airbnb Data Analytics Dashboard

An interactive dashboard to explore Airbnb market data across cities.

---

## 🌍 1. Geographic Distribution of Listings
- Map visualizing listing locations  
- Marker **size & color** reflect price  
- Helps identify high-cost and low-cost zones  

---

## 💲 2. Price Distribution Analysis
A histogram showing:
- The price range of listings  
- Common pricing tiers  
- Market outliers  

---

## 🏘️ 3. Property Type Market Composition
Visual breakdown of property categories:
- Entire homes  
- Private rooms  
- Shared spaces  
- Apartments, studios, etc.  

---

## 📈 4. Guest Booking Activity
Box plot showing:
- Monthly reviews as a booking activity indicator  
- Typical engagement levels  
- Outlier listings with high customer activity  

---

## ⚡ 5. Quick Market Summary
Provides a snapshot of selected city insights:

- **Average nightly price**  
- **Average monthly reviews**  
- **Market activity level**  

_Example_:  
Albany has an average price of **$111** and ~**2 reviews/month** → **Moderate activity**.

---

## 🤖 6. Personalized AI Recommendation
AI tool that generates hosting advice based on:
- Age  
- Gender  
- Hosting experience  

Helps users make smarter hosting decisions.

---

# 👥 Authors

- **Omar Farag**  
- **Bassem Ahmed**  
- **Rana Ehab**  
- **Mohamed Mosad**

