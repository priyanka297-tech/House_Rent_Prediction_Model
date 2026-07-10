import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

def app():

    # -------------------------------------------------------
    # Load Dataset
    # -------------------------------------------------------

    @st.cache_data
    def load_data():
        return pd.read_csv("House_Rent_Dataset.csv")

    df = load_data()

    # -------------------------------------------------------
    # CSS
    # -------------------------------------------------------

    st.markdown("""
    <style>

    .big-font{
    font-size:35px !important;
    font-weight:bold;
    color:#1565C0;
    }

    .small-font{
    font-size:18px;
    color:gray;
    }

    </style>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------
    # Header
    # -------------------------------------------------------

    st.markdown(
    """
    <div class='big-font'>
    📈 Exploratory Data Analysis Dashboard
    </div>

    <div class='small-font'>
    Interactive visualization and analysis of the House Rent Dataset.
    </div>
    """,
    unsafe_allow_html=True
    )

    st.divider()

    # -------------------------------------------------------
    # KPI Cards
    # -------------------------------------------------------

    rows = df.shape[0]
    cols = df.shape[1]

    cities = df["City"].nunique()

    avg_rent = round(df["Rent"].mean())

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("📄 Total Records",rows)
    c2.metric("📑 Total Features",cols)
    c3.metric("🏙 Cities",cities)
    c4.metric("💰 Avg Rent",f"₹ {avg_rent:,}")

    st.divider()

    # -------------------------------------------------------
    # Sidebar Filters
    # -------------------------------------------------------

    st.sidebar.header("🔎 Filters")

    city = st.sidebar.multiselect(
        "Select City",
        sorted(df["City"].unique()),
        default=sorted(df["City"].unique())
    )

    bhk = st.sidebar.multiselect(
        "Select BHK",
        sorted(df["BHK"].unique()),
        default=sorted(df["BHK"].unique())
    )

    furnishing = st.sidebar.multiselect(
        "Furnishing Status",
        sorted(df["Furnishing Status"].unique()),
        default=sorted(df["Furnishing Status"].unique())
    )

    tenant = st.sidebar.multiselect(
        "Tenant Preference",
        sorted(df["Tenant Preferred"].unique()),
        default=sorted(df["Tenant Preferred"].unique())
    )

    filtered_df = df[
        (df["City"].isin(city)) &
        (df["BHK"].isin(bhk)) &
        (df["Furnishing Status"].isin(furnishing)) &
        (df["Tenant Preferred"].isin(tenant))
    ]

    st.success(f"Showing {len(filtered_df)} records")

    st.divider()

    # ==========================================================
    # COUNT PLOTS
    # ==========================================================

    st.header("📊 Count Plots")

    cat_cols = [
        "City",
        "BHK",
        "Furnishing Status",
        "Tenant Preferred",
        "Bathroom"
    ]

    selected_cat = st.selectbox(
        "Select Categorical Feature",
        cat_cols
    )

    fig = px.histogram(
        filtered_df,
        x=selected_cat,
        color=selected_cat,
        text_auto=True,
        title=f"{selected_cat} Distribution"
    )

    fig.update_layout(
        height=550,
        showlegend=False
    )

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # ==========================================================
    # HISTOGRAM
    # ==========================================================

    st.header("📈 Histogram")

    num_cols = [
        "Rent",
        "Size",
        "Bathroom",
        "BHK"
    ]

    selected_num = st.selectbox(
        "Select Numerical Feature",
        num_cols
    )

    fig = px.histogram(
        filtered_df,
        x=selected_num,
        nbins=30,
        marginal="box",
        title=f"{selected_num} Distribution"
    )

    fig.update_layout(height=550)

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # ==========================================================
    # BOXPLOT
    # ==========================================================

    st.header("📦 Boxplot Analysis")

    box_col = st.selectbox(
        "Select Feature",
        num_cols,
        key="box"
    )

    fig = px.box(
        filtered_df,
        y=box_col,
        color_discrete_sequence=["#1565C0"],
        title=f"Outlier Detection - {box_col}"
    )

    fig.update_layout(height=550)

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    st.info(
    """
    📌 Use the sidebar filters to dynamically explore the dataset.
    All charts update automatically based on your selected filters.
    """
    )
    
    # ==========================================================
    # CORRELATION HEATMAP
    # ==========================================================

    import plotly.figure_factory as ff

    st.divider()

    st.header("🔥 Correlation Heatmap")

    numeric_df = filtered_df.select_dtypes(include=np.number)

    corr = numeric_df.corr().round(2)

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=corr.values,
        colorscale="RdBu",
        showscale=True
    )

    fig.update_layout(
        height=700,
        title="Correlation Matrix"
    )

    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================================
    # SCATTER PLOT
    # ==========================================================

    st.divider()

    st.header("📉 Scatter Plot Analysis")

    num_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox(
            "Select X-axis",
            num_cols,
            index=num_cols.index("Size")
        )

    with col2:
        y_axis = st.selectbox(
            "Select Y-axis",
            num_cols,
            index=num_cols.index("Rent")
        )

    color = st.selectbox(
        "Color By",
        ["City", "BHK", "Furnishing Status", "Tenant Preferred"]
    )

    fig = px.scatter(
        filtered_df,
        x=x_axis,
        y=y_axis,
        color=color,
        size="Bathroom",
        hover_data=filtered_df.columns,
        title=f"{y_axis} vs {x_axis}"
    )

    fig.update_layout(height=650)

    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================================
    # RELATIONSHIP PLOT
    # ==========================================================

    st.divider()

    st.header("🏡 Relationship Analysis")

    cat = st.selectbox(
        "Select Category",
        ["City",
        "BHK",
        "Furnishing Status",
        "Tenant Preferred"],
        key="relationship"
    )

    fig = px.box(
        filtered_df,
        x=cat,
        y="Rent",
        color=cat,
        title=f"Rent Distribution by {cat}"
    )

    fig.update_layout(
        height=600,
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================================
    # CITY ANALYSIS
    # ==========================================================

    st.divider()

    st.header("🏙 Average Rent by City")

    city_df = (
        filtered_df
        .groupby("City")["Rent"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        city_df,
        x="City",
        y="Rent",
        color="Rent",
        text_auto=".2f",
        title="Average Rent by City"
    )

    fig.update_layout(
        height=600,
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================================
    # BHK ANALYSIS
    # ==========================================================

    st.divider()

    st.header("🏠 Average Rent by BHK")

    bhk_df = (
        filtered_df
        .groupby("BHK")["Rent"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        bhk_df,
        x="BHK",
        y="Rent",
        markers=True,
        title="Average Rent vs BHK"
    )

    fig.update_layout(height=550)

    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================================
    # DOWNLOAD REPORTS
    # ==========================================================

    st.divider()

    st.header("📋 Download Reports")

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Filtered Dataset",
        data=csv,
        file_name="Filtered_House_Rent_Dataset.csv",
        mime="text/csv"
    )

    corr_csv = corr.to_csv().encode("utf-8")

    st.download_button(
        label="⬇ Download Correlation Matrix",
        data=corr_csv,
        file_name="Correlation_Matrix.csv",
        mime="text/csv"
    )

    summary = filtered_df.describe().round(2)

    summary_csv = summary.to_csv().encode("utf-8")

    st.download_button(
        label="⬇ Download Statistical Summary",
        data=summary_csv,
        file_name="Statistical_Summary.csv",
        mime="text/csv"
    )