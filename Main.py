import streamlit as st
from DataAnalysis import DataAnalysis

st.set_page_config(page_title="Data Analysis App", page_icon="📊")

st.title("Data Analysis App with Pandas")

st.markdown('''
    This is a paragraph example of the explaination of the project.
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