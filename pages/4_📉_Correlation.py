import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr, kendalltau

st.set_page_config(page_title="Correlation", page_icon="📉")

st.markdown("""
            # Correlation
            Shows possible correlation in the data, using a matrix, a heatmap, and three correlation coefficients (Pearson's r, Spearman's rho & Kendall's tau). 
            Numeric columns only.""")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.write("## Correlation Matrix")
    matrix = df.corr(numeric_only=True)
    st.write(matrix)

    st.write("## Heatmap")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.heatmap(matrix, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.write("## Correlation Coefficients")
    column_names = list(df.select_dtypes(include=np.number).columns)
    option_x = st.selectbox("X variable", column_names,index=None, placeholder="Select the X variable...")
    option_y = st.selectbox("Y variable", column_names,index=None, placeholder="Select the Y variable...")

    if option_x and option_y:
        x = df[option_x]
        y = df[option_y]
        st.write("### Pearson's :orange[r]: ", x.corr(y))
        st.write("### Spearman's :orange[rho]: ", x.corr(y, method="spearman"))
        st.write("### Kendall's :orange[tau]: ", x.corr(y, method="kendall"))

else:
    st.error("No data uploaded")