import pandas as pd, streamlit as st,calendar
import plotly.graph_objects as go, plotly.express as px
from data import Data
# import data

def main_chart(df):
    dfc=df.groupby(['year_month'])[['Value','CP']].sum().reset_index()
    # plotly chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dfc['year_month'], y=dfc['Value'], mode='lines', name='Price',line_color='green',fill='tonexty'))
    fig.add_trace(go.Scatter(x=dfc['year_month'], y=dfc['CP'], mode='lines', name='Cost',line_color='red',fill='tozeroy'))
    fig.update_layout(title={'text':'Cost & Price Distribution During 2023 & 2024','x':0.1,'y':.95},
                      xaxis_title='Year-Month', yaxis_title='Amount',hovermode='x',
                      legend=dict(yanchor='top',y=0.95,xanchor='left',x=0.85),
                      plot_bgcolor='white',paper_bgcolor='#f5f5f5',
                      margin=dict(l=50,r=20,t=50,b=50))
    fig.update_traces(hovertemplate=None)
    return fig

def product_chart(pdf,product):
    dfa=pdf[pdf['Description']==product]
    dfc=dfa.groupby('year_month')[['QTY']].sum().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dfc['year_month'], y=dfc['QTY'], mode='lines', name='Price',line_color='green'))
    fig.update_layout(title={'text':product,'x':0.1,'y':.95},
                      xaxis_title='Year-Month', yaxis_title='Quantity',hovermode='x',
                      legend=dict(yanchor='top',y=0.95,xanchor='left',x=0.85),
                      plot_bgcolor='white',paper_bgcolor='#edf2f7',
                      margin=dict(l=50,r=20,t=50,b=50),
                      height=300)
    fig.update_traces(hovertemplate=None)
    return fig
def prod_chart(df,currentYear,previousYear,product):
    # Data preparation
    dfa=df[df['Description']==product]
    dfb=dfa[dfa['year'].isin([currentYear,previousYear])]
    dfc=pd.pivot_table(data=dfb,index='Month',values='QTY',columns='year', aggfunc='sum').reset_index()
    dfc['Month']=dfc['Month'].map(lambda x :calendar.month_abbr[x])
    # create plotly chart 
    if currentYear not in dfc.columns:
        title=f"Sale for the year {previousYear} only"
        fig=go.Figure(data=[
        go.Bar(x=dfc['Month'],y=dfc[previousYear],text=dfc[previousYear])])
        fig.update_layout(
            title={'text':title,'x':0.5,'y':.95},
            margin=dict(l=50,r=50,t=50,b=50),
            xaxis_title='Month', yaxis_title='Quantity',
            height=300,
            plot_bgcolor='white',paper_bgcolor='#edf2f7')
        
    elif previousYear not in dfc.columns:
        title=f"Sale for the year {currentYear} only"
        fig=go.Figure(data=[
        go.Bar(x=dfc['Month'],y=dfc[currentYear],text=dfc[currentYear])]) 
        fig.update_layout(
            title={'text':title,'x':0.5,'y':.95},
            margin=dict(l=50,r=50,t=50,b=50),
            plot_bgcolor='white',paper_bgcolor='#edf2f7',
            xaxis_title='Month', yaxis_title='Quantity',
            height=300,)
        fig.update_traces(marker_color='blue')
        
    else:
        title=f"Comparison of Sale During {previousYear} and {currentYear}"    
        fig=go.Figure(data=[
        go.Bar(x=dfc['Month'],y=dfc[previousYear],text=dfc[previousYear],name=dfc.columns[1],marker_color=px.colors.qualitative.Dark24[19]),
        go.Bar(x=dfc['Month'],y=dfc[currentYear],text=dfc[currentYear],name=dfc.columns[2],marker_color=px.colors.qualitative.Dark24[2])])
        fig.update_layout(
            title={'text':title,'x':0.5,'y':.95},
            margin=dict(l=50,r=50,t=50,b=50),
            xaxis_title='Month', yaxis_title='Quantity',
            plot_bgcolor='white',paper_bgcolor='#edf2f7',
            height=300,)

        
        
    return fig






    
    
    
    