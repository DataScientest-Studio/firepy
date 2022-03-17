# -*- coding: utf-8 -*-
"""
Script for the Streamlit demo of the FirePy project
"""

import folium  # map rendering library
import streamlit as st
from streamlit_folium import folium_static
import rasterio as rio
import tifffile
import numpy as np
import matplotlib.pyplot as plt
import appsession as session
import json
import os                      #+Deployment
import inspect                 #+Deployment
from pyproj import Proj, transform
import tensorflow as tf
from smooth_blending import predict_img_with_smooth_windowing
from unet_model import simple_unet_model


def main():
    state = session._get_state()
    pages = {
        "Firepy Project": page_dashboard,
        "Datasets": page_datasets,
        "Prédiction (démo)": page_demo,
    }
    st.sidebar.title("FirePy")
    st.sidebar.subheader("Menu") 
    page = st.sidebar.radio("", tuple(pages.keys()))
    pages[page](state)
    state.sync()
    st.sidebar.info(
        "Projet DS - Promotion Juin 2021"
        "\n\n"
        "Participants:"
        "\n\n"
        " Emmanuelle CANO, François FAUPIN, Thomas GOSSART"
        "\n\n"
        )

# ######################################################################################################################
# page HOME
# ######################################################################################################################

def page_dashboard(state):
    st.title("FirePy")
    st.header("Ce projet a été réalisé dans le cadre de la formation Data Scientist de Datascientest (promotion continue Juin 2021)")
    st.write("\n\n")  
    st.write(
    "Le relevé manuel des périmètres de feu est une tâche fastidieuse et sujette à erreur humaine. Le niveau de détails obtenu est limité car des poches épargnées par les flammes peuvent se trouver à l’intérieur des zones de feu."
    "\n\n"    
    "L’automatisation de la détection de surfaces brûlées par un algorithme permettrait d’alléger la charge de travail humaine, d’apporter de la robustesse dans l’analyse et de passer à l’échelle la zone d’analyse et permettrait d’apporter un estimation préliminaire quant aux dégâts (naturels, les biens, les infrastructures). Le traitement mathématique des images satellites est aussi un moyen d’aller au-delà d’une information binaire brûlé / non brûlé et d’affiner le niveau de brûlure."
     "\n\n"
    "Les méthodes traditionnelles de détection de zones brûlées ont des performances limitées. En fonctionnant à l’aide de seuils, il est difficile pour ces techniques de détecter des petites zones brûlées ou des brûlures de faible intensité. Certains algorithmes basés sur la détection d'anomalie sur le voisinage de pixels ont un taux élevé de fausse détection. Enfin, les méthodes exploitant les différences dans les séquences d’image dans le temps ont l’inconvénient de nécessiter beaucoup de données. Face à ce constat, les algorithmes de deep learning semblent particulièrement prometteurs et font l’objet de nombreuses recherches et publications."
    "\n\n"
    "La bonne disponibilité des données des satellites Sentinel 2 financés par le programme Copernicus de l’ESA est un atout essentiel pour le lancement du projet. En effet, les images sont disponibles gratuitement et couvrent depuis 2015 une grande partie de la surface terrestre."
    "\n\n"
    "C’est tout l’objectif de notre projet.", unsafe_allow_html=True)  


# ######################################################################################################################
# page Datasets
# ######################################################################################################################
def page_datasets(state):
#===============================================================================
# Chargement d'une image
#===============================================================================
    @st.cache
    def load_image(cdir, link):
        return plt.imread(os.path.join(cdir, link))

    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def app():

        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
        st.subheader("Fire GALLERY")

        gallery_content = open(os.path.join(currentdir, 'ressources/gallery.json'))
        data  = json.load(gallery_content)

        for images_row in chunks(data['gallery']['images'], 3):
            c1, c2, c3 = st.beta_columns([1, 1, 1])
            if len(images_row)>=1: c1.image(load_image(currentdir, images_row[0]['image-link']), caption=images_row[0]['image-desc'], use_column_width='always') 
            if len(images_row)>=2: c2.image(load_image(currentdir, images_row[1]['image-link']), caption=images_row[1]['image-desc'], use_column_width='always') 
            if len(images_row)==3: c3.image(load_image(currentdir, images_row[2]['image-link']), caption=images_row[2]['image-desc'], use_column_width='always')


# ######################################################################################################################
# page PREDICTION
# ######################################################################################################################
def page_demo(state):
    select_fire_events = st.sidebar.selectbox(
        "Select a fire event",
        ("Fire_1", "Fire_2", "Fire_3")
    )

    sentinel2_opacity_slider = st.sidebar.slider(
        'Opacity of Sentinel 2 overlay', 0.0, 1.0, 1.0)

    if select_fire_events == "Fire_1": 
        st.title("Incendie n°1 :")
        st.write(" ")
        st.subheader("Incendie ayant eu lieu le XX/XX/XXXX")
        sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_185_postFire_RGBIR.tif'


    elif select_fire_events == "Fire_2": 
        st.title("Incendie n°2 :")
        st.write(" ")
        st.subheader("Incendie ayant eu lieu le XX/XX/XXXX")
        sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_321_postFire_RGBIR.tif'


    else :
        st.title("Incendie n°3 :")
        st.write(" ")
        st.subheader("Incendie ayant eu lieu le XX/XX/XXXX")
        sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_8351_postFire_RGBIR.tif'   

    # Sentinel 2 image path

    raster_sentinel2 = rio.open(sentinel2_image_path)

    # Bounding box
    inProj = Proj(init='epsg:32610')
    outProj = Proj(init='epsg:4326')
    longitude1, latitude1 = transform(
        inProj, outProj, raster_sentinel2.bounds.left, raster_sentinel2.bounds.bottom)
    longitude2, latitude2 = transform(
        inProj, outProj, raster_sentinel2.bounds.right, raster_sentinel2.bounds.top)
    gps_bounding_box = [longitude1, latitude1, longitude2, latitude2]

    bbox = [[gps_bounding_box[1], gps_bounding_box[0]],
            [gps_bounding_box[3], gps_bounding_box[2]]]

    # Array data
    arr = raster_sentinel2.read()

    # Normalize the data (divide par 10000)
    arr = arr / 10000

    # Change dimension order (number of channel at the end)
    arr = np.moveaxis(arr, 0, -1)

    # Selecting the RGB channels in the right order
    image_rgb = arr[:, :, :3]
    image_rgb = image_rgb[:, :, ::-1] * 10


    def predict(arr):
        # Loading a pre-trained model
        model = simple_unet_model(256, 256, 5)
        model.load_weights(
            './streamlit/saved_model/model_patches_20220130bis.hdf5')

        predictions_smooth = predict_img_with_smooth_windowing(
            arr,
            window_size=256,
            # Minimal amount of overlap for windowing. Must be an even number.
            subdivisions=2,
            nb_classes=1,
            pred_func=(
                lambda img_batch_subdiv: model.predict((img_batch_subdiv))
            )
        )
        return predictions_smooth[:, :, 0]


    # Adding the UI components for the user
    st.title("FirePy demo")

    zoom_slider = st.sidebar.slider(
        'Map zoom', 5.0, 15.0, 10.0)

    # Showing the map centered on San Jose GPS coordinates
    map_california = folium.Map(location=[34, -116.8],
                                zoom_start=zoom_slider)



    # Adding the Sentinel 2 image
    image = folium.raster_layers.ImageOverlay(
        name="Test image",
        image=image_rgb,
        bounds=bbox,
        interactive=True,
        zindex=1,
        opacity=sentinel2_opacity_slider
    )
    image.add_to(map_california)

    prediction_button = st.sidebar.button("Predict the burnt area")
    prediction_boolean = False
    if prediction_button:
        prediction_smooth_img = predict(arr)
        prediction_boolean = True
        st.session_state.prediction = prediction_smooth_img

    prediction_opacity_slider = st.sidebar.slider(
        'Opacity of the prediction overlay', 0.0, 1.0, 0.5)

    if 'prediction' in st.session_state:
        saved_result = st.session_state.prediction
        # Adding the prediction image
        image_prediction = folium.raster_layers.ImageOverlay(
            name="Prediction image",
            image=saved_result,
            bounds=bbox,
            interactive=True,
            zindex=2,
            opacity=prediction_opacity_slider
        )
        image_prediction.add_to(map_california)

    # Display the map
    folium_static(map_california)    


    
if __name__ == '__main__':
    main()
