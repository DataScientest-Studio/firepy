import streamlit as st 

import os                      #+Deployment
import inspect                 #+Deployment
import home
import dataset
import prediction
import credits
import home


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

logo = os.path.join(currentdir, 'ressources/logo_fire.png')
PAGE_CONFIG = {"page_title":"Firepy","page_icon": logo,"layout":"wide"}
st.set_page_config(**PAGE_CONFIG)

MENU_ = {
    "Home" : home,
    "Dataset" : dataset,
    "Prediction" : prediction,
    "Credits" : credits
}

st.sidebar.title('Menu')
selection_page = st.sidebar.radio("",list(MENU_.keys()))
page = MENU_[selection_page]
page.app()
