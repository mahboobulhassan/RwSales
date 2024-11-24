import pandas as pd,numpy as np



def data_prep(dfa):
    dfa.rename(columns={'Date_':'Date'},inplace=True)
    dfa['Date']=pd.to_datetime(dfa['Date'],format='mixed')
    dfa['year_month']=dfa['Date'].dt.strftime('%Y-%m')
    dfa['year']=dfa['Date'].dt.year
    dfa['Month']=dfa['Date'].dt.month
    dfa['Week']=dfa['Date'].dt.strftime("%U")
    dfa['Month']=pd.to_numeric(dfa['Month'])
    dfa['Value']=np.round(dfa['Value'],0)
    dfa['CP']=np.round(dfa['CP'],0)
    return dfa
def data(conn, sDate, eDate):
    query = f"SELECT Date_, Description, Department, Category, OP, Supplier_Name, CP, QTY, Value FROM Trans_Details WHERE TRY_CONVERT(DATE, Date_) BETWEEN '{sDate}' AND '{eDate}'"
    dfa = pd.read_sql_query(query, conn)
    df = data_prep(dfa)
    return df
def supplier_data(df24):
    df_supplier=df24[['Supplier_Name','CP']]
    dfa_supplier=df_supplier.groupby('Supplier_Name')['CP'].sum().reset_index().sort_values(by='CP',ascending=False).head(10)
    return dfa_supplier
def op_data(df24):
    df_op=df24[['OP','QTY']]
    dfa_op=df_op.groupby('OP')['QTY'].sum().reset_index().sort_values(by='QTY',ascending=False).head(10)
    return dfa_op
def category_data(df24):
    df_category=df24[['Category','Value']]
    dfa_category=df_category.groupby('Category')['Value'].sum().reset_index().sort_values(by='Value',ascending=False).head(10)
    return dfa_category
def department_data(df24):
    df_department=df24[['Department','Value']]
    dfa_department=df_department.groupby('Department')['Value'].sum().reset_index().sort_values(by='Value',ascending=False).head(10)
    return dfa_department
def product_data(df24):
    df_department=df24[['Description','QTY']]
    dfa_department=df_department.groupby('Description')['QTY'].sum().reset_index().sort_values(by='QTY',ascending=False).head(30)
    return dfa_department



    
    