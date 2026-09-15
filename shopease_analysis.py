# ============================================================================
# PROJECT 1 – ShopEase E-commerce PVT. LTD.
# ============================================================================
# Description: Sales & Profitability Data Analysis 
# Author: Aniket
# Date: 09 September 2026
# Dataset: shopease_sales_data.csv
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)

print("="*70)
print("                  📊 ShopEase E-commerce PVT. LTD.")
print("="*70)

# --------------------------------------
# Phase 1 – Business Understanding
# --------------------------------------
try:
    data = pd.read_csv("shopease_sales_data.csv")
except FileNotFoundError:
    print("\n❌ Error: 'shopease_sales_data.csv' not found!")
    print("Please check the file path and try again.")
    exit(1)
# Inspect the dataset
print(f"\n📌 Rows          : {data.shape[0]:,}")
print(f"📌 Columns       : {data.shape[1]}")
print(f"📌 Memory Usage  : {data.memory_usage(deep=True).sum() / 1024:.2f} KB")  # memory usage of dataset

print("📌 Column Name & Data Type:")
print(f"{'Column Name':<25} {'Data Type':<15}")
print("-"*50)
for col in data.columns:
    print(f"{col:<25} {str(data[col].dtype):<15}")

print("\n📌 Missing Values Summary:")  # Total number of missing values
print(data.isnull().sum())

print("\n📌 First 10 Rows of the Dataset:")
print(data.head(10))
print("\n📌 Last 10 Rows of the Dataset:")
print(data.tail(10))

# --------------------------------------
# Phase 2 - Dataset Understanding
# --------------------------------------
print(f"\n{'Column Name':<25} {'Data Type':<15} {'Category':<15}")
print("-"*60)
for col in data.columns:
    if data[col].dtype in ['int64', 'float64']:   # Check if column is numerical
        category = "Numerical"
    else:
        category = "Categorical"
    print(f"{col:<25} {str(data[col].dtype):<15} {category:<15}")

cat_columns = ['Ship Mode', 'Segment', 'Country', 'Region', 'City', 'State', 'Category', 'Sub-Category']  # List of categorical columns to inspect
print("\n📌 Categorical Columns Summary:")
print(f"{'Column':<20} {'Unique':<10} {'Sample Values'}")
print("-"*60)
for col in cat_columns:
    unique_count = data[col].nunique()
    unique_vals = data[col].unique()
    if len(unique_vals) > 5:
            display = f"{unique_vals[:3].tolist()} ... (+{len(unique_vals)-3} more)"
    else:
            display = unique_vals.tolist()
    print(f"{col:<20} {unique_count:<10} {display}")


num_columns = ['Sales', 'Quantity', 'Discount', 'Profit', 'Postal Code']  # List of numerical columns to inspect
print("\n📌 Numerical Columns Summary:")
print(f"{'Column':<15} {'Count':<10} {'Min':<12} {'Max':<12} {'Mean':<12} {'Median':<12} {'Std Dev':<12}")
print("-"*90)
for col in num_columns:
    print(f"{col:<15} {data[col].count():<10} {data[col].min():<12.2f} {data[col].max():<12.2f} "
          f"{data[col].mean():<12.2f} {data[col].median():<12.2f} {data[col].std():<12.2f}")
print("\n📌 Quartiles for Numerical Columns:")
for col in num_columns:
    print(f"{col}:")
    print(f"  25%: {data[col].quantile(0.25):.2f}")
    print(f"  50%: {data[col].quantile(0.50):.2f}")
    print(f"  75%: {data[col].quantile(0.75):.2f}")
    print("-" * 30)
# Data info
print("\n📌 Data Info:")
data.info()

# --------------------------------------
# Phase 3 - Data Cleaning & Validation
# --------------------------------------
missing_report = pd.DataFrame({
     'Column': data.columns,
     'Missing Count': data.isnull().sum().values,
     'Missing %': (data.isnull().sum().values / len(data) * 100).round(2)
})
print("\n📌 Missing Values Report:")
print(missing_report)

duplicate_count = data.duplicated().sum()
print(f"\n📌 Duplicate Rows: {duplicate_count}")
data = data.drop_duplicates()
# Check if duplicates are removed
print(f"📌 Total duplicate rows: {data.duplicated().sum():,}")
# Check for negative sales values
negative_sales = data[data['Sales'] < 0]
print(f"📌 Transactions with Negative Sales: {len(negative_sales)}")
# Check for negative Quantity values
invalid_quantity = data[data['Quantity'] <= 0]
print(f"📌 Transactions with Quantity <= 0: {len(invalid_quantity)}")
# Check for negative Discount values
negative_discount = data[data['Discount'] < 0]
print(f"📌 Transactions with Negative Discount: {len(negative_discount)}")
# Rows having Discount greater than 1 
discount_gt_1 = data[data['Discount'] > 1]
print(f"📌 Transactions with Discount > 1: {len(discount_gt_1)}")
print("📌 Datatype of Profit Column:",data['Profit'].dtype)


# ------------------------------------------
# Phase 4 - Exploratory Data Analysis (EDA)
# ------------------------------------------

total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()
total_quantity = data['Quantity'].sum()
avg_discount = data['Discount'].mean()
profit_margin = (total_profit / total_sales) * 100 
# Transaction Summary
print("\n📌 KEY METRICS:")
print("-"*50)
print(f". Total Sales     :  ${total_sales:,.2f}")
print(f". Total Profit    :  ${total_profit:,.2f}")
print(f". Total Quantity  :  {total_quantity}")
print(f". Average Discount:  {avg_discount:.2f}")
print(f". Profit Margin   :  {profit_margin:.2f}%")

# category wise performance 
category_wise_performance = data.groupby('Category').agg(  # category-wise performance metrics
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum'),
    Quantity=('Quantity', 'sum'),
    Avg_Discount=('Discount', 'mean')
).round(2)
print("\n📌 CATEGORY-WISE PERFORMANCE:")
print("-"*50)
print(category_wise_performance)

# Sub-category wise performance
sub_category_wise_performance = data.groupby('Sub-Category').agg(
     Total_Sales = ('Sales', 'sum'),
     Total_Profit = ('Profit', 'sum'),
     Loss_making_Transactions = ('Profit', lambda x: (x < 0).sum())
).round(2).sort_values(by='Total_Sales', ascending=False)
sub_category_wise_performance['Profit_Margin'] = (sub_category_wise_performance['Total_Profit'] / sub_category_wise_performance['Total_Sales']) * 100
print("\n📌 SUB-CATEGORY-WISE PERFORMANCE:")
print("-"*50)
print(sub_category_wise_performance.sort_values(by='Total_Sales', ascending=True).round(2))

# Calculate Profit Margin by Category
category_wise_performance['Profit_Margin'] = (category_wise_performance['Profit'] / category_wise_performance['Sales']) * 100
print("\n📌 CATEGORY-WISE PERFORMANCE WITH PROFIT MARGIN:")
print("-"*70)
print(category_wise_performance.round(2))

# Region-wise performance metrics
region_wise_performance = data.groupby('Region').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
region_wise_performance['Profit_Margin'] = (region_wise_performance['Total_Profit'] / region_wise_performance['Total_Sales']) * 100
region_wise_performance = region_wise_performance.sort_values(['Profit_Margin','Loss_Making_Transactions'], ascending=False)
print("\n📌 REGION-WISE PERFORMANCE:")
print("-"*70)
print(region_wise_performance.round(2))

# Segment-wise performance metrics
segment_wise_performance = data.groupby('Segment').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
segment_wise_performance['Profit_Margin'] = (segment_wise_performance['Total_Profit'] / segment_wise_performance['Total_Sales']) * 100
segment_wise_performance = segment_wise_performance.sort_values('Profit_Margin', ascending=False)
print("\n📌 SEGMENT-WISE PERFORMANCE:")
print("-"*70)
print(segment_wise_performance.round(2))

# discount-wise performance metrics
discount_wise_performance = data.groupby('Discount').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
)
discount_wise_performance['Profit_Margin'] = (discount_wise_performance['Total_Profit'] / discount_wise_performance['Total_Sales']) * 100
discount_wise_performance = discount_wise_performance.sort_values('Discount', ascending=True)
print("\n📌 DISCOUNT-WISE PERFORMANCE:")
print("-"*70)
print(discount_wise_performance.round(2))

# ship mode-wise performance metrics
ship_mode_wise_performance = data.groupby('Ship Mode').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
ship_mode_wise_performance['Profit_Margin'] = (ship_mode_wise_performance['Total_Profit'] / ship_mode_wise_performance['Total_Sales']) * 100
ship_mode_wise_performance = ship_mode_wise_performance.sort_values('Total_Sales', ascending=False)
print("\n📌 SHIP MODE-WISE PERFORMANCE:")
print("-"*70)
print(ship_mode_wise_performance.round(2))

# ------------------------------------------
# Phase 5 - Buisness Qestions & Insights
# ------------------------------------------
# group by sub-category and discount to analyze the impact of discount on profit margin
discount_impact = data.groupby(['Sub-Category', 'Discount']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
discount_impact['Profit_Margin'] = (discount_impact['Total_Profit'] / discount_impact['Total_Sales']) * 100
print("\n📌 DISCOUNT IMPACT ON PROFIT MARGIN BY SUB-CATEGORY:")
print("-"*70)
print(discount_impact.round(2).sort_values(by='Profit_Margin', ascending=True))

# group by region , category and discount to analyze the impact of discount on profit margin by region and category
region_category_discount_impact = data.groupby(['Region', 'Category', 'Discount']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
region_category_discount_impact['Profit_Margin'] = (region_category_discount_impact['Total_Profit'] / region_category_discount_impact['Total_Sales']) * 100
print("\n📌 REGION-CATEGORY-DISCOUNT IMPACT ON PROFIT MARGIN:")
print("-"*70)
print(region_category_discount_impact.round(2).sort_values(by='Profit_Margin', ascending=True))

# ------------------------------------------
# Phase 6 - Advanced Analysis
# ------------------------------------------
# High sales + poor profitability sub-categories
sorted_sales = sub_category_wise_performance.sort_values(by='Total_Sales', ascending=False)
high_sales_poor_profitability = sorted_sales[(sorted_sales['Total_Sales'] > sorted_sales['Total_Sales'].median()) & (sorted_sales['Profit_Margin'] < 0)]
print("\n📌 HIGH SALES + POOR PROFITABILITY SUB-CATEGORIES:")
print("-"*70)
print(high_sales_poor_profitability.round(2))

# High profitabilty + low sales sub-categories
sorted_profit_margin = sub_category_wise_performance.sort_values(by='Profit_Margin', ascending=False)
high_profitability_low_sales = sorted_profit_margin[(sorted_profit_margin['Profit_Margin'] > sorted_profit_margin['Profit_Margin'].median()) & (sorted_profit_margin['Total_Sales'] < sorted_profit_margin['Total_Sales'].median())]
print("\n📌 HIGH PROFITABILITY + LOW SALES SUB-CATEGORIES:")
print("-"*70)
print(high_profitability_low_sales.round(2))

# Region Category Performance Analysis
region_category_performance = data.groupby(['Region', 'Category']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
region_category_performance['Profit_Margin'] = (region_category_performance['Total_Profit'] / region_category_performance['Total_Sales']) * 100
region_category_high_sales_profit = region_category_performance[(region_category_performance['Total_Sales'] > region_category_performance['Total_Sales'].median()) & (region_category_performance['Profit_Margin'] > region_category_performance['Profit_Margin'].median())]
print("\n📌 REGION-CATEGORY PERFORMANCE ANALYSIS:")
print("-"*70)
print(region_category_high_sales_profit.round(2).sort_values(by=['Total_Profit'], ascending=[False]))

# Region Discount Performance Analysis
region_discount_performance = data.groupby(['Region', 'Discount']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
region_discount_performance['Profit_Margin'] = (region_discount_performance['Total_Profit'] / region_discount_performance['Total_Sales']) * 100
print("\n📌 REGION-DISCOUNT PERFORMANCE ANALYSIS:")
print("-"*70)
print(region_discount_performance.round(2).sort_values(by=['Region', 'Discount'], ascending=[True, False]))

# Region category discount performance analysis
region_category_discount_performance = data.groupby(['Region', 'Category', 'Discount']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
).round(2)
region_category_discount_performance['Profit_Margin'] = (region_category_discount_performance['Total_Profit'] / region_category_discount_performance['Total_Sales']) * 100
print("\n📌 REGION-CATEGORY-DISCOUNT PERFORMANCE ANALYSIS:")
print("-"*70)
print(region_category_discount_performance.round(2).sort_values(by=['Region', 'Category', 'Discount'], ascending=[True, True, False]))

# Discount wise performance analysis 
discount_wise_performance = data.groupby('Discount').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Loss_Making_Transactions=('Profit', lambda x: (x < 0).sum())
)
discount_wise_performance['Profit_Margin'] = (discount_wise_performance['Total_Profit'] / discount_wise_performance['Total_Sales']) * 100
print("\n📌 DISCOUNT WISE PERFORMANCE ANALYSIS:")
print("-"*70)
print(discount_wise_performance.round(2).sort_values(by=['Profit_Margin'], ascending=[False]))
# correlation between discount and profit margin
correlation_discount_profit_margin = discount_wise_performance.reset_index()[['Discount', 'Profit_Margin']].corr().iloc[0, 1]
print("\n📌 CORRELATION BETWEEN DISCOUNT AND PROFIT MARGIN:")
print("-"*70)
print(f"Correlation: {correlation_discount_profit_margin:.2f}")

# ------------------------------------------
# Phase 7 - Visualization 
# ------------------------------------------
# Global Styling for all plots
plt.style.use('seaborn-v0_8-darkgrid')              # Background style
plt.rcParams['font.family'] = 'sans-serif'          # Font family
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 10                      # Default font size
plt.rcParams['axes.titlesize'] = 12                 # Chart title size
plt.rcParams['axes.labelsize'] = 10                 # Axis label size
plt.rcParams['legend.fontsize'] = 9                 # Legend text size
# Figure and Grid Setup
fig, axes = plt.subplots(
    2, 2,                          
    figsize=(14, 10),             
    facecolor='#f5f5f5'         
)
# Axis naming 
ax1 = axes[0, 0]  
ax2 = axes[0, 1]  
ax3 = axes[1, 0]   
ax4 = axes[1, 1]   
# Spacing Adjustments
plt.subplots_adjust(
    hspace=0.3,
    wspace=0.25,
    top=0.78,       
    bottom=0.06
)
# Chart 1: Category Performance (Sales vs Profit Margin)
cat_data = data.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()
cat_data["Profit_Margin"] = (cat_data["Total_Profit"] / cat_data["Total_Sales"]) * 100
bars = ax1.bar(                  # Primary Y-axis (Sales bars)
    cat_data["Category"],        # X-axis values
    cat_data["Total_Sales"],     # Y-axis values
    color='#1f77b4',             # Bar color
    edgecolor='white',           # Border color
    linewidth=1,                 # Border width
    label='Sales'                # Legend label
)
ax1_twin = ax1.twinx()           # Secondary Y-axis (Margin line)
ax1_twin.plot(
    cat_data["Category"],
    cat_data["Profit_Margin"],
    color='#ff7f0e',
    marker='o',
    linewidth=2,
    markersize=8,label='Profit Margin'
)
ax1.set_title('Category Performance', fontweight='bold')  # Title + labels
ax1.set_ylabel('Sales ($)')
ax1_twin.set_ylabel('Profit Margin (%)')
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax1_twin.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper left', frameon=True, facecolor='white')

# Chart 2: Regional Performance (Sales vs Profit Margin)
region_data = data.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()
region_data["Profit_Margin"] = (region_data["Total_Profit"] / region_data["Total_Sales"]) * 100

bars = ax2.bar(region_data["Region"], region_data["Total_Sales"],
               color='#2ca02c', label='Sales')

ax2_twin = ax2.twinx()
ax2_twin.plot(region_data["Region"], region_data["Profit_Margin"],
              color='#d62728', marker='o', linewidth=2, label='Profit Margin')

ax2.set_title('Regional Performance', fontweight='bold')
ax2.set_ylabel('Sales ($)')
ax2_twin.set_ylabel('Profit Margin (%)')
h1, l1 = ax2.get_legend_handles_labels()
h2, l2 = ax2_twin.get_legend_handles_labels()
ax2.legend(h1 + h2, l1 + l2, loc='upper left', frameon=True, facecolor='white')

# Chart 3: Sub-Category Profit Margin
subcat_data = data.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()
subcat_data["Profit_Margin"] = (subcat_data["Total_Profit"] / subcat_data["Total_Sales"]) * 100
subcat_data = subcat_data.sort_values("Profit_Margin", ascending=True)  # Sort for readability
colors = ['#d62728' if m < 0 else '#2ca02c' for m in subcat_data["Profit_Margin"]]
bars = ax3.barh(
    subcat_data["Sub-Category"],   # Y-axis values
    subcat_data["Profit_Margin"],  # X-axis values
    color=colors,                  # Conditional color
    edgecolor='white'
)
ax3.set_title('Sub-Category Profitability', fontweight='bold')
ax3.set_xlabel('Profit Margin (%)')
ax3.axvline(x=0, color='black', linewidth=1)   # Zero line

# Chart 4: Discount vs Profit Margin
discount_data = data.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()
discount_data["Profit_Margin"] = (discount_data["Total_Profit"] / discount_data["Total_Sales"]) * 100
ax4.plot(
    discount_data["Discount"] * 100,     # X-axis (as %)
    discount_data["Profit_Margin"],      # Y-axis
    color='#9467bd',
    marker='o',
    markersize=8,
    linewidth=2,
    label='Profit Margin'
)
ax4.axhline(y=0, color='black', linestyle='--', linewidth=1)   # Zero line
ax4.set_title('Discount vs Profit Margin', fontweight='bold')
ax4.set_xlabel('Discount (%)')
ax4.set_ylabel('Profit Margin (%)')
ax4.legend()

fig.suptitle(    # Dashboard Title
    'ShopEase E-Commerce – Business Performance Dashboard',
    fontsize=20,
    fontweight='bold',
    y=0.99,                # Y position (0=bottom, 1=top)
    color='#333333'
)
# KPI card at the Top of the Dashboard
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum() 
profit_margin = (total_profit / total_sales) * 100
total_quantity = data['Quantity'].sum()
positions = [0.12, 0.37, 0.62, 0.87]
labels = [" Total Sales", " Total Profit", " Profit Margin", " Total Quantity"]
values = [
    f"${total_sales:,.0f}",
    f"${total_profit:,.0f}",
    f"{profit_margin:.1f}%",
    f"{total_quantity:,.0f}"
]
for i in range(4):
    fig.text(
        positions[i], 0.88,
        f"{labels[i]}\n\n{values[i]}",
        ha='center', va='center',
        fontsize=12, fontweight='bold',
        color='#333333',
        bbox=dict(
            boxstyle='round,pad=1',
            facecolor='white',
            edgecolor='#1f77b4',
            linewidth=2
        )
    )
plt.show()

# ----------------------------------------------
# Phase 8 - Final Analyst Report
# ----------------------------------------------

print("\n" + "="*70)
print("        📊 SHOPEASE E-COMMERCE – FINAL ANALYST REPORT")
print("="*70)

# 1: Project Objective
print("\n📌 1. PROJECT OBJECTIVE:")
print("-"*70)
print("""
The objective of this analysis is to evaluate ShopEase E-Commerce's 
sales and profitability performance across categories, regions, 
business segments, and discount levels. The analysis aims to identify 
high-performing and underperforming areas, uncover the key factors 
associated with profitability, and provide actionable, data-driven 
recommendations to support strategic business decisions.
""")

# 2: Business Problem
print("\n📌 2. BUSINESS PROBLEM:")
print("-"*70)
print("""
ShopEase E-Commerce generates substantial sales revenue, but 
profitability is not consistent across its business operations. 
Management needs to understand:

    • Which product categories and sub-categories are profitable 
      and which are loss-making?
    • Which regions are efficient and which are underperforming?
    • What is the relationship between discount levels and profit margins?
    • Where should the company focus to improve profitability 
      without compromising sales growth?

Without clear answers to these questions, the business risks 
continuing to generate revenue with poor or negative returns.
""")

# 3: Dataset Overview
print("\n📌 3. DATASET OVERVIEW:")
print("-"*70)
print(f"  • Total Records          : {data.shape[0]:,}")
print(f"  • Total Columns          : {data.shape[1]}")
print(f"  • Memory Usage           : {data.memory_usage(deep=True).sum()/1024:.2f} KB")
print(f"\n  📊 Technical Classification (pandas dtype):")
print(f"    • Numerical Columns    : {len(data.select_dtypes(include=['int64','float64']).columns)}")
print(f"    • Categorical Columns  : {len(data.select_dtypes(include=['object']).columns)}")
print(f"\n  📊 Analytical Classification:")
print(f"    • Measures             : Sales, Quantity, Discount, Profit")
print(f"    • Identifier/Location  : Postal Code")
print(f"    • Categorical Dims     : Ship Mode, Segment, Country, City, State, Region, Category, Sub-Category")
print(f"\n  📊 Dataset Dimensions:")
print(f"    • Unique Categories      : {data['Category'].nunique()}")
print(f"    • Unique Sub-Categories  : {data['Sub-Category'].nunique()}")
print(f"    • Unique Regions         : {data['Region'].nunique()}")
print(f"    • Unique Segments        : {data['Segment'].nunique()}")
print(f"    • Unique Cities          : {data['City'].nunique()}")
print(f"    • Unique States          : {data['State'].nunique()}")

# 4: Cleaning & Validation
print("\n📌 4. DATA CLEANING & VALIDATION:")
print("-"*70)
print(f"  • Missing Values Found         : {data.isnull().sum().sum()}")
print(f"  • Duplicate Rows Removed       : {duplicate_count}")
print(f"  • Negative Sales Transactions  : {len(negative_sales)}")
print(f"  • Negative Quantity Values     : {len(invalid_quantity)}")
print(f"  • Negative Discount Values     : {len(negative_discount)}")
print(f"  • Discount > 100% Values       : {len(discount_gt_1)}")
print(f"  • Data Quality Status          : ✅ Validated for the checked conditions")

# 4: Key KPIs
print("\n📌 5. KEY PERFORMANCE INDICATORS:")
print("-"*70)
print(f"  • Total Sales            : ${total_sales:,.2f}")
print(f"  • Total Profit           : ${total_profit:,.2f}")
print(f"  • Overall Profit Margin  : {profit_margin:.2f}%")
print(f"  • Total Quantity Sold    : {total_quantity:,}")
print(f"  • Average Discount       : {avg_discount:.2f}")
print(f"  • Average Sales per Transaction    : ${data['Sales'].mean():,.2f}")

# 6: EDA Findings
print("\n📌 6. EDA FINDINGS:")
print("-"*70)

print("\n  6.1 Category-Wise Performance:")
print(category_wise_performance.round(2))

print("\n  6.2 Region-Wise Performance:")
print(region_wise_performance.round(2))

print("\n  6.3 Segment-Wise Performance:")
print(segment_wise_performance.round(2))

print("\n  6.4 Ship Mode-Wise Performance:")
print(ship_mode_wise_performance.round(2))

# 7: Advanced Analysis
print("\n📌 7. ADVANCED ANALYSIS:")
print("-"*70)

print("\n  7.1 Discount vs Profit Margin Correlation:")
print(f"     Correlation Value: {correlation_discount_profit_margin:.2f}")
print(f"     Interpretation   : Strong Negative Association")
print(f"     Meaning          : Higher discount levels are strongly negatively")
print(f"                        associated with aggregated profit margin.")

print("\n  7.2 High Sales + Poor Profitability Sub-Categories:")
print(high_sales_poor_profitability.round(2))

print("\n  7.3 High Profitability + Low Sales Sub-Categories:")
print(high_profitability_low_sales.round(2))

print("\n  7.4 Strongest Region × Category Combinations:")
print(region_category_high_sales_profit.round(2).sort_values('Total_Profit', ascending=False))

# 8: Business Insights 
print("\n📌 8. BUSINESS INSIGHTS:")
print("-"*70)

print("""
  8.1 Discount Impact on Profitability:
      Strong negative association (-0.94) between discount level and 
      aggregated profit margin. In the observed aggregated 
      discount-level results, discount levels below 30% remain 
      profitable, while discount levels of 30% and above show 
      negative aggregated margins. At 80% discount, margin reaches 
      -180%.

  8.2 Furniture Category Efficiency Issue:
      Furniture generates ~$742K in sales but only 2.49% profit margin. 
      Office Supplies and Technology generate ~17% margin each. Furniture 
      has a profitability-efficiency problem, not a sales problem.

  8.3 Central Region Requires Attention:
      Central region has ~$500K sales but lowest profit margin (7.92%) 
      and highest loss-making transactions (740). South region has lower 
      sales but higher margin (11.93%).

  8.4 Tables Sub-Category is a Significant Concern:
      Tables generated ~$207K sales (above median) but lost $17,725 
      with -8.56% margin. This makes Tables a particularly important 
      sub-category profitability concern.

  8.5 West × Office Supplies is a Star:
      Generates ~$221K sales with 23.80% margin and $52,528 profit. 
      Highest efficiency among the high-sales, high-margin 
      region-category combinations analyzed.

  8.6 Extreme Discount Risk:
      Central × Office Supplies at 80% discount generated ~$17K sales 
      but lost $30,533 (-180% margin) with 299 loss-making transactions.
""")

# 9: Recommendations
print("\n📌 9. RECOMMENDATIONS:")
print("-"*70)

print("""
  1. Review High-Discount Transactions:
     In the observed dataset, discount levels of 30% and above are 
     associated with negative aggregated profit margins. Management 
     may consider reviewing discount policies at these levels to 
     assess whether the current discount structure aligns with 
     profitability goals.

  2. Fix Furniture Category:
     Investigate why Furniture converts sales into low profit (2.49%). 
     Review pricing, shipping costs, and product mix for this category.

  3. Address Tables Sub-Category:
     Tables is loss-making despite high sales. Consider repricing, 
     reducing discounts, or discontinuing slow-moving variants.

  4. Focus on Central Region:
     Central region has high sales but low margin. Investigate discount 
     patterns, operational costs, and product mix in this region.

  5. Scale West × Office Supplies:
     This combination is highly efficient. Increase marketing spend, 
     expand product range, and replicate best practices to other regions.

  6. Review Extreme Discount Transactions:
     Very high discount levels (e.g., 80%) are consistently associated 
     with significant losses in the observed data. It is recommended 
     that management review extreme-discount transactions and evaluate 
     whether additional approval controls or policy adjustments are 
     warranted.

  7. Explore High-Margin, Low-Sales Sub-Categories:
     Some sub-categories show strong profit margins but relatively low 
     sales volumes. These may represent growth opportunities — 
     increasing visibility and demand through targeted marketing could 
     help scale them while preserving their margin advantage.   
""")

# 10: Final Conclusion
print("\n📌 10. FINAL CONCLUSION:")
print("-"*70)
print("""
ShopEase E-Commerce has a strong sales foundation ($2.3M+) but 
profitability challenges that need attention. The analysis revealed 
that:

    • Overall profit margin is 12.5%, with substantial variation 
      across categories, regions, and discount levels.
    • High discount levels (30%+) show a strong negative association 
      with aggregated profit margins in the observed dataset.
    • Furniture category and Central region are the biggest 
      profitability concerns.
    • West is the strongest region (highest sales, profit, and margin).
    • Technology is the strongest category (highest sales and profit).
    • West × Office Supplies is a particularly strong region-category 
      combination.  

By reviewing discount policies, addressing low-margin categories 
such as Furniture, and prioritizing high-performing regions, ShopEase 
may be able to improve its profitability while maintaining its sales 
base.

The data-driven recommendations in this report provide a clear 
roadmap for management to make informed, strategic decisions that 
balance growth and profitability.
""")

