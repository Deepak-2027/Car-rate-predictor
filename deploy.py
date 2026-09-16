import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

model = pickle.load(open("used_car_model.pkl", "rb"))

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Used Car Price Prediction")
st.write("Enter the details below to predict the selling price.")

year = st.number_input(
    "Manufacturing Year",
    min_value=2000,
    max_value=datetime.now().year,
    value=2020
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000,
    step=1000
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

car_condition=st.number_input(
    "Car Rating",
    min_value=1,
    value=5,
    step=1
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0, 1, 2, 3]
)

fuel_map = {
    "Petrol": 0,
    "Diesel": 1,
    "CNG": 2
}

fuel = fuel_map[fuel_type]


if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Kilometers Driven": [kms_driven],
        "Year": [year],
        "Owner": [owner],
        "Fuel Type": [fuel],
        "Car Condition": [car_condition]
    })

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")
