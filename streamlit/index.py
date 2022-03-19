import streamlit as st

import os  # +Deployment
import inspect  # +Deployment
import home
import dataset
import prediction
import about
import conclusion
import home
import streamlit.components.v1 as components

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

logo = os.path.join(currentdir, 'ressources/logo_fire.png')
PAGE_CONFIG = {"page_title": "Firepy", "page_icon": logo, "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)

MENU_ = {
    "Home": home,
    "Dataset": dataset,
    "Prediction": prediction,
    "About": about,
    "Conclusion": conclusion
}

st.sidebar.title('Menu')
selection_page = st.sidebar.radio("", list(MENU_.keys()))

st.sidebar.title('Credits')

st.sidebar.write(
    "[Emmanuelle CANO ](https://www.linkedin.com/in/emmanuelle-cano-4b845940/)")
st.sidebar.write(
    "[François FAUPIN](https://www.linkedin.com/in/francois-faupin/)")
st.sidebar.write("[Thomas GOSSART](https://www.linkedin.com/in/gossartt/)")
st.sidebar.write("Mentor :")
st.sidebar.write("[Pierre ADEIKALAM](https://www.linkedin.com/in/data-jesus/)")

st.sidebar.title('Github')
st.sidebar.write("[FirePy](https://github.com/DataScientest-Studio/firepy)")
page = MENU_[selection_page]
page.app()
