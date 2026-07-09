import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Sales Forecasting & Demand Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Forecasting & Demand Intelligence System")
st.markdown("### Internship Project Dashboard")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("sales_cleaned.csv")

df = load_data()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Project Overview",
        "Sales Analysis",
        "Forecasting",
        "Anomaly Detection",
        "Product Segmentation"
    ]
)

# -----------------------------
# Overview
# -----------------------------
if page == "Project Overview":

    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Total Sales", f"${df['Sales'].sum():,.2f}")

    st.write("### Dataset Preview")
    st.dataframe(df.head())
# -----------------------------
# Sales Analysis
# -----------------------------
elif page == "Sales Analysis":

    st.header("📊 Sales Analysis")

    # Category Sales
    st.subheader("Sales by Category")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig1, ax1 = plt.subplots(figsize=(8,5))

    category_sales.plot(
        kind="bar",
        ax=ax1
    )

    ax1.set_xlabel("Category")
    ax1.set_ylabel("Sales")
    ax1.set_title("Total Sales by Category")

    st.pyplot(fig1)

    st.dataframe(category_sales)

    st.divider()

    # Region Sales
    st.subheader("Sales by Region")

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig2, ax2 = plt.subplots(figsize=(8,5))

    region_sales.plot(
        kind="bar",
        ax=ax2
    )

    ax2.set_xlabel("Region")
    ax2.set_ylabel("Sales")
    ax2.set_title("Total Sales by Region")

    st.pyplot(fig2)

    st.dataframe(region_sales)
