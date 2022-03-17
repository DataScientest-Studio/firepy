# -*- coding: utf-8 -*-
"""
Script for the Streamlit demo of the FirePy project
"""

import folium  # map rendering library
import streamlit as st
from streamlit_folium import folium_static
import rasterio as rio
import tifffile
import os
import inspect
import numpy as np
from pyproj import Proj, transform
import tensorflow as tf
from smooth_blending import predict_img_with_smooth_windowing
from unet_model import simple_unet_model


def app():

    # Adding the title
    st.title("FirePy demo")

    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))

    # Adding a drop down menu
    select_fire_events = st.sidebar.selectbox(
        "Select a fire event",
        ("Apple fire 2020-07-31", "Airport fire 2022-02-16"),
        index=1
    )

    # Adding a Sentinel 2 opacity slider
    sentinel2_opacity_slider = st.sidebar.slider(
        'Opacity of Sentinel 2 overlay', 0.0, 1.0, 1.0)

    # Selectig the desired data
    if select_fire_events == "Apple fire 2020-07-31":
        st.image(os.path.join(currentdir, 'ressources/apple_fire_d.jpg'))
        st.markdown(f'''<a href="https://www.fire.ca.gov/incidents/2020/7/31/apple-fire/" style="text-decoration: none;color:64a5c3">Click here for complete status</a>''', unsafe_allow_html=True)
        sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_185_postFire_RGBIR.tif'

    elif select_fire_events == "Airport fire 2022-02-16":
        st.image(os.path.join(currentdir, 'ressources/airport_fire_d.jpg'))
        st.markdown(f'''<a href="https://www.fire.ca.gov/incidents/2022/2/16/airport-fire/" style="text-decoration: none;color:64a5c3">Click here for complete status</a>''', unsafe_allow_html=True)
        sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_Airport_postFire_RGBIR.tif'

    else:
        st.write('No fire selected')

    # Reset of the prediction
    if 'prediction' in st.session_state and 'prediction_name' in st.session_state:
        if st.session_state.prediction_name != select_fire_events:
            del st.session_state['prediction']
            del st.session_state['prediction_name']

    # Sentinel 2 image open
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

    center_of_bbox = [(gps_bounding_box[1] + gps_bounding_box[3]) / 2,
                      (gps_bounding_box[0] + gps_bounding_box[2]) / 2]

    # Array data
    arr = raster_sentinel2.read()

    # Normalize the data (divide par 10000)
    arr = arr / 10000

    # Change dimension order (number of channel at the end)
    arr = np.moveaxis(arr, 0, -1)

    # Selecting the RGB channels in the right order
    image_rgb = arr[:, :, :3]
    image_rgb = image_rgb[:, :, ::-1] * 100

    # Loading the pre-trained model
    if 'prediction_model' not in st.session_state:
        model = simple_unet_model(256, 256, 5)
        model.load_weights(
            './streamlit/saved_model/model_patches_20220130bis.hdf5')
        st.session_state.prediction_model = model

    # Prediction function
    def predict(arr):

        predictions_smooth = predict_img_with_smooth_windowing(
            arr,
            window_size=256,
            # Minimal amount of overlap for windowing. Must be an even number.
            subdivisions=2,
            nb_classes=1,
            pred_func=(
                lambda img_batch_subdiv: st.session_state.prediction_model.predict(
                    (img_batch_subdiv))
            )
        )
        return predictions_smooth[:, :, 0]

    # Adding the zoom slider
    zoom_slider = st.sidebar.slider(
        'Map zoom', 5.0, 15.0, 10.0)

    # Showing the map centered on the fire event
    map_california = folium.Map(location=center_of_bbox,
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

    # Adding the prediction button
    prediction_button = st.sidebar.button("Predict the burnt area")
    if prediction_button:
        prediction_smooth_img = predict(arr)
        st.session_state.prediction = prediction_smooth_img
        st.session_state.prediction_name = select_fire_events

    # Adding the prediction opacity slider
    if 'prediction' in st.session_state:
        prediction_opacity_slider = st.sidebar.slider(
            'Opacity of the prediction overlay', 0.0, 1.0, 0.5)

    # Adding the prediction image
    if 'prediction' in st.session_state:
        image_prediction = folium.raster_layers.ImageOverlay(
            name="Prediction image",
            image=st.session_state.prediction,
            bounds=bbox,
            interactive=True,
            zindex=2,
            opacity=prediction_opacity_slider
        )
        image_prediction.add_to(map_california)

    # Display the map
    folium_static(map_california)
