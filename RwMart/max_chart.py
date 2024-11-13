import pandas as pd,numpy as np
import seaborn as sns, matplotlib.pyplot as plt
from max_data import supplier_data,op_data,category_data,department_data,product_data

def chart(data,x,y,title,h,fs):
    sns.set_theme()
    plt.figure(figsize=(12, h))
    ax=sns.barplot(data=data,x=x, y=y)
    ax.bar_label(ax.containers[0],fontsize='9')
    plt.title(title,fontsize=fs,fontweight='bold')
    plt.xticks(fontsize='9')
    plt.yticks(fontsize='9')
    return plt.gcf()
def op_chart(data):    
    x='QTY'; y='OP'; h=3; fs='20'
    title='Top Ten Salesmen'
    fig=chart(data,x,y,title,h,fs)
    return fig
def department_chart(data):
    x='Value'; y='Department'; h=3; fs='20'
    title='Top Ten Departments'
    fig=chart(data,x,y,title,h,fs)
    return fig
def category_chart(data):
    x='Value'; y='Category'; h=3 ; fs='20'
    title='Top Ten Categories'
    fig=chart(data,x,y,title,h,fs)
    return fig
def product_chart(data):
    x='QTY';  y='Description'; h=9; fs='28'
    title='Top 30 Products'
    fig=chart(data,x,y,title,h,fs)
    return fig
def supplier_chart(data):
    x='CP'; y='Supplier_Name'; h=3;  fs='20'
    title='Top Ten Supplier'
    fig=chart(data,x,y,title,h,fs)
    return fig