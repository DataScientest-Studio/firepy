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
from pyproj import Proj, transform
import tensorflow as tf
from smooth_blending import predict_img_with_smooth_windowing
from unet_model import simple_unet_model

select_fire_events = st.sidebar.selectbox(
    "Select a fire event",
    ("Fire_1", "Fire_2", "Fire_3", "Airport fire 2022-02-16"),
    index=3
)

sentinel2_opacity_slider = st.sidebar.slider(
    'Opacity of Sentinel 2 overlay', 0.0, 1.0, 1.0)

if select_fire_events == "Fire_1":
    st.title("Incendie n°1 :")
    st.write(" ")
    st.subheader("Incendie ayant eu lieu le XX/XX/XXXX")
    sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_185_postFire_RGBIR.tif'
    if 'prediction' in st.session_state:
        del st.session_state['prediction']

elif select_fire_events == "Fire_2":
    st.title("Incendie n°2 :")
    st.write(" ")
    st.subheader("The fire started on 16th of February")
    sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_321_postFire_RGBIR.tif'
    if 'prediction' in st.session_state:
        del st.session_state['prediction']

elif select_fire_events == "Airport fire 2022-02-16":
    st.title("Incendie n°4 :")
    st.write(" ")
    st.subheader("The fire started on 16th of February 2022")
    st.subheader("The burnt area is 1674 ha")
    st.subheader("The road closures: Warm Springs Road east of Hwy 395")
    sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_Airport_postFire_RGBIR.tif'
    if 'prediction' in st.session_state:
        del st.session_state['prediction']

else:
    st.title("Incendie n°3 :")
    st.write(" ")
    st.subheader("Incendie ayant eu lieu le XX/XX/XXXX")
    sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_8351_postFire_RGBIR.tif'
    if 'prediction' in st.session_state:
        del st.session_state['prediction']

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
image_rgb = image_rgb[:, :, ::-1]


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


# Adding the title
st.title("FirePy demo")

# Adding the zoom slider
zoom_slider = st.sidebar.slider('Map zoom', 5.0, 15.0, 10.0)

# Showing the map centered on the fire event
map_california = folium.Map(location=center_of_bbox, zoom_start=zoom_slider)

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
