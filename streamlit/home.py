import streamlit as st 
import os                      #+Deployment
import inspect                 #+Deployment


def app():

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    st.title("FirePy")
    st.header("This project was made out as part of training course at Datascientest.com (Data Scientist program June '21) ")
    st.write("\n\n")  
    st.write(
    "Manual surveying of fire perimeters is a tedious and tiring task and subject to human error. The level could be limited due to pockets spared by the flames found inside the fire zones."
    "\n\n"    
    "The automation of the detection of burnt surfaces by an algorithm would make it possible to lighten the human workload, to bring robustness to the analysis and to scale the analysis area and would make it possible to provide a preliminary estimate of damage (natural, property, infrastructure). Mathematical processing of satellite images is also a way to go beyond burnt/unburnt binary information and refine the burn level."
     "\n\n"
    "Traditional burn area detection methods have limited performance. By operating using thresholds, it is difficult for these techniques to detect small burned areas or low intensity burns. Some algorithms based on anomaly detection on the neighborhood of pixels have a high rate of false detection. Finally, methods exploiting differences in image sequences over time have the disadvantage of requiring a lot of data. Faced with this observation, deep learning algorithms seem particularly promising and are the subject of numerous research and publications."
    "\n\n"
    "The good availability of data from the Sentinel 2 satellites financed by ESA's Copernicus program is an essential asset for the launch of the project. Indeed, the images are available free of charge and have covered a large part of the earth's surface since 2015."
    "\n\n"
    "This is the objective of our project.", unsafe_allow_html=True) 
    st.image(os.path.join(currentdir, 'ressources/image12.png'))
