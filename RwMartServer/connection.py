import pyodbc,datetime
import pandas as pd,streamlit as st
from sqlalchemy import create_engine
from data import data, data_prep

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
        time.sleep(2.5)  # Simulating data loading time
        text='Loading data ......'
        progress_bar.progress(percent_complete,text=text)
        # Clear the progress bar once loading is complete
    
    progress_bar.empty()
    return progress_bar

# Define the main function
def LoadData():
    sList=['DESKTOP-QEH9V2R\SQLEXPRESS','192.168.1.200']    
    server = st.sidebar.selectbox('Select server name',sList)
    
    if server:
        try:
            conn = establish_connection(server)
            try:            
                sDate=st.sidebar.text_input('Enter Start Date',value=20230101)
                eDate=st.sidebar.text_input("Enter End date", value=20241030)
                if sDate and eDate:
                    df=data(conn,sDate,eDate)            
                    return df
                    
            except:
                st.error('Please enter valid DATES') 
        except Exception as e:
            st.error('Please enter valid server name',e)   
    
        
            
       
    
