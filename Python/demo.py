# Save this in demo.py
import streamlit as st

st.title("Live Presentation Dashboard")
number = st.slider("Pick a number", 1, 100)
st.write(f"The square of {number} is {number ** 2}")