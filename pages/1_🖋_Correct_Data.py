import streamlit as st

st.set_page_config(page_title="Correct Data", page_icon="🖋")

st.markdown("# Correct Data")

if "data" in st.session_state:
    df = st.session_state["data"]

else:
    st.error("No data uploaded")