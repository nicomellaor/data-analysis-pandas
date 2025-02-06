import streamlit as st
from DataAnalysis import DataAnalysis

st.set_page_config(page_title="Dispertion & Correlation", page_icon="📉")

st.markdown("# Dispertion & Correlation")

if "data" in st.session_state:
    df = st.session_state["data"]

else:
    st.error("No data uploaded")