import pandas as pd,numpy as np, streamlit as st
import seaborn as sns, matplotlib.pyplot as plt
import LoadData
#import data
  
df=pd.read_csv('TransDetails_Max.csv')
df_24=df[df['year']==2024]
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
    