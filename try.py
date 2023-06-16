import streamlit as st
import pandas as pd

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Sepal Length", 
                                                "Sepal Width", 
                                                "Petal Length", 
                                                "Petal Width", 
                                                "Variety"])

st.subheader("Add Record")
num_new_rows = st.sidebar.number_input("Add Rows",1,50)
if "num_new_rows" not in st.session_state:
    st.session_state.num_new_rows = num_new_rows
ncol = st.session_state.df.shape[1]  # col count
if "ncol" not in st.session_state:
    st.session_state.ncol = ncol
rw = -1
rwdta = []

if "rw" not in st.session_state and "rwdta" not in st.session_state:
    st.session_state.rw = rw
    st.session_state.rwdta = rwdta

with st.form(key="add form", clear_on_submit= True):
    cols = st.columns(ncol)
    if "dfcols" not in st.session_state:
        st.session_state.dfcols = st.session_state.df.columns
    
    # rwdta = ["" for value in range(ncol)]
    for i in range(ncol):
        rwdta.append(cols[i].text_input(st.session_state.df.columns[i]))

    # you can insert code for a list comprehension here to change the data (rwdta) 
    # values into integer / float, if required

    if st.form_submit_button("Add"):
        if st.session_state.df.shape[0] == num_new_rows:
            st.error("Add row limit reached. Cant add any more records..")
        else:
            rw = st.session_state.df.shape[0] + 1
            st.info(f"Row: {rw} / {num_new_rows} added")
            st.session_state.df.loc[rw] = rwdta
            st.session_state
            if st.session_state.df.shape[0] == num_new_rows:
                st.error("Add row limit reached...")

    st.session_state
    st.dataframe(st.session_state.df)

    df = st.session_state.df