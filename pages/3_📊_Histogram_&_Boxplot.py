import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from functions import count_outliers

st.set_page_config(page_title="Histogram & Boxplot", page_icon="📊")

st.markdown("""
            # Histogram & Boxplot
            Displays both graphs and counts the number of outliers. Filter by column (numeric only).""")

if "data" in st.session_state:
    df = st.session_state["data"]
    new_df = df.select_dtypes(include=np.number)
    
    column_names = list(new_df.columns)
    option = st.selectbox("Show graphics", column_names,index=None, placeholder="Select a column name...")
    if option:
        st.write("## Histogram")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(df[option], bins=10, rwidth=0.95, color="lightsalmon")
        ax.set_xlabel(f"{option}")
        ax.set_ylabel("Frequency")
        ax.yaxis.grid(color="lightgray", linestyle="--")
        st.pyplot(fig)
    
        st.write("## Boxplot")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(x=df[option], color="lightsalmon", ax=ax)
        ax.set_title(f"Boxplot {option}")
        ax.xaxis.grid(color="lightgray", linestyle="--")
        st.pyplot(fig)

        outliers = count_outliers(df[option])
        st.write("### Number of :orange[Outliers]: ", outliers)


else:
    st.error("No data uploaded")