import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide"
)

st.title("📊 Sales Forecasting & Demand Intelligence System")
st.markdown("---")

st.markdown("""
### Project Objective

This dashboard provides an interactive analysis of the Superstore Sales dataset,
including sales trends, category-wise performance, regional analysis, and
forecasting insights generated from machine learning models.
""")

# Load Data
df = pd.read_csv("sales_cleaned.csv")
# ==============================
# Dashboard KPI Cards
# ==============================

total_sales = df["Sales"].sum()
total_orders = len(df)
total_categories = df["Category"].nunique()
total_regions = df["Region"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("🛒 Orders", total_orders)
col3.metric("📦 Categories", total_categories)
col4.metric("🌍 Regions", total_regions)
# ==============================
# Sidebar Filters
# ==============================

st.sidebar.header("Dashboard Filters")
st.sidebar.markdown("---")

st.sidebar.info(
    "Use the filters below to explore sales by region and category."
)
selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]
    
st.header("Dataset Preview")
st.caption("Preview of the filtered dataset based on the selected filters.")
st.dataframe(filtered_df.head(10))

st.write(
    f"Rows: {filtered_df.shape[0]} | Columns: {filtered_df.shape[1]}"
)st.markdown("---")
st.header("Sales by Category")
st.caption("Comparison of total sales across product categories.")
category_sales = (
    filtered_df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,5))

category_sales.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Total Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales")

st.pyplot(fig)
st.markdown("---")
st.header("Sales by Region")
st.caption("Comparison of sales across different geographical regions.")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots(figsize=(8,5))

region_sales.plot(
    kind="bar",
    ax=ax2
)

ax2.set_title("Total Sales by Region")
ax2.set_xlabel("Region")
ax2.set_ylabel("Sales")

st.pyplot(fig2)
st.markdown("---")
# ==============================
# Monthly Sales Trend
# ==============================

st.header("📈 Monthly Sales Trend")
st.caption("Monthly sales trend based on the selected filters.")

temp_df = filtered_df.copy()

temp_df["Order Date"] = pd.to_datetime(
    temp_df["Order Date"]
)

monthly_sales = (
    temp_df
    .groupby(
        temp_df["Order Date"].dt.to_period("M")
    )["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

fig3, ax3 = plt.subplots(figsize=(12,5))

monthly_sales.plot(
    
    marker="o",
    linewidth=2,
    ax=ax3
)

ax3.set_title("Monthly Sales Trend")
ax3.set_xlabel("Month")
ax3.set_ylabel("Sales")

plt.xticks(rotation=45)

st.pyplot(fig3)
st.markdown("---")
# ==============================
# Forecast Summary
# ==============================

st.header("📊 Forecast Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Best Model",
        "SARIMA"
    )

    st.metric(
        "Forecast Horizon",
        "3 Months"
    )

with col2:
    st.metric(
        "MAE",
        "18031.40"
    )

    st.metric(
        "MAPE",
        "18.97%"
    )

st.info(
    """
The SARIMA model achieved the best forecasting performance
among all the implemented models and was selected for
future sales prediction.
"""
)
# ==============================
# Project Information
# ==============================

st.header("📁 Project Information")

st.write("""
### Models Implemented

- ✅ SARIMA
- ✅ Facebook Prophet
- ✅ XGBoost

### Machine Learning Techniques

- Time Series Forecasting
- Anomaly Detection
- K-Means Clustering

### Deployment

- GitHub
- Streamlit Community Cloud
""")
st.markdown("")
st.success("Dashboard Loaded Successfully!")

st.markdown("---")

st.caption(
    "Developed by Anju Kumari | End-to-End Sales Forecasting & Demand Intelligence System"
)
