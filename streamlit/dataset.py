import streamlit as st 
import matplotlib.pyplot as plt
import json
import os                      #+Deployment
import inspect                 #+Deployment

@st.cache
def load_image(cdir, link):
    return plt.imread(os.path.join(cdir, link))

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def app():

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    st.subheader("Some exemples from Firepy dataset ")

    gallery_content = open(os.path.join(currentdir, 'ressources/gallery.json'))
    data  = json.load(gallery_content)

    for images_row in chunks(data['gallery']['images'], 3):
        c1, c2, c3 = st.columns([1, 1, 1])
        if len(images_row)>=1: c1.image(load_image(currentdir, images_row[0]['image-link']), caption=images_row[0]['image-desc'], use_column_width='always') 
        if len(images_row)>=2: c2.image(load_image(currentdir, images_row[1]['image-link']), caption=images_row[1]['image-desc'], use_column_width='always') 
        if len(images_row)==3: c3.image(load_image(currentdir, images_row[2]['image-link']), caption=images_row[2]['image-desc'], use_column_width='always')
