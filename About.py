import streamlit as st

def app():

    st.title("ℹ️ About This Project")

    st.markdown("""
    # 🏠 House Rent Prediction using Machine Learning
    """)

    st.write("""
    The **House Rent Prediction System** is an end-to-end Machine Learning
    application developed to estimate monthly rental prices based on
    property characteristics.

    The application demonstrates the complete Machine Learning workflow,
    from data preprocessing and exploratory analysis to model deployment
    using Streamlit.
    """)

    st.divider()

    # --------------------------------------------------

    st.header("🎯 Project Objective")

    st.write("""
    The objective of this project is to build a predictive system that can
    estimate house rent using various property features.

    The application assists landlords, tenants, and real-estate businesses
    by providing accurate rent estimates using Machine Learning.
    """)

    st.divider()

    # --------------------------------------------------

    st.header("📊 Dataset Information")

    st.info("""

    Dataset : House Rent Dataset

    Features :

    • BHK

    • Rent

    • Size

    • City

    • Bathroom

    • Furnishing Status

    • Tenant Preferred

    • Floor

    • Posted On

    """)

    st.divider()

    # --------------------------------------------------

    st.header("⚙️ End-to-End Machine Learning Pipeline")

    st.image(
    "images/workflow.png",
    caption="End-to-End House Rent Prediction Workflow",
    use_container_width=True
)

    st.divider()

    # --------------------------------------------------

    st.header("🤖 Machine Learning Model")

    st.success("""

    Algorithm Used

    ✔ Random Forest Regressor

    Why Random Forest?

    • High Accuracy

    • Handles Non-linear Data

    • Reduces Overfitting

    • Robust Performance

    • Feature Importance

    """)

    st.divider()

    # --------------------------------------------------

    st.header("🛠 Technologies Used")

    c1,c2,c3 = st.columns(3)

    with c1:

        st.info("""

    ### Programming

    Python

    Pandas

    NumPy

    """)

    with c2:

        st.info("""

    ### Visualization

    Plotly

    Matplotlib

    Seaborn

    """)

    with c3:

        st.info("""

    ### Machine Learning

    Scikit-Learn

    Random Forest

    GridSearchCV

    StandardScaler

    """)

    st.divider()

    # --------------------------------------------------

    st.header("✨ Key Features")

    st.markdown("""

    ✅ Interactive Dashboard

    ✅ Exploratory Data Analysis

    ✅ Dynamic Filtering

    ✅ House Rent Prediction

    ✅ Model Performance Analysis

    ✅ Feature Importance

    ✅ Responsive Streamlit UI

    """)

    st.divider()

    # --------------------------------------------------

    st.header("👩‍💻 Developer")

    st.success("""

    Developed By

    **Priyanka Pal**

    AI & Machine Learning Project

    Built using Python, Scikit-Learn and Streamlit.

    """)

    st.divider()

    st.markdown(
    """
    <center>

    Made with ❤️ using Streamlit

    </center>
    """,
    unsafe_allow_html=True
    )