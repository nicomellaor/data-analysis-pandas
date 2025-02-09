import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

st.set_page_config(page_title="Time Series", page_icon="📈")

st.markdown("""
            # Time Series Analysis
            Time series can be decomposed as a combination of level, trend, seasonality and noise.
            
            - Level: average value in the series
            - Trend: increasing or decreasing value in the series
            - Seasonality: repeating short-term cycle in the series
            - Noise: random variation in the series
            
            More info: [How to Decompose Time Series Data into Trend and Seasonality.](https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/)""")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.write("## Resample")
    st.write("Resample time-series data. The object must have a datetime-like index.")
    date_columns = list(df.select_dtypes(include=np.datetime64).columns)
    date_column = st.selectbox("Index column", date_columns,index=None, placeholder="Select a datetime column...")

    num_columns = list(df.select_dtypes(include=np.number).columns)
    num_column = st.selectbox("Numeric column", num_columns,index=None, placeholder="Select a numeric column...")

    frequency = st.selectbox("Frequency", ["ME", "YE"], index=None, placeholder="Select a frequency...")

    st.write("## Time Series")
    model_option = st.selectbox("Model", ["additive", "multiplicative"], index=None, placeholder="Select a type of model...")

    if date_columns and num_column and frequency and model_option:
        #Resample
        new_df = df.set_index(date_column)
        series = new_df[num_column].resample(frequency).mean().ffill()

        #Time Series
        result = seasonal_decompose(series, model=model_option)
        trend = result.trend
        seasonal = result.seasonal
        resid = result.resid
        observed = result.observed

        fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)

        axes[0].plot(observed, label='Observed', color='blue')
        axes[0].legend()
        axes[0].set_title('Observed')

        axes[1].plot(trend, label='Trend', color='red')
        axes[1].legend()
        axes[1].set_title('Trend')

        axes[2].plot(seasonal, label='Seasonal', color='green')
        axes[2].legend()
        axes[2].set_title('Seasonal')

        axes[3].plot(resid, label='Resid', color='orange')
        axes[3].legend()
        axes[3].set_title('Resid')

        plt.tight_layout()
        
        st.pyplot(fig)
else:
    st.error("No data uploaded")