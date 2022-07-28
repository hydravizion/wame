import streamlit as st

number_str = st.text_input(label="Input mobile number eg. 0132962323")
http_str = "https://wa.me/+6"+number_str
st.write(http_str)