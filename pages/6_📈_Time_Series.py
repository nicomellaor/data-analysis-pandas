import streamlit as st

st.set_page_config(page_title="Time Series", page_icon="📈")

st.markdown("# Time Series Analysis")

if "data" in st.session_state:
    df = st.session_state["data"]

else:
    st.error("No data uploaded")