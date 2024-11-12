import streamlit as st, pandas as pd
from data import Data, max_data
from dbs_con import connect_to_sql
from sqlalchemy import create_engine
import time
# from globals import globals

def establish_connection(server):
    
    if server=='DESKTOP-QEH9V2R\\SQLEXPRESS':
        database='TransDetails'
        password=""
        username=""
        engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
        conn=engine.connect()
    else:
        database='smsDB'
        password="ITpro99_"
        username="sa"
        engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
        conn=engine.connect()
    
    return conn
def progressBar():
    progress_bar = st.progress(0,text="Loading......")  # Initialize the progress bar
                # Simulating data loading
    for percent_complete in range(1, 101):
        time.sleep(3.4)  # Simulating data loading time
        text='Loading data ......'
        progress_bar.progress(percent_complete,text=text)
        # Clear the progress bar once loading is complete
    progress_bar.empty()
    return progress_bar

# Define the main function
def app():
    st.markdown('#### :blue[Load Data From Server]')
      
    server=st.text_input('Enter server name')
        
    # Change the button color by setting the beta_color parameter
    
    st.markdown("""
                <style>
                    button{background-color: #4CAF50;
                    color:#fff;
                    border-radius:20px;
                    cursor:pointer;}
                </style>
                """, 
                unsafe_allow_html=True)
    
    loadData=st.button('Load data')
    if loadData:
        try:
            conn=establish_connection(server)
            if conn:
                st.write('Connected Successfully')                       
                progressBar()            
                df= Data(conn)
                #df.to_csv('TransDetails_EDA.csv', encoding='utf-8')
                maxData=max_data(conn)
                #maxData.to_csv('TransDetails_Max.csv', encoding='utf-8')
                st.write('Data loaded successfully')
                                
        except:
            st.write('Connection failed')
    
    

    
    



