import streamlit as st

st.title("Weather forecast for the next days")

places = st.text_input("Places: ")
days = st.slider("Forecasted Days:", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view:", ("Temperature", "Sky"), help="Select the option")

st.subheader(f"{option} for the next {days} days in {places} ")