import pyodbc
import pandas as pd
from sqlalchemy import create_engine


def connection():
    server='DESKTOP-QEH9V2R\\SQLEXPRESS'
    database='TransDetails'
    conn_str=(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER='+server+';'
        r'DATABASE='+database+';'
        r'TRUSTED_CONNECTION=yes;'
    )
    try:
        conn = pyodbc.connect(conn_str)
                
    except pyodbc.Error as ex:
        ('Error Connecting to SQLSERVER',ex)
    return conn

def connect_to_sql():
    server='DESKTOP-QEH9V2R\\SQLEXPRESS'
    database='TransDetails'
    password=""
    username=""
    # engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
    engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
    conn=engine.connect()    
    return conn
# def con():
#     import pymssql
#     server='DESKTOP-QEH9V2R'
#     database='TransDetails'
#     password=""
#     user=""
#     conn = pymssql.connect(server, user, password, database)
#     return conn

    
