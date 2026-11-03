
import streamlit as st

st.title("Clean Streamlit Test")

domain = st.text_input("Enter a domain")
if st.button("Test"):
    st.success(f"Input received: {domain}")

