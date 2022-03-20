import streamlit as st
import matplotlib.pyplot as plt
import json
import os  # +Deployment
import inspect  # +Deployment


@st.cache
def load_image(cdir, link):
    return plt.imread(os.path.join(cdir, link))


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def app():

    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))

    st.subheader("Conclusion")
    st.write("This project has been the opportunity to apply many Data Science techniques & methodologies that we learnt during the training. We had to address typical data scientist challenges like hyper parameter tuning, data cleaning, app deployment...")
    st.write("This use case enables us to learn new tools (Geographic Information System like QGIS) and data types (Raster and Shapefile). The objective of the business case has been achieved with good performance metrics and calculation time.")

    st.subheader("Limitations and future developments")
    st.write("To improve the performance of the model, the training data could be enriched to include other types of lands and vegetations. Eventhough, the model has been trained on California and Portugal database, there could be a bias of these biomes. Moreover, some techniques to improve the quality of the input images could be implemented (better identification of the containment date used to request Google Earth Engine, computer vision methods to manage the presence of snow and fire plumes...)")
    st.write(
        "The model architecture could also be adapted to include attention mecanism.")
    st.write("Finally, the images from other satellites could be used. The active sensors (radar) have the ability to gather land information even when the weather is cloudy or contaminated with fire plumes. The geostationay satellite could add interesting data by staying above a target while Sentinel 2 satellites have a small temporal resolution (few days between 2 flyovers above the same spot).")
