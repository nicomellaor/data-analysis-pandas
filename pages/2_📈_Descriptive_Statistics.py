import streamlit as st
from DataAnalysis import DataAnalysis

st.set_page_config(page_title="Descriptive Statistics", page_icon="📈")

st.markdown("# Descriptive Statistics")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.write(df.describe())
else:
    st.error("No data uploaded")