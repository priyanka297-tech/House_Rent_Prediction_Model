import streamlit as st

def app():

    # ---------------------------------------------------
    # Custom CSS
    # ---------------------------------------------------

    st.markdown("""
    <style>

    .hero{
    background:linear-gradient(90deg,#1565C0,#1E88E5);
    padding:35px;
    border-radius:15px;
    color:white;
    text-align:center;
    }

    .card{
    background:#FFFFFF;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    }

    .feature{
    background:#F5F7FA;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    }

    .footer{
    text-align:center;
    color:gray;
    padding-top:30px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # Hero Section
    # ---------------------------------------------------

    st.markdown("""
    <div class='hero'>

    # 🏠 AI House Rent Prediction System

    ### Predict Monthly House Rent using Machine Learning

    A professional AI-powered application that predicts house rent using
    property features such as location, BHK, size, furnishing status,
    floor information, and tenant preferences.

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ---------------------------------------------------
    # Dashboard Metrics
    # ---------------------------------------------------

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric(
            "Algorithm",
            "Random Forest"
        )

    with col2:
        st.metric(
            "Accuracy",
            "87%"
        )

    with col3:
        st.metric(
            "Framework",
            "Streamlit"
        )

    with col4:
        st.metric(
            "Type",
            "Regression"
        )

    st.divider()

    # ---------------------------------------------------
    # About Project
    # ---------------------------------------------------

    st.header("📖 About the Project")

    st.write("""
    The **House Rent Prediction System** is a Machine Learning application
    designed to estimate monthly rental prices based on various housing
    attributes.

    The system follows the complete Data Science lifecycle including
    data preprocessing, feature engineering, exploratory data analysis,
    model training, hyperparameter tuning, and deployment using Streamlit.

    The prediction model has been trained using the **Random Forest Regressor**
    which achieved high prediction accuracy on unseen data.
    """)

    st.divider()

    # ---------------------------------------------------
    # Features
    # ---------------------------------------------------

    st.header("🚀 Key Features")

    left,right=st.columns(2)

    with left:

        st.markdown("""
    <div class="feature">

    ### 📊 Data Analysis

    - Dataset Overview
    - Missing Value Analysis
    - Statistical Summary
    - Duplicate Detection

    </div>
    """,unsafe_allow_html=True)

        st.markdown("""
    <div class="feature">

    ### 📈 Exploratory Data Analysis

    - Distribution Plots
    - Count Plots
    - Boxplots
    - Correlation Heatmap

    </div>
    """,unsafe_allow_html=True)

    with right:

        st.markdown("""
    <div class="feature">

    ### 🤖 Machine Learning

    - Feature Engineering
    - Data Scaling
    - Random Forest Regression
    - Hyperparameter Tuning

    </div>
    """,unsafe_allow_html=True)

        st.markdown("""
    <div class="feature">

    ### 🏠 Prediction System

    - Real-Time Prediction
    - Interactive User Interface
    - Instant Results
    - Responsive Dashboard

    </div>
    """,unsafe_allow_html=True)

    st.divider()

    # ---------------------------------------------------
    # Workflow
    # ---------------------------------------------------

    st.header("⚙️ Project Workflow")

    st.image(
    "images/workflow.png",
    
    use_container_width=True
)

    st.divider()

    # ---------------------------------------------------
    # Technology Stack
    # ---------------------------------------------------

    st.header("🛠 Technology Stack")

    c1,c2,c3=st.columns(3)

    with c1:

        st.info("""
    ### Programming

    - Python
    - Pandas
    - NumPy
    """)

    with c2:

        st.info("""
    ### Visualization

    - Matplotlib
    - Seaborn
    - Plotly
    """)

    with c3:

        st.info("""
    ### Machine Learning

    - Scikit-Learn
    - Random Forest
    - StandardScaler
    - Pickle
    """)

    st.divider()

    # ---------------------------------------------------
    # Navigation
    # ---------------------------------------------------

    st.header("📌 Dashboard Navigation")

    st.success("""
    Use the sidebar to explore the complete application.

    🏠 Home

    📊 Dataset Overview

    📈 Exploratory Data Analysis

    🤖 Rent Prediction

    📉 Model Performance

    ℹ️ About
    """)

    # ---------------------------------------------------
    # Footer
    # ---------------------------------------------------

    st.markdown("""
    <div class='footer'>

    Developed by <b>Priyanka Pal</b><br>

    AI & Machine Learning Project

    </div>
    """,unsafe_allow_html=True)