import streamlit as st 
import os                      #+Deployment
import inspect                 #+Deployment

def app():

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    st.image(os.path.join(currentdir, 'ressources/banner.jpg'))
