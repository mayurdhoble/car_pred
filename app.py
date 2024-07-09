import streamlit as st
import pickle
import pandas as pd
import numpy as np

model=pickle.load(open('lgrmodelf.pkl','rb'))
car=pd.read_csv(r'file:///C:\Users\dell\Downloads\Cleaned_Car_data.csv')

st.title('Car Price Prediction')

# Assuming you have a loaded prediction model named 'model'

for companies in [car['company']]:
  selected_company = st.selectbox("Select the company:", companies)
selected_names = car.iloc[:, 1]  # Assuming "name" is the second column (index 1)

selected_names=car['name']
selected_model=st.selectbox("Select the model:", selected_names)

for years in [car['year']]:
  selected_year = st.selectbox("Select Year of Purchase:", years)

km_driven = st.number_input("Enter the Number of Kilometres driven:")

for fuel_types in [car['fuel_type']]:
  selected_fuel_type = st.selectbox("Select the fuel type:", fuel_types)
  


def predict_price():
  # Prepare user input data as a DataFrame
  data = np.array([selected_company,selected_model, selected_year, km_driven, selected_fuel_type])
  

  # Make prediction using the model
  prediction = model.predict(data)

  # Assuming the model returns a single value
  predicted_price = prediction
  st.write(f"Prediction: ₹ {predicted_price:.2f}")  # Format price with 2 decimals

if st.button("Predict Price"):
  predict_price()
