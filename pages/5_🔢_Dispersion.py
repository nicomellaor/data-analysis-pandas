import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dispersion", page_icon="🔢")

st.markdown("""
            # Dispersion
            Shows a Scatter plot to observe relationships between two variables (x & y). Numeric columns only.""")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.write("## Scatter plot")
    column_names = list(df.select_dtypes(include=[np.number, np.datetime64]).columns)
    option_x = st.selectbox("X variable", column_names,index=None, placeholder="Select the X variable...")
    option_y = st.selectbox("Y variable", column_names,index=None, placeholder="Select the Y variable...")

    if option_x and option_y:
        fig, ax = plt.subplots(figsize=(8,4))
        sns.scatterplot(x=option_x, y=option_y, data=df, color="lightsalmon", alpha=0.7, ax=ax)
        ax.set_title(f"{option_x} & {option_y}")
        st.pyplot(fig)

else:
    st.error("No data uploaded")