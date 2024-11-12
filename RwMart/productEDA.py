import streamlit as st,pandas as pd, numpy as np
from dbs_con import connect_to_sql
from data import Data
from chart import prod_chart,product_chart




def load_data():
    conn=connect_to_sql()
    data=Data(conn)
    return data
    
def app():
    st.markdown('## :green[Product Sale Analysis]')
    df=pd.read_csv('TransDetails_EDA.csv')
    list=df['Description'].unique() 
    products=np.sort(list)
    selected_product=st.selectbox('Select a product',products,format_func=lambda x:x ,placeholder='search product')
    st.markdown("#### :blue[Product Sale For 2023 & 2024 ]")
    dfb=df[df['Description']==selected_product]   
    dft=dfb.groupby('year')[['QTY','CP','Value']].sum().reset_index()
    df2024=dfb[dfb['year']==2024]
    df24=df2024.groupby('year_month')[['QTY','Value']].sum().reset_index()
    df24_max=df24.sort_values(by='Value',ascending=False).head(3)
    df24_min=df24.sort_values(by='Value',ascending=True).head(3)
    with st.container():
        col1,col2,col3=st.columns(3)
        with col1:
            st.markdown('##### :blue[Sale During 2023 & 2024]')
            st.dataframe(dft,hide_index=True)
        with col2:
            st.markdown('##### :blue[Max Sale During 2024]')
            st.dataframe(df24_max, hide_index=True)
        with col3:
            st.markdown('##### :blue[Min Sale During 2024]')
            st.dataframe(df24_min,hide_index=True)
    
    chart=product_chart(df,selected_product)
    st.plotly_chart(chart)
    labelD=st.markdown("##### :blue[]")
        
    st.markdown("#### :blue[Monthly Comparison of Sales]")
    year_list=df['year'].unique()
    col1,col2=st.columns(2)
    with col1:
        currentYear=st.selectbox('select current year',year_list)
    with col2:
        previousYear=st.selectbox('select previous year',year_list)
    try:
        prodChart=prod_chart(df,currentYear,previousYear,selected_product)
        st.plotly_chart(prodChart)
    except:
        st.write('Current and previous years should not be same')

    
    