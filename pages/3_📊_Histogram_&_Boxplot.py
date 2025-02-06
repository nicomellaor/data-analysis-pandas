import streamlit as st
from DataAnalysis import DataAnalysis

st.set_page_config(page_title="Histogram & Boxplot", page_icon="📊")

st.markdown("# Histogram & Boxplot")

if "data" in st.session_state:
    df = st.session_state["data"]

else:
    st.error("No data uploaded")