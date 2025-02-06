import streamlit as st
from DataAnalysis import DataAnalysis

st.set_page_config(page_title="Descriptive Statistics", page_icon="📈")

st.markdown("""
            # Descriptive Statistics
            Summary statistics of the Dataframe provided""")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.write("## Summary Table")
    column_names = list(df.columns)
    option = st.selectbox("Show Table", column_names,index=None, placeholder="Select a column name...")
    if option:
        st.write(df[option].describe())
    else:
        st.write(df.describe())
    
    st.write("## Central Tendency")
    st.write(df.mean(numeric_only=True).to_frame(name="Mean"))
    st.write(df.median(numeric_only=True).to_frame(name="Median"))
    st.write(df.mode().iloc[0].to_frame(name="Mode"))
else:
    st.error("No data uploaded")