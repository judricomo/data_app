import datetime
import streamlit as st
import pandas as pd

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
                                                               "Distributors/B2B"),
                                                               key="CustomerChannel")
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
            st.session_state.df = pd.concat([df,
                                             pd.DataFrame(new_row, index=[rw])],
                                             ignore_index=True)
            if st.session_state.df.shape[0] == num_new_rows:
                st.error("Add a row, limit reached...")

    st.dataframe(st.session_state.df)

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(st.session_state.df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='dataframe_df.csv',
        mime='text/csv',
    )
with tab2:
    st.header("Store")
    cont1 = st.container()

    with cont1:

        st.subheader("Input Information")
        CustomerSoldToStore = st.text_input(
            "CustomerSoldTo", "input value", key="CustomerSoldToStore")
        OriginalStoreCode = st.text_input(
            "OriginalStoreCode", "input value", key="OriginalStoreCode")
        StoreName = st.text_input(
            "StoreName", "input value", key="StoreName")
        Channel = st.selectbox("Channel", ("Digital",
                                            "Brick and Mortar",
                                            "Catalogs"),
                                            key="Channel")
        KTZ = st.selectbox("KTZ", ("Yes",
                                    "No",),
                                    key="KTZ")
        State = st.text_input(
            "State", "input value", key="State")
        City = st.text_input(
            "City", "input value", key="City")
        if "dfStore" not in st.session_state:
            st.session_state.dfStore = pd.DataFrame(columns=["CustomerSoldTo",
                                                        "OriginalStoreCode",
                                                        "StoreName",
                                                        "Channel",
                                                        "KTZ",
                                                        "State",
                                                        "City"])
        num_new_rows_store = st.sidebar.number_input("Add Rows To Table Store", 1, 500)
        ncol_campaign = st.session_state.dfStore.shape[1]  # col count
        rw_store = -1
        rwdta_campaign = []
        if "num_new_rows_store" not in st.session_state:
            st.session_state.num_new_rows_store = num_new_rows_store
        if "ncol_campaign" not in st.session_state:
            st.session_state.ncol_campaign = ncol_campaign
        if "rw_store" not in st.session_state and "rwdta_campaign" not in st.session_state:
            st.session_state.rw_store = rw_store
            st.session_state.rwdta_campaign = rwdta_campaign

    col1, col2, col3 = st.columns(3)
    with col2:
        Attach_button_store = st.button("Attach File Store", use_container_width=True)
    cont3 = st.container()

    with cont3:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col2:
            edit_button_store = st.button("Edit Store", use_container_width=True)
        with col3:
            Delete_button_store = st.button("Delete Store", use_container_width=True)
        with col4:
            save_button_store = st.button("Save Store", use_container_width=True)
    rwdta_campaign = [value for value in st.session_state.dfStore.columns]
    if st.button("Add Store", use_container_width=True):
        if st.session_state.dfStore.shape[0] == num_new_rows_store:
            st.error("Add row limit reached. Cant add any more records..")
        else:
            dfStore = st.session_state.dfStore
            rw = st.session_state.dfStore.shape[0] + 1
            st.info(f"Row: {rw_store} / {num_new_rows_store} added")
            #st.session_state.df.loc[rw] = rwdta
            num_new_rows_store = {
                "CustomerSoldTo": st.session_state.CustomerSoldTo,
                "OriginalStoreCode": st.session_state.OriginalStoreCode,
                "StoreName": st.session_state.StoreName,
                "Channel": st.session_state.Channel,
                "KTZ": st.session_state.KTZ,
                "State": st.session_state.State,
                "City": st.session_state.City,
            }
            st.session_state.dfStore = pd.concat([dfStore,
                                                  pd.DataFrame(num_new_rows_store, index=[rw_store])],
                                                  ignore_index=True)
            if st.session_state.dfStore.shape[0] == num_new_rows_store:
                st.error("Add a row, limit reached...")

    st.dataframe(st.session_state.dfStore)

    @st.cache_data
    def convert_df_store(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    csv_store = convert_df_store(st.session_state.dfStore)

    st.download_button(
        label="Download data as CSV",
        data=csv_store,
        file_name='dataframe_store.csv',
        mime='text/csv',
    )
with tab3:
    st.header("Campaign")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    cont1 = st.container()

    with cont1:

        st.subheader("Input Information")
        CampaignName = st.text_input(
            "CampaignName", "input value", key="CampaignName")
        CampaingnStartDate = st.text_input(
            "CampaingnStartDate", "input value", key="CampaingnStartDate")
        CampaignEndName = st.text_input(
            "CampaignEndName", "input value", key="CampaignEndName")
        ArticleCode = st.text_input(
            "ArticleCode", "input value", key="ArticleCode")
        if "dfCampaign" not in st.session_state:
            st.session_state.dfCampaign = pd.DataFrame(columns=["CampaignName",
                                                        "CampaignStartDate",
                                                        "CampaingEndDate",
                                                        "ArticleCode",])
        num_new_rows_campaign = st.sidebar.number_input("Add Rows To Table Campaign", 1, 500)
        ncol_campaign = st.session_state.dfCampaign.shape[1]  # col count
        rw_campaign = -1
        rwdta_campaign = []
        if "num_new_rows_campaign" not in st.session_state:
            st.session_state.num_new_rows_campaign = num_new_rows_campaign
        if "ncol_campaign" not in st.session_state:
            st.session_state.ncol_campaign = ncol_campaign
        if "rw_campaign" not in st.session_state and "rwdta_campaign" not in st.session_state:
            st.session_state.rw_campaign = rw_campaign
            st.session_state.rwdta_campaign = rwdta_campaign

    col1, col2, col3 = st.columns(3)
    with col2:
        Attach_button_campaign = st.button("Attach File Campaign", use_container_width=True)
    cont3 = st.container()

    with cont3:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col2:
            edit_button_campaign = st.button("Edit Campaign", use_container_width=True)
        with col3:
            Delete_button_campaign = st.button("Delete Campaign", use_container_width=True)
        with col4:
            save_button_campaign = st.button("Save Campaign", use_container_width=True)
    rwdta_campaign = [value for value in st.session_state.dfCampaign.columns]
    if st.button("Add campaign", use_container_width=True):
        if st.session_state.dfCampaign.shape[0] == num_new_rows_campaign:
            st.error("Add row limit reached. Cant add any more records..")
        else:
            dfCampaign = st.session_state.dfCampaign
            rw = st.session_state.dfCampaign.shape[0] + 1
            st.info(f"Row: {rw_campaign} / {num_new_rows_campaign} added")
            #st.session_state.df.loc[rw] = rwdta
            num_new_rows_campaign = {
                "CampaignName": st.session_state.CampaignName,
                "CampaignStartDate": st.session_state.CampaignStartDate,
                "CampaignEndDate": st.session_state.CampaignEndDate,
                "ArticleCode": st.session_state.ArticleCode,
            }
            st.session_state.dfCampaign = pd.concat([dfCampaign,
                                                  pd.DataFrame(num_new_rows_campaign, index=[rw_campaign])],
                                                  ignore_index=True)
            if st.session_state.dfCampaign.shape[0] == num_new_rows_campaign:
                st.error("Add a row, limit reached...")

    st.dataframe(st.session_state.dfCampaign)

    @st.cache_data
    def convert_df_campaign(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    csv_campaign = convert_df_campaign(st.session_state.dfCampaign)

    st.download_button(
        label="Download data as CSV",
        data=csv_campaign,
        file_name='dataframe_campaign.csv',
        mime='text/csv',
    )

with tab4:
    st.header("Target")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
