#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import joblib
import pandas as pd

model = joblib.load('housing_model.pkl')

st.title("House Price Prediction App")

area = st.number_input("Area", min_value=1, value=5000)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

stories = st.number_input(
    "Stories",
    min_value=1,
    value=2
)

parking = st.number_input(
    "Parking",
    min_value=0,
    value=1
)

total_rooms = bedrooms + bathrooms

if bedrooms > 0:
    area_per_bedroom = area / bedrooms
else:
    area_per_bedroom = 0

has_parking = 1 if parking > 0 else 0
luxury_home = 0

mainroad_yes = 1
guestroom_yes = 0
basement_yes = 0
hotwaterheating_yes = 0
airconditioning_yes = 1
prefarea_yes = 0
furnishingstatus_semi_furnished = 0
furnishingstatus_unfurnished = 0

if st.button("Predict Price"):

    input_data = pd.DataFrame([{
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'parking': parking,
        'total_rooms': total_rooms,
        'area_per_bedroom': area_per_bedroom,
        'has_parking': has_parking,
        'luxury_home': luxury_home,
        'mainroad_yes': mainroad_yes,
        'guestroom_yes': guestroom_yes,
        'basement_yes': basement_yes,
        'hotwaterheating_yes': hotwaterheating_yes,
        'airconditioning_yes': airconditioning_yes,
        'prefarea_yes': prefarea_yes,
        'furnishingstatus_semi-furnished': furnishingstatus_semi_furnished,
        'furnishingstatus_unfurnished': furnishingstatus_unfurnished
    }])

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ₦{prediction[0]:,.2f}")
    
# In[ ]:




