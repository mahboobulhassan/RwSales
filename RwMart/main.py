import streamlit as st
from dbs_con import connection
from streamlit_option_menu import option_menu
import productEDA,martEda,maxEda,LoadData

# Define the main function
def main():
    col1, col2, col3 = st.columns([17,5,78])
    with col1:
        st.image('rw.jpg', width=150)
    with col3:
        st.markdown("<h1 style='font-family:BROADWAY;color:#b62f2f'>RIGHTWAY WHOLESALE</h1>",unsafe_allow_html=True)
    st.markdown("""
        <style>
            .block-container{padding-top: 30px;}
        </style>        
    """,
    unsafe_allow_html=True)      
    
    with st.sidebar:
        st.markdown("<p style='color:green;text-align:center;font-size:30px;font-family:stencil'>RW SALES<p>",unsafe_allow_html=True)
        app=option_menu(
            menu_title='',
            options=['♻️ Load Data','📊 Mart EDA', '📊 Product EDA', '📈 Top Trends'],
            icons=['h','h','h','h'],
            menu_icon=[""],
            default_index=0,
            styles={"container":{'background-color':'black','padding':'20px','margin-top':'0px'},
                    "icon":{'color':'white','font-size':'15px'},
                    "nav-link":{'color':'white','font-size':'15px'},
                    "nav-link-selector":{'background-color':'red'},
                    "menu-title":{'color':'white','padding':'10px','border-radius':'5px','font-size':'23px','font-weight':'bold','background-color':'blue'},
                    
                   }                 
        )
    if app=='♻️ Load Data':
        LoadData.app()    
    if app=='📊 Mart EDA':
        martEda.app()
    if app=='📊 Product EDA':
        productEDA.app()    
    if app=='📈 Top Trends':
        maxEda.app()
    
        
        pass
if __name__=='__main__':
    main()