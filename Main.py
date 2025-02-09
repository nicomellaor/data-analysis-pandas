import streamlit as st
from DataAnalysis import DataAnalysis

st.set_page_config(page_title="Data Analysis App", page_icon="🐼")

st.title("Data Analysis App with Pandas")

st.markdown('''
            This Data Analysis App is built using **Pandas** and **Streamlit**, allowing users to upload and explore CSV files interactively. The app 
            provides a comprehensive set of tools for data exploration, cleaning, and visualization, making it easier to analyze datasets without writing code.
            
            **Key Features:**
            - *CSV File Upload & Table Display*: Load and visualize data in a tabular format.
            - *Data Cleaning & Preprocessing*: Handle missing values, correct data inconsistencies, and refine datasets.
            - *Descriptive Statistics*: Generate summary statistics (mean, median, standard deviation, etc.).
            - *Visualizations*:
                - *Histograms & Boxplots*: Understand data distributions.
                - *Scatter Plots & Correlation Analysis*: Identify relationships between variables.
                - *Time Series Analysis*: Explore temporal trends in the dataset.
            
            With this Streamlit-powered app, users can seamlessly explore and analyze their data through an intuitive web interface.

            :orange-background[Once you have cleaned the data, you can **download** the CSV file by clicking on the *download button* below in the main table.]
''') 

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    da = DataAnalysis(uploaded_file)
    df = da.get_df()
    st.session_state["data"] = df
    st.success("Data successfully uploaded")
    st.sidebar.info("Select an option above")
    
if "data" in st.session_state:
    df = st.session_state["data"]
    st.markdown("## Dataframe Visualization")    
    st.dataframe(df, hide_index=True)