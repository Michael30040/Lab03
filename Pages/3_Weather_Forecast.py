import streamlit as st
import requests
import json

# OpenWeatherMap API setup
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "791af3bea8dd2112315d6c7900be88fd"

# Function to fetch weather data
def fetch_weather_data(lat, lon, units):
    """Fetch weather data using latitude and longitude."""
    url = f"{WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units={units}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Streamlit app
st.title("Current Weather Data")
st.write("Get current weather information using latitude and longitude.")

# User inputs
lat = st.text_input("Enter Latitude:", value="40.7128")  # NEW
lon = st.text_input("Enter Longitude:", value="-74.0060")  # NEW
units = st.selectbox("Select Temperature Unit:", ["Celsius", "Fahrenheit"]) #NEW
unit_param = "metric" if units == "Celsius" else "imperial"

# Fetch and display weather data
if st.button("Get Weather"): #NEW
    data = fetch_weather_data(lat, lon, unit_param)
    
    if data:
        # Extract weather details
        city_name = data.get("name", "Unknown location")
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        # Display weather details
        st.subheader(f"Weather in {city_name}")
        st.write(f"**Temperature:** {temp}° {units}")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Condition:** {weather_desc.capitalize()}")

        # Display additional
        st.metric(label="Temperature", value=f"{temp}° {units}") #NEW
        st.metric(label="Humidity", value=f"{humidity}%") #NEW
    else:
        st.error("Could not fetch weather data. Please check the inputs and try again.")
