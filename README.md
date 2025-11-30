User Housing Preferences Analysis Project
Azura PowerPI
Tools and Technology
Layer / Purpose	Technology Used
Data Ingestion	Azure Data Factory (ADF)
Data Storage	Azure Data Lake Storage Gen2
Data Processing	Azure Databricks (PySpark)
Data Visualization	Microsoft Power BI
Technical Architecture

This project follows a modern Medallion Data Architecture (Bronze → Silver → Gold) implemented entirely on Microsoft Azure.

We first collected Airbnb housing data through web scraping, then processed it using a structured data pipeline.

1. Bronze Layer — Raw Data Collection

In this stage:

Raw Airbnb data was scraped from the website.

Data included listings, host profiles, pricing, location metadata, and availability calendars.

Azure Data Factory (ADF) pipelines ingested this data.

Data was stored exactly as collected in Azure Data Lake Storage Gen2.

No transformations, cleaning, or validations were applied.

Purpose: Store untouched raw data from the source.

2. Silver Layer — Data Cleaning & Standardization

In the Silver layer we used Azure Databricks (PySpark) to process and clean the previously scraped Airbnb data.

Key cleaning and transformation actions:

Removing duplicates

Handling missing or invalid values

Standardizing column names

Normalizing schema formats

Joining related datasets (listings, hosts, reviews, pricing, etc.)

Enforcing dataset consistency

Purpose: Create a reliable and analytics-ready dataset.

3. Gold Layer — Curated Dataset for Analytics

The Gold layer contains the final refined dataset used for Power BI dashboards.

Transformations included:

Creating aggregated metrics (average price, occupancy rate, review activity)

Generating city-level and location-based insights

Structuring tables optimized for Power BI models

Preparing curated data marts for analysis

Purpose: Provide clean, structured, analysis-ready data for visualization and reporting.

Airbnb Data Analytics Dashboard

An interactive Power BI dashboard that analyzes Airbnb markets across different cities.
Users can select a city and explore:

Pricing trends

Listing availability

Market composition

Geographic distribution

Guest engagement metrics

Personalized AI-powered recommendations

Designed for hosts, analysts, and decision-makers to quickly understand market behavior.

Dashboard Features
1. Geographic Distribution of Listings

Interactive map of listings showing:

Location

Pricing (reflected by marker size and color)

2. Price Distribution Analysis

Histogram visualizing nightly price ranges:

Identifies common pricing tiers

Highlights market outliers

3. Property Type Market Composition

Pie or bar chart showing:

Apartments

Houses

Shared rooms

Studios

Other property types

Gives insight into market supply structure.

4. Guest Booking Activity

Box plot illustrating:

Monthly review frequency per listing

Typical engagement level

Outliers with unusually high activity

Used as a proxy for booking demand.

5. Quick Market Summary

A fast overview of the selected city’s Airbnb market:

Average nightly price

Average monthly reviews

Market activity level

Example:
Albany’s average price ≈ $111, with ~2 reviews per month, showing moderate guest activity.

6. Personalized AI Recommendation

A user-input tool that generates hosting recommendations based on:

Age

Gender

Hosting experience

Helps guide new or existing hosts with AI-powered insights.

Authors

Omar Farag

Bassem Ahmed

Rana Ehab

Mohamed Mosad
