import streamlit as st
from functions import replace_nulls, remove_nulls, change_to_datetime, count_inconsistent_ages, replace_ages, remove_ages

st.set_page_config(page_title="Fix Data", page_icon="🖋")

st.markdown("""
            # Fix Data
            Clears the dataset. Identifies missing/null values, empty cells, wrong format. Fixes dtype to datetime64 for Dates and changes the date format.
            Identifies inconsistent age data (such as negative numbers or numbers greater than 100).""")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.write("### Null values")
    null = df.isnull().sum().to_frame("null")
    st.write(null)
    duplicated = df.duplicated().sum()
    st.write("duplicated data counted:", duplicated)

    st.write(":orange-background[Select what to do with null values. First, **select one** of the columns below.]")
    column_names = list(df.columns)
    option_null = st.selectbox("Column of nulls", column_names, index=None, placeholder="Choose a column of nulls")

    number = st.number_input("Replace custom", placeholder="Type a number...", key="null_input")
    if st.button(f"Replace with {number}"):
        new_df = replace_nulls(df, option_null, number)
        st.session_state["data"] = new_df
        st.success("Values successfully replaced")

    if st.button("Replace with median"):
        mdn = df[option_null].median()
        new_df = replace_nulls(df, option_null, mdn)
        st.session_state["data"] = new_df
        st.success("Values successfully replaced")
        
    if st.button("Remove rows"):
        new_df = remove_nulls(df, option_null)
        st.session_state["data"] = new_df
        st.success("Values successfully deleted")

    st.divider()
    
    st.write("### Date Column")
    option_date = st.selectbox("Select dates", column_names, index=None, placeholder="Select a date column...")

    if option_date:
        dtype = df[option_date].dtype
        st.write("dtype: ", dtype)
        if st.button("Change to datetime"):
            new_df = change_to_datetime(df, option_date)
            st.session_state["data"] = new_df
            st.success("dtype successfully changed")
    
    st.divider()

    st.write("### Age Data")
    option_age = st.selectbox("Select ages", column_names, index=None, placeholder="Select an age column...")
    
    if option_age:
        ages_num = count_inconsistent_ages(df, option_age)
        st.write("Inconsistent age data (numbers less than 0 and greater than 100): ", ages_num)

        number_2 = st.number_input("Replace ages", value=0, placeholder="Type an age...", key="age_input")
        if st.button(f"Replace with {number_2}"):
            new_df = replace_ages(df, option_age, number_2)
            st.session_state["data"] = new_df
            st.success("Values successfully replaced")

        if st.button("Replace with median", key="button_l_2"):
            mdn = df[option_age].median()
            new_df = replace_ages(df, option_age, mdn)
            st.session_state["data"] = new_df
            st.success("Values successfully replaced")
            
        if st.button("Remove rows", key="button_r_2"):
            new_df = remove_ages(df, option_age)
            st.session_state["data"] = new_df
            st.success("Values successfully deleted")

    st.markdown(":orange-background[Once you have cleaned the data, you can **download** the CSV file by clicking on the *download button* below in the **Main** page table.]")

else:
    st.error("No data uploaded")