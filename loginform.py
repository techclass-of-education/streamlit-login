import streamlit as st

st.set_page_config(page_title="Login Form",
                   layout="wide",
                   page_icon="👤")
st.title("Login Here")

email=st.text_input("Email-id",
              placeholder="Enter Email-id")
password=st.text_input("Password",
                       placeholder="Enter password")
st.button("Login")

