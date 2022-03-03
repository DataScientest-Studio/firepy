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

# Sentinel 2 image path
sentinel2_image_path = './streamlit/test_images/CAL_database_Sentinel2_185_postFire_RGBIR.tif'
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

# Adding the UI components for the user
st.title("FirePy demo")

zoom_slider = st.sidebar.slider(
    'Map zoom', 0.0, 20.0, 10.0)

select_fire_events = st.sidebar.selectbox(
    "Select a fire event",
    ("Fire 1", "Fire 1", "Fire 3")
)

sentinel2_opacity_slider = st.sidebar.slider(
    'Opacity of Sentinel 2 overlay', 0.0, 1.0, 1.0)

prediction_button = st.sidebar.button("Generate the burnt area prediction")

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

# Display the map
folium_static(map_california)
