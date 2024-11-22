import streamlit as st, pandas as pd
from data import data_prep, product_data,supplier_data,category_data,op_data,department_data
from max_chart import products_chart,op_chart,supplier_chart,category_chart,department_chart
from chart import product_chart,prod_chart,productWeeklyChart
from connection import LoadData

  

from chart import main_chart
st.set_page_config(page_title="RW Sale", layout="wide")

st.markdown("""
        <style>
            .block-container{padding-top: 12px;}
          
        </style>        
    """,
    unsafe_allow_html=True)  


# Define the main function
def main():
    col1, col2, col3 = st.columns([17,5,78])
    with col1:
        st.image('assets/images/rw.jpg', width=150)
    with col3:
        st.markdown("<h1 style='font-family:BROADWAY;color:#b62f2f'>RIGHTWAY WHOLESALE</h1>",unsafe_allow_html=True)
    
    st.sidebar.markdown("## :blue[RW Sale Analysis]")
    martEda=st.sidebar.checkbox('Mart Overall EDA')
    maxEda=st.sidebar.checkbox('Top Trends EDA')
    ProductEda=st.sidebar.checkbox('Product EDA')
    st.sidebar.markdown("## :blue[Upload Data]")
    
    dfa=LoadData()
    
              
    if martEda:
        maxEda=False
        productEda=False
        st.markdown("## :green[Overall Mart Sale Analysis]")
        chart=main_chart(dfa)
        st.plotly_chart(chart)
        
    elif maxEda:
        martEda=False
        productEda=False
        st.markdown("## :green[Top Trends of Various Disciplines]")
        df24=dfa[dfa['year']==2024]
        productData=product_data(df24)
        productChart=products_chart(productData)
        st.pyplot(productChart)
        opData=op_data(df24)
        opChart=op_chart(opData)
        st.pyplot(opChart)            
        depData=department_data(df24)
        depChart=department_chart(depData)
        st.pyplot(depChart)
        catData=category_data(df24)
        catChart=category_chart(catData)
        st.pyplot(catChart)
        supData=supplier_data(df24)
        supChart=supplier_chart(supData)
        st.pyplot(supChart)
        
        
    elif ProductEda:
        maxEda=False
        martEda=False
        st.markdown('## :green[Products Sale Analysis]')
        df=dfa
        products=df['Description'].unique()
        selected_product=st.selectbox('Select a product',products,format_func=lambda x:x ,placeholder='search product')
        if selected_product:
            dfb=df[df['Description']==selected_product]
            year_list=dfb['year'].unique()
            col1,col2=st.columns(2)
            with col1:
                currentYear=st.selectbox('select current year',year_list)
            with col2:
                previousYear=st.selectbox('select previous year',year_list)
                
            # st.markdown("#### :blue[Monthly Product Sale Analysis ]")
            dfYear=dfb.groupby('year')[['QTY','CP','Value']].sum().reset_index()
            dfCYear=dfb[dfb['year']==currentYear]
            dfCy=dfCYear.groupby('year_month')[['QTY','Value']].sum().reset_index()
            
            
            if currentYear==previousYear:
                heading=f"<h4 style='color:green;'>Sale During {previousYear}</h4>"
            else:
                heading=f"<h4>Sale During {previousYear} & {currentYear}</h4>"
            st.markdown(heading,unsafe_allow_html=True)
                
            col1,col2=st.columns([30,70])
            with col1:                    
                
                st.dataframe(dfYear,hide_index=True)
            with col2:
                chart=product_chart(df,selected_product)
                st.plotly_chart(chart)
                
            st.markdown("### :green[Monthly Comparison of Sales]")
            
            try:
                prodChart=prod_chart(dfa,currentYear,previousYear,selected_product)
                st.plotly_chart(prodChart)
            except:
                st.write('Current and previous years should not be same')
            
            st.markdown(f"<h4 style='color:green'>Weekly Product Sale During {currentYear}</h4>",unsafe_allow_html=True)
            dfa=df[(df['Description']==selected_product)&(df['year']==currentYear)]
            
            dfc=dfa.groupby('Week')[['QTY','Value']].sum().reset_index()
            dfc['Accu-QTY']=dfc['QTY'].cumsum()
            dfc['Accu-Value']=dfc['Value'].cumsum()
            
            colA,colB=st.columns([40,60])
            with colA:
                st.dataframe(dfc,hide_index=True)
            with colB:
                WChart=productWeeklyChart(dfc,selected_product)
                st.plotly_chart(WChart)
            
        
        
if __name__=='__main__':
    main()