import pandas as pd,numpy as np
from dbs_con import connection, connect_to_sql
from sqlalchemy import text


def data_prep(df):
    dfa=df.copy()
    dfa.rename(columns={'Date_':'Date'},inplace=True)
    dfa['Date']=pd.to_datetime(dfa['Date'],format='mixed')
    dfa['year_month']=dfa['Date'].dt.strftime('%Y-%m')
    dfa['year']=dfa['Date'].dt.year
    dfa['Month']=dfa['Date'].dt.month
    dfa['Month']=pd.to_numeric(dfa['Month'])
    dfa['Value']=np.round(dfa['Value'],0)
    dfa['CP']=np.round(dfa['CP'],0)
    return dfa
def Data(conn):
    query = text("SELECT Date_,Description,QTY,Value,CP FROM Trans_Details Where Date_>='2023-01-01' AND Date_<='2025-12-31' ")
    pdf=pd.read_sql_query(query,con=conn)
    df=data_prep(pdf)
    return df
def max_data(conn):
    query = text("SELECT Date_,Description,Supplier_Name,Department,Category,OP,QTY,Value,CP FROM Trans_Details Where Date_>='2023-01-01' AND Date_<='2025-12-31'")
    pdf=pd.read_sql_query(query,con=conn)
    df=data_prep(pdf)
    return df


    
    