import streamlit as st
import pickle
import numpy as np
import pandas as pd


def app():

    # ==========================================================
    # Load Model
    # ==========================================================

    with open("house_price_model_and_preprocessors.pkl", "rb") as f:
        model_components = pickle.load(f)

    model = model_components["model"]
    scaler = model_components["scaler"]
    encoder = model_components["label_encoder"]
    # st.write(model_components["feature_columns"])

    feature_columns = model_components["feature_columns"]
    cities = model_components["cities"]
    tenant_preferences = model_components["tenant_preference"]
    furnishing_classes = list(model_components["furnishing_classes"])

    # ==========================================================
    # UI
    # ==========================================================

    st.title("🏠 House Rent Prediction")
    st.write("Enter the property details to estimate the monthly rent.")

    st.subheader("🏠 Enter Property Details")

    c1, c2, c3 = st.columns(3)

    with c1:

        BHK = st.number_input("BHK", 1, 10, 2)

        Bathroom = st.number_input("Bathrooms", 1, 10, 2)

        House_Age = st.number_input("House Age", 0, 100, 5)

    with c2:

        Size = st.number_input("Size (sq.ft)", 100, 10000, 1000)

        Total_Floor = st.number_input("Total Floors", 1, 100, 5)

        Your_Floor = st.number_input("Property Floor", 0, 100, 2)

    with c3:

        Furnishing = st.selectbox(
            "Furnishing",
            furnishing_classes
        )

        City = st.selectbox(
            "City",
            cities
        )

        Tenant_Preference = st.selectbox(
            "Tenant Preference",
            tenant_preferences
        )

    st.divider()

    predict = st.button(
        "🏠 Predict House Rent",
        use_container_width=True
    )

    # ==========================================================
    # Prediction
    # ==========================================================

    if st.button("Predict Rent", use_container_width=True):

        # Create dataframe using training columns

        input_df = pd.DataFrame(
            np.zeros((1, len(feature_columns))),
            columns=feature_columns
        )

        # Numeric Features

        if "BHK" in input_df.columns:
            input_df["BHK"] = BHK

        if "Size" in input_df.columns:
            input_df["Size"] = Size

        if "Bathroom" in input_df.columns:
            input_df["Bathroom"] = Bathroom

        if "HouseAge" in input_df.columns:
            input_df["HouseAge"] = House_Age

        # Floor Ratio

        floor_ratio = Your_Floor / max(Total_Floor, 1)

        if "FloorRatio" in input_df.columns:
            input_df["FloorRatio"] = floor_ratio

        # Encode Furnishing

        furnishing_encoded = encoder.transform([Furnishing])[0]

        if "Furnishing Status" in input_df.columns:
            input_df["Furnishing Status"] = furnishing_encoded

        # One Hot Encoding - City

        city_column = f"City_{City}"

        if city_column in input_df.columns:
            input_df[city_column] = 1

        # One Hot Encoding - Tenant Preference

        tenant_column = f"Tenant Preferred_{Tenant_Preference}"

        if tenant_column in input_df.columns:
            input_df[tenant_column] = 1

        # Scale

        scaled_data = scaler.transform(input_df)

        # Prediction

        prediction = model.predict(scaled_data)

        # Reverse log transform

        predicted_rent = np.expm1(prediction[0])

        # Result

        st.success(f"🏠 Estimated Monthly Rent : ₹ {predicted_rent:,.0f}")

        st.subheader("Input Features")

        st.dataframe(input_df, use_container_width=True)