import streamlit as st
from streamlit_option_menu import option_menu

# Import Pages
from Home import app as home_page
from Dataset import app as dataset_page
from EDA import app as eda_page
from Prediction import app as prediction_page
from Model_performance import app as model_page
from About import app as about_page

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="House Rent Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.image(
        "https://th.bing.com/th/id/OIP.jtM285Is-cdlz3CCKOpvMAHaFj?w=245&h=184&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        width=210
    )

    st.title("House Rent AI")

    selected = option_menu(

        menu_title="",

        options=[
            "Home",
            "Dataset",
            "EDA",
            "Prediction",
            "Model Performance",
            "About"
        ],

        icons=[
            "house",
            "table",
            "bar-chart",
            "robot",
            "graph-up",
            "info-circle"
        ],

       

        default_index=0,

        styles={
            "container":{
                "padding":"5!important",
                "background-color":"#fafafa"
            },

            "icon":{
                "color":"orange",
                "font-size":"18px"
            },

            "nav-link":{
                "font-size":"16px",
                "text-align":"left",
                "margin":"0px",
                "--hover-color":"#eee"
            },

            "nav-link-selected":{
                "background-color":"#1565C0"
            }
        }
    )


# ----------------------------------------------------
# Routing
# ----------------------------------------------------

if selected=="Home":
    home_page()

elif selected=="Dataset":
    dataset_page()

elif selected=="EDA":
    eda_page()

elif selected=="Prediction":
    prediction_page()

elif selected=="Model Performance":
    model_page()

elif selected=="About":
    about_page()