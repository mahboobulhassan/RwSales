import pyodbc
import pandas as pd
from sqlalchemy import create_engine

def connect_to_sql():
    server='DESKTOP-QEH9V2R\\SQLEXPRESS'
    database='TransDetails'
    password=""
    username=""    
    engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
    conn=engine.connect()    
    return conn


    
