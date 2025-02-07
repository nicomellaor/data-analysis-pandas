import streamlit as st
from functions import calculate_iqr

st.set_page_config(page_title="Descriptive Statistics", page_icon="📈")

st.markdown("""
            # Descriptive Statistics
            Summary statistics of the Dataframe provided. Filter by column to display the summary table (all numerics by default).
            Shows measures of central tendency and dispersion.""")

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

    st.write("## Dispersion Measures")
    st.write(df.std(numeric_only=True).to_frame(name="Std"))
    st.write(df.var(numeric_only=True).to_frame(name="Var"))
    st.write(calculate_iqr(df).to_frame(name="IQR"))
else:
    st.error("No data uploaded")