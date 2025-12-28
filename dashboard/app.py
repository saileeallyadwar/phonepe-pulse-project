import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="PhonePe Pulse Dashboard",
    layout="wide"
)

st.title("📊 PhonePe Pulse Data Visualization & Exploration")
st.markdown("Interactive dashboard built using PhonePe Pulse GitHub data")

# --------------------------------------------------
# MYSQL CONNECTION
# --------------------------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sailee@999",   # 🔴 CHANGE THIS
    database="phonepe_pulse"
)

query = "SELECT * FROM aggregated_transaction"
df = pd.read_sql(query, conn)

# --------------------------------------------------
# SIDEBAR FILTERS (DROPDOWNS)
# --------------------------------------------------
st.sidebar.header("🔍 Filters")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["year"].unique())
)

quarter = st.sidebar.selectbox(
    "Select Quarter",
    sorted(df["quarter"].unique())
)

transaction_type = st.sidebar.selectbox(
    "Transaction Type",
    sorted(df["transaction_type"].unique())
)

metric = st.sidebar.selectbox(
    "Metric",
    ["Transaction Amount", "Transaction Count"]
)

value_col = "transaction_amount" if metric == "Transaction Amount" else "transaction_count"

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------
filtered_df = df[
    (df["year"] == year) &
    (df["quarter"] == quarter) &
    (df["transaction_type"] == transaction_type)
]

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transaction Amount",
    f"₹ {filtered_df['transaction_amount'].sum():,.0f}"
)

col2.metric(
    "Total Transaction Count",
    f"{filtered_df['transaction_count'].sum():,}"
)

avg_value = (
    filtered_df["transaction_amount"].sum() /
    filtered_df["transaction_count"].sum()
    if filtered_df["transaction_count"].sum() > 0 else 0
)

col3.metric(
    "Average Transaction Value",
    f"₹ {avg_value:,.2f}"
)

# --------------------------------------------------
# TOP STATES BAR CHART
# --------------------------------------------------
st.subheader("🏆 Top 10 States by Selected Metric")

top_states = (
    filtered_df
    .groupby("state")[value_col]
    .sum()
    .reset_index()
    .sort_values(by=value_col, ascending=False)
    .head(10)
)

fig_bar = px.bar(
    top_states,
    x="state",
    y=value_col,
    color=value_col,
    title=f"Top 10 States by {metric}",
    text_auto=".2s"
)

fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar, width="stretch")

# --------------------------------------------------
# TRANSACTION TYPE DISTRIBUTION (DONUT)
# --------------------------------------------------
st.subheader("🍩 Transaction Type Distribution")

type_df = (
    df[
        (df["year"] == year) &
        (df["quarter"] == quarter)
    ]
    .groupby("transaction_type")[value_col]
    .sum()
    .reset_index()
)

fig_donut = px.pie(
    type_df,
    names="transaction_type",
    values=value_col,
    hole=0.45,
    title=f"Transaction Type Split ({metric})"
)

st.plotly_chart(fig_donut, width="stretch")

# --------------------------------------------------
# TREND OVER TIME
# --------------------------------------------------
st.subheader("📈 Transaction Trend Over Time")

trend_df = (
    df
    .groupby(["year", "quarter"])[value_col]
    .sum()
    .reset_index()
)

trend_df["period"] = (
    trend_df["year"].astype(str) +
    " Q" +
    trend_df["quarter"].astype(str)
)

fig_line = px.line(
    trend_df,
    x="period",
    y=value_col,
    markers=True,
    title=f"Transaction Trend Over Time ({metric})"
)

st.plotly_chart(fig_line, width="stretch")

# --------------------------------------------------
# STATE COMPARISON
# --------------------------------------------------
st.subheader("🔍 Compare States")

selected_states = st.multiselect(
    "Select states to compare",
    sorted(df["state"].unique()),
    default=sorted(df["state"].unique())[:3]
)

compare_df = (
    filtered_df[filtered_df["state"].isin(selected_states)]
    .groupby("state")[value_col]
    .sum()
    .reset_index()
)

fig_compare = px.bar(
    compare_df,
    x="state",
    y=value_col,
    color="state",
    title=f"State Comparison ({metric})"
)

st.plotly_chart(fig_compare, width="stretch")

# --------------------------------------------------
# RAW DATA VIEW
# --------------------------------------------------
with st.expander("📂 View Raw Data"):
    st.dataframe(filtered_df)

conn.close()
