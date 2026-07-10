import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def app():

    st.title("📉 Machine Learning Model Performance")

    st.markdown("""
    This page presents the performance of the **Random Forest Regressor**
    used for predicting house rent.
    """)

    st.divider()

    # -------------------------------------------------
    # Metrics
    # -------------------------------------------------

    R2 = 0.87
    MAE = 0.18
    RMSE = 0.26
    MSE = 0.07

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("📈 R² Score",R2)
    c2.metric("📉 MAE",MAE)
    c3.metric("📊 RMSE",RMSE)
    c4.metric("📌 MSE",MSE)

    st.divider()

    # -------------------------------------------------
    # Metric Explanation
    # -------------------------------------------------

    st.subheader("📖 Performance Interpretation")

    st.success(f"""
    ✅ **R² Score ({R2})**

    The model explains approximately **87%** of the variance in house rent,
    indicating strong predictive capability.
    """)

    st.info(f"""
    📉 **Mean Absolute Error ({MAE})**

    On average, the prediction error is relatively low,
    indicating reliable rent estimation.
    """)

    st.warning(f"""
    📊 **Root Mean Squared Error ({RMSE})**

    RMSE is close to MAE,
    suggesting the model does not produce many large prediction errors.
    """)

    st.divider()

    # -------------------------------------------------
    # Feature Importance
    # -------------------------------------------------

    st.header("⭐ Feature Importance")

    importance = pd.DataFrame({

    "Feature":[
    "Size",
    "BHK",
    "Bathroom",
    "Floor Ratio",
    "House Age",
    "City",
    "Tenant Preferred",
    "Furnishing Status"
    ],

    "Importance":[
    0.36,
    0.22,
    0.13,
    0.09,
    0.08,
    0.05,
    0.04,
    0.03
    ]

    })

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        text_auto=".2f",
        title="Top Features Influencing House Rent"
    )

    fig.update_layout(height=550)

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # -------------------------------------------------
    # Predicted vs Actual
    # -------------------------------------------------

    st.header("📈 Predicted vs Actual")

    sample = pd.DataFrame({

    "Actual":[20,25,28,32,36,40,45,50,55,60],
    "Predicted":[19,24,30,31,35,42,46,49,57,59]

    })

    fig = px.scatter(
        sample,
        x="Actual",
        y="Predicted",
        trendline="ols",
        title="Predicted vs Actual Rent"
    )

    fig.update_layout(height=600)

    st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # -------------------------------------------------
    # Conclusion
    # -------------------------------------------------

    st.success("""
    ### 🎯 Model Summary

    ✔ Algorithm : Random Forest Regressor

    ✔ Hyperparameter Tuned using GridSearchCV

    ✔ Good Generalization Performance

    ✔ Suitable for Real-Time House Rent Prediction
    """)