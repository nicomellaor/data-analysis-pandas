import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dispersion", page_icon="🔢")

st.markdown("# Dispersion")

if "data" in st.session_state:
    df = st.session_state["data"]

else:
    st.error("No data uploaded")