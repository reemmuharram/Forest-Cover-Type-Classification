import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import streamlit as st

model = joblib.load("model.pkl")

st.title("Forest Cover Type Classification 🌳")
st.header("Please fill the following info")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("⛰️ Surface Characteristics")
    Elevation = st.number_input("Enter the elevation in meters:", 
                                min_value=1859, value = 2000, max_value=3858, step = 100)
    Aspect = st.number_input("Enter the aspect in degrees azimuth", 
                            min_value = 0, max_value = 360, step = 45, value = 90)
    Slope = st.number_input("Enter the Slope in degrees",
                            min_value = 0, max_value = 360, value=180, step = 10)


with col2:
    st.write("📏 Proximity Features")
    Horizontal_Distance_To_Hydrology = st.number_input("Enter the Horizontal Distance To Hydrology to nearest water surface", 
                                                    min_value=0, step=100, max_value=1397, value=500)
    Horizontal_Distance_To_Roadways = st.number_input("Enter the Horizontal Distance to the nearest roadway", 
                                                    min_value = 0, max_value = 7117, value = 3500, step = 100)
    Vertical_Distance_To_Hydrology = st.number_input("Enter teh Vertical Distance to the nearest water surface", 
                                                    min_value = -173, max_value = 601, value = 100, step = 100)
    Horizontal_Distance_To_Fire_Points = st.number_input("Enter the Horizontal Distance to the nearest wildfire ignition points",
                                                     min_value = 0, max_value = 7173, value = 3500, step = 100)
    
with col3:
    st.write("🔆 Hillshade")
    Hillshade_9am = st.number_input("Enter the Hillshade index at 9AM, summer solstice", 
                                    min_value = 0, max_value = 254, value = 100, step = 50)
    Hillshade_Noon = st.number_input("Enter the Hillshade index at noon, summer solstice",
                                    min_value = 0, max_value = 254, value = 100, step = 50)
    Hillshade_3pm = st.number_input("Enter the Hillshade index at 3PM, summer solstice",
                                    min_value = 0, max_value = 254, value = 100, step = 50)
    
with col4:
    st.write("🌱 Wilderness Area and Soil Type")
    Wilderness_Area = st.radio("Choose the wilderness area designition:", [1, 2, 3, 4])
    Soil_Type = st.slider("Choose the soil type designation", min_value = 0, max_value = 40, value = 20, step = 1)


if st.button("Predict The Forest Cover Type 🌳"):
    data = {"Elevation" : Elevation,
            "Aspect" : Aspect,
            "Slope" : Slope,
            "Horizontal_Distance_To_Hydrology" : Horizontal_Distance_To_Hydrology,
            "Vertical_Distance_To_Hydrology" : Vertical_Distance_To_Hydrology,
            "Horizontal_Distance_To_Roadways" : Horizontal_Distance_To_Roadways,
            "Hillshade_9am" : Hillshade_9am,
            "Hillshade_Noon" : Hillshade_Noon,
            "Hillshade_3pm" : Hillshade_3pm,
            "Horizontal_Distance_To_Fire_Points" : Horizontal_Distance_To_Fire_Points,
            "Soil_Type" : Soil_Type,
            "Wilderness_Area" : Wilderness_Area
    }
    df = pd.DataFrame([data])
    preds = model.predict(df)[0]
    st.success(f"Forest Cover Type is: {preds} ✅")