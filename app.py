import streamlit as st 
from GetRequest import get_whether_data 
st.title("API Calling")
city = st.text_input("Enter city name")
btn =st.button("Submit")
if btn:
    data = get_whether_data(city)
    st.write(f"Weather: {data['weather'][0]['main']}")
    st.write(f"Description: {data['weather'][0]['description']}")
    st.write(f"Temperature: {data['main']['temp']}")
    