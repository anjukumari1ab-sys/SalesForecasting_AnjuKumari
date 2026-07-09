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
