# ShopEase E-Commerce PVT. LTD.

### Sales & Profitability Data Analysis

**Author:** Aniket
**Date:** 09 September 2026

---

## About the Project

This is my first Data Analytics project, where I worked on an e-commerce sales dataset to understand sales, profit, discounts, product categories, regions, and other business-related patterns.

The main purpose of this project was to practice the complete data analysis process using Python and turn raw sales data into useful business insights.

## What I Wanted to Find

Through this project, I wanted to understand:

* How much total sales and profit the business generated
* Which categories and sub-categories performed the best
* Which regions generated the most sales and profit
* How discounts were related to profitability
* Which areas of the business were performing well or poorly
* What useful recommendations could be made from the data

## Dataset

The dataset contains **9,994 original sales records** with information such as:

* Ship Mode
* Segment
* Country
* City
* State
* Postal Code
* Region
* Category
* Sub-Category
* Sales
* Quantity
* Discount
* Profit

After cleaning and removing duplicate records, the dataset contained **9,977 records**.

## Tools I Used

* Python
* Pandas
* NumPy
* Matplotlib

## What I Did in the Project

I followed a complete data analysis workflow:

1. Loaded the CSV dataset using Pandas
2. Explored the dataset and checked its structure
3. Checked missing values and duplicate records
4. Cleaned the data
5. Calculated important business KPIs
6. Analysed sales, profit and quantity
7. Compared categories, sub-categories and regions
8. Analysed the relationship between discounts and profit
9. Created charts and visualizations using Matplotlib
10. Prepared a final business-oriented analysis report

## Some Results I Found

Some important results from my analysis were:

* **Total Sales:** $2,296,195.59
* **Total Profit:** $286,241.42
* **Total Quantity Sold:** 37,820
* **Average Discount:** 16%
* **Overall Profit Margin:** 12.47%

### Key observations

* Technology generated the highest sales and profit and also had a strong profit margin.
* Furniture had a much lower profit margin of around **2.49%**.
* The West region performed strongly compared with the other regions.
* The Central region had the lowest profit margin, around **7.92%**.
* Higher discount levels were generally associated with lower profitability.
* Discount groups of **30% or more** showed negative aggregate profit.
* Consumer had the highest sales and profit among the segments, while Home Office had the highest profit margin.

## What I Learned

This project helped me understand how different Python tools work together in a real data analysis workflow.

I learned how to:

* Work with real-world CSV data
* Clean and prepare data before analysis
* Use Pandas for data manipulation and grouping
* Use NumPy for numerical calculations
* Create meaningful visualizations using Matplotlib
* Calculate business KPIs
* Find patterns in data
* Convert analysis results into business insights
* Make recommendations based on data

## Business Recommendations

Based on my analysis:

* Discount strategies should be reviewed because higher discounts were associated with lower profitability.
* Low-margin categories such as Furniture should be analysed carefully to improve profitability.
* The business should continue focusing on strong-performing areas while investigating weaker regions and sub-categories.
* Discounts should be managed based on profitability rather than only increasing sales volume.

## Project Workflow

```text
Raw CSV Data
      ↓
Data Exploration
      ↓
Data Cleaning
      ↓
Data Analysis
      ↓
Business KPIs
      ↓
Advanced Analysis
      ↓
Data Visualization
      ↓
Business Insights & Recommendations
```

## Project Files

```text
ShopEase-Ecommerce-Analysis/
│
├── shopease_analysis.py
├── shopease_sales_data.csv
└── README.md
```

## Author

**Aniket**

This project is part of my journey toward becoming a job-ready Data Analyst.
