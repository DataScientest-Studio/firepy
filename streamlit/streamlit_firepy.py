# -*- coding: utf-8 -*-
"""
Script for the Streamlit demo of the FirePy project
"""

import folium  # map rendering library
import streamlit as st
from streamlit_folium import folium_static

# Adding the UI components for the user
st.title("FirePy demo")

select_fire_events = st.sidebar.selectbox(
    "Select a fire event",
    ("Fire 1", "Fire 1", "Fire 3")
)
sentinel_display = st.sidebar.radio(
    label='Show Sentinel 2 image', options=['Yes', 'No'])

prediction_button = st.sidebar.button("Predict the burnt area")

# Showing the map centered on San Jose GPS coordinates
map_california = folium.Map(location=[37.335480, -121.893028],
                            zoom_start=6)

folium_static(map_california)
