import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title('Sell Out Forms')

tab1, tab2, tab3, tab4 = st.tabs(["Customer", "Store", "Campaign", "Target"])

with tab1:
    cont1 = st.container()

    with cont1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Input Information")
            CustomerSoldTo = st.text_input(
                "CustomerSoldTo", "input value", key="CustomerSoldTo")
            GroupName = st.text_input(
                "GroupName", "input value", key="GroupName")
            BannerName = st.text_input(
                "BannerName", "input value", key="BannerName")
            BusinessModel = st.selectbox("BusinessModel", ("1P",
                                                           "Partner Program",
                                                           "Reseller"), key="BusinessModel")
            CustomerChannel = st.selectbox("CustomerChannel", ("Multispecialist",
                                                               "Generalist",
                                                               "Directional",
                                                               "Platform",
                                                               "Distributors/B2B"), key="CustomerChannel")
            CustomerSegmentation = st.selectbox("CustomerSegmentation", ("BDAS",
                                                                         "BDFS",
                                                                         "BDMS",
                                                                         "BDSD",
                                                                         "BDSG",
                                                                         "BDSS",
                                                                         "BSDG",
                                                                         "CDCD",
                                                                         "CDMS",
                                                                         "CDSG"),
                                                key="CustomerSegmentation"
                                                )
            WHSChannel = st.radio(
                "WHSChannel", ("FKA", "KA"), horizontal=True, key="WHSChannel")

            if "df" not in st.session_state:
                st.session_state.df = pd.DataFrame(columns=["CustomerSoldTo",
                                                            "GroupName",
                                                            "BannerName",
                                                            "BusinessModel",
                                                            "CustomerChannel",
                                                            "CustomerSegmentation",
                                                            "WHSChannel"])
            num_new_rows = st.sidebar.number_input("Add Rows To Table", 1, 500)
            ncol = st.session_state.df.shape[1]  # col count
            rw = -1
            rwdta = []
            if "num_new_rows" not in st.session_state:
                st.session_state.num_new_rows = num_new_rows

            if "ncol" not in st.session_state:
                st.session_state.ncol = ncol
            if "rw" not in st.session_state and "rwdta" not in st.session_state:
                st.session_state.rw = rw
                st.session_state.rwdta = rwdta
        with col2:
            st.subheader("Customer Fields")
            col2col1, col2col2 = st.columns(2)

            with col2col1:
                date = st.date_input(
                    "Date", datetime.date(2023, 6, 6), key="date")
                StoreCode = st.text_input(
                    "Store Code", "input value", key="store_code")
                ArticleCode = st.text_input(
                    "Article Code", "input value", key="article_code")
                Size = st.text_input("Size", "input value", key="size")
                NetSales = st.text_input(
                    "Net Sales", "input value", key="net_sales")

            with col2col2:
                TotalMarkdown = st.text_input(
                    "Total Markdown", "input value", key="total_markdown")
                NetQuantity = st.text_input(
                    "Net Quantity", "input value", key="net_quantity")
                StockQuantity = st.text_input(
                    "Stock Quantity", "input value", key="stock_quantity")
                WHSPrice = st.text_input(
                    "WHS Price", "input value", key="whs_price")
                InvoiceValue = st.text_input(
                    "Invoice Value", "input value", key="invoice_value")

    col1, col2, col3 = st.columns(3)
    with col2:
        Attach_button = st.button("Attach File", use_container_width=True)
    cont3 = st.container()

    with cont3:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col2:
            edit_button = st.button("Edit", use_container_width=True)
        with col3:
            Delete_button = st.button("Delete", use_container_width=True)
        with col4:
            save_button = st.button("Save", use_container_width=True)
    rwdta = [value for value in st.session_state.df.columns]
    if st.button("Add", use_container_width=True):
        if st.session_state.df.shape[0] == num_new_rows:
            st.error("Add row limit reached. Cant add any more records..")
        else:
            df = st.session_state.df
            rw = st.session_state.df.shape[0] + 1
            st.info(f"Row: {rw} / {num_new_rows} added")
            #st.session_state.df.loc[rw] = rwdta
            new_row = {
                "CustomerSoldTo": st.session_state.CustomerSoldTo,
                "GroupName": st.session_state.GroupName,
                "BannerName": st.session_state.BannerName,
                "BusinessModel": st.session_state.BusinessModel,
                "CustomerChannel": st.session_state.CustomerChannel,
                "CustomerSegmentation": st.session_state.CustomerSegmentation,
                "WHSChannel": st.session_state.WHSChannel,
            }
            st.session_state.df = pd.concat([df, pd.DataFrame(new_row, index=[rw])], ignore_index=True)
            if st.session_state.df.shape[0] == num_new_rows:
                st.error("Add a row, limit reached...")

    st.dataframe(st.session_state.df)
#st.session_state
with tab2:
    st.header("Store")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Campaign")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
    st.header("Target")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
