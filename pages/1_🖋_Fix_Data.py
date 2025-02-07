import streamlit as st

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

    st.write(":orange-background[Select what to do with null values]")
    left, right = st.columns(2)
    number = st.number_input("Replace custom", placeholder="Type a number...", key="null_input")
    if st.button(f"Replace with {number}"):
        #function
        st.success("Values successfully replaced")

    if left.button("Replace with median", use_container_width=True):
        #function
        st.success("Values successfully replaced")
        
    if right.button("Remove rows", use_container_width=True):
        #function
        st.success("Values successfully deleted")

    st.divider()
    
    st.write("### Date Column")
    column_names = list(df.columns)
    option_date = st.selectbox("Select dates", column_names, index=None, placeholder="Select a date column...")

    if option_date:
        dtype = df[option_date].dtype
        st.write("dtype: ", dtype)
        if st.button("Change to datetime"):
            #function
            st.success("dtype successfully changed")
    
    st.divider()

    st.write("### Age Data")
    option_age = st.selectbox("Select ages", column_names, index=None, placeholder="Select an age column...")
    
    if option_age:
        #function to count ages conditions
        st.write("Inconsistent age data (numbers less than 0 and greater than 100): ")
        left_2, right_2 = st.columns(2)
        number_2 = st.number_input("Replace ages", value=0, placeholder="Type an age...", key="age_input")
        if st.button(f"Replace with {number_2}"):
            #function
            st.success("Values successfully replaced")

        if left_2.button("Replace with median", use_container_width=True, key="button_l_2"):
            #function
            st.success("Values successfully replaced")
            
        if right_2.button("Remove rows", use_container_width=True, key="button_r_2"):
            #function
            st.success("Values successfully deleted")

else:
    st.error("No data uploaded")