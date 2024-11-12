import streamlit as st,pandas as pd
from max_data import supplier_data,op_data,category_data,department_data,product_data
from max_chart import supplier_chart,op_chart,department_chart,category_chart,product_chart
# Define the main function
def app():
    st.markdown('### :blue[Top Trends During 2024]')
    df=pd.read_csv('TransDetails_Max.csv')
    df24=df[df['year']==2024]
    
    
    productData=product_data(df24)
    chart_product=product_chart(productData)
    st.pyplot(chart_product)
    
    
    opData=op_data(df24)
    chart_op=op_chart(opData)
    st.pyplot(chart_op)
    

    depData=department_data(df24)
    chart_dep=department_chart(depData)
    st.pyplot(chart_dep)
    
    
    catData=category_data(df24)
    chart_cat=category_chart(catData)
    st.pyplot(chart_cat)
    
    
    supData=supplier_data(df24)
    chart_sup=supplier_chart(supData)
    st.pyplot(chart_sup)