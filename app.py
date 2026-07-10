import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide"
)

st.title("📊 Sales Forecasting & Demand Intelligence System")

st.write(
    """
    This dashboard presents the analysis performed on the Superstore Sales dataset.
    """
)

# Load Data
df = pd.read_csv("sales_cleaned.csv")

st.header("Dataset Preview")

st.dataframe(df.head())

st.write("Shape of Dataset:", df.shape)

st.header("Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
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

st.header("Sales by Region")

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

ax2.set_title("Total Sales by Region")
ax2.set_xlabel("Region")
ax2.set_ylabel("Sales")

st.pyplot(fig2)

st.success("Dashboard Loaded Successfully!")
