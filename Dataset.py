import streamlit as st
import pandas as pd
import numpy as np

def app():
    
    # -----------------------------------
    # Load Dataset
    # -----------------------------------

    @st.cache_data
    def load_data():
        return pd.read_csv("House_Rent_Dataset.csv")

    df = load_data()

    # -----------------------------------
    # Title
    # -----------------------------------

    st.title("📊 Dataset Overview")

    st.write(
        """
    This section provides an overview of the **House Rent Dataset** used for
    training the Machine Learning model.
    """
    )

    st.divider()

    # -----------------------------------
    # Dataset Metrics
    # -----------------------------------

    rows, cols = df.shape

    missing = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    memory = round(df.memory_usage().sum()/1024,2)

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("📄 Total Records", rows)
    c2.metric("📑 Total Features", cols)
    c3.metric("❌ Missing Values", missing)
    c4.metric("🔁 Duplicate Rows", duplicates)

    st.divider()

    # -----------------------------------
    # Dataset Preview
    # -----------------------------------

    st.subheader("📋 Dataset Preview")

    option = st.radio(
        "Choose View",
        ["First 5 Rows","Last 5 Rows","Random Sample"],
        horizontal=True
    )

    if option=="First 5 Rows":
        st.dataframe(df.head(),use_container_width=True)

    elif option=="Last 5 Rows":
        st.dataframe(df.tail(),use_container_width=True)

    else:
        st.dataframe(df.sample(5),use_container_width=True)

    st.divider()

    # -----------------------------------
    # Dataset Information
    # -----------------------------------

    st.subheader("📌 Dataset Information")

    col1,col2 = st.columns(2)

    with col1:

        st.write("### Numerical Columns")

        num_cols = df.select_dtypes(include=np.number).columns

        st.write(list(num_cols))

    with col2:

        st.write("### Categorical Columns")

        cat_cols = df.select_dtypes(exclude=np.number).columns

        st.write(list(cat_cols))

    st.divider()

    # -----------------------------------
    # Data Types
    # -----------------------------------

    st.subheader("🧾 Data Types")

    dtype_df = pd.DataFrame({
        "Column":df.columns,
        "Data Type":df.dtypes.astype(str)
    })

    st.dataframe(dtype_df,use_container_width=True)

    st.divider()

    # -----------------------------------
    # Missing Values
    # -----------------------------------

    st.subheader("❌ Missing Value Analysis")

    missing_df = pd.DataFrame({
        "Column":df.columns,
        "Missing Values":df.isnull().sum(),
        "Percentage":(
            df.isnull().sum()/len(df)*100
        ).round(2)
    })

    st.dataframe(missing_df,use_container_width=True)

    st.divider()

    # -----------------------------------
    # Duplicate Records
    # -----------------------------------

    st.subheader("🔁 Duplicate Records")

    st.success(f"Total Duplicate Rows : {duplicates}")

    st.divider()

    # -----------------------------------
    # Statistical Summary
    # -----------------------------------

    st.subheader("📈 Statistical Summary")

    summary = df.describe().T

    st.dataframe(summary,use_container_width=True)

    st.divider()

    # -----------------------------------
    # Unique Values
    # -----------------------------------

    st.subheader("🔍 Unique Values")

    unique = pd.DataFrame({
        "Column":df.columns,
        "Unique Values":df.nunique()
    })

    st.dataframe(unique,use_container_width=True)

    st.divider()

    # -----------------------------------
    # Feature Description
    # -----------------------------------

    st.subheader("📖 Feature Description")

    feature = pd.DataFrame({

    "Feature":[
    "BHK",
    "Rent",
    "Size",
    "Floor",
    "Area Type",
    "Area Locality",
    "City",
    "Furnishing Status",
    "Tenant Preferred",
    "Bathroom",
    "Point of Contact",
    "Posted On"
    ],

    "Description":[
    "Number of Bedrooms",
    "Monthly House Rent",
    "House Size (Square Feet)",
    "Current Floor Information",
    "Super/Carpet/Built-up Area",
    "Locality Name",
    "City Name",
    "Furnished/Semi-Furnished/Unfurnished",
    "Preferred Tenant Type",
    "Number of Bathrooms",
    "Owner/Broker Details",
    "Advertisement Posting Date"
    ]

    })

    st.dataframe(feature,use_container_width=True)

    st.divider()

    # -----------------------------------
    # Download Dataset
    # -----------------------------------

    st.subheader("📥 Download Dataset")

    csv = df.to_csv(index=False).encode()

    st.download_button(
        label="⬇ Download Dataset",
        data=csv,
        file_name="House_Rent_Dataset.csv",
        mime="text/csv"
    )

    st.divider()

    # -----------------------------------
    # Footer
    # -----------------------------------

    st.markdown(
    """
    ---
    <center>
    Developed by <b>Priyanka Pal</b><br>
    AI & Machine Learning Project
    </center>
    """,
    unsafe_allow_html=True
    )