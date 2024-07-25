import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")

places = st.text_input("Places: ")
days = st.slider("Forecasted Days:", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view:", ("Temperature", "Sky"), help="Select the option")

st.subheader(f"{option} for the next {days} days in {places} ")

def get_data(days):
    dates = ["2024-26-07", "2024-27-07", "2024-28-07"]
    temperatures = [24,25,27]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)