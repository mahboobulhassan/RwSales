import streamlit as st,pandas as pd
from chart import main_chart
from data import Data

# Define the main function

def app():
    df=pd.read_csv('data.csv')
    dfa=df.groupby('year')[['CP','Value']].sum().reset_index()
    df24=df[df['year']==2024]
    df2024=df24.groupby('year_month')[['QTY','Value']].sum().reset_index()
    df2024_max=df2024.sort_values(by='Value',ascending=False).head(3)
    df2024_min=df2024.sort_values(by='Value',ascending=True).head(3)    
    chart=main_chart(df)
    st.markdown('### :green[Mart Sale During 2023 & 2024]')
        
    with st.container():
        col1, col2, col3=st.columns(3)
        with col1:
            st.markdown('##### :blue[Sale During 2023 & 2024]')
            st.dataframe(dfa,hide_index=True)            
                   
        with col2:
            st.markdown('##### :blue[Max Sale During 2024]')
            st.dataframe(df2024_max,hide_index=True)
        with col3:
            st.markdown('##### :blue[Min Sale During 2024]')
            st.dataframe(df2024_min,hide_index=True)
        
        st.plotly_chart(chart)
        
            
        