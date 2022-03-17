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
    st.subheader("Some examples on RGB bands from Firepy dataset with associate masks")
    
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            st.write("Despite the small number of images available, it was decided to favor the data quality.")
            st.write("Non-quality factors are related to the presence of elements between the burnt area and the satellite sensor.") 
            st.write("Unlike other satellites with an active sensor (radar sending an electromagnetic wave crossing the elements), the Sentinel-2 images only receive emissions from Earth in different frequencies.") 
            st.write("Any unwanted element between the sensor and the burnt area is therefore disturbing for the training of the model.")

            
        with c2:
            st.write(" The generation of masks takes place in 4 steps:")
            st.write(" • Preparation of a mask raster image built on the features of the corresponding Sentinel 2 image and containing null values. The GDAL10 library containing the “GTiff” driver was used.")
            st.write(" • Recovery of geometry from the corresponding shapefile. The OGR11 library containing the “ESRI shapefile” driver was used.")
            st.write(" • Added burnt area geometry to mask raster image.")
            st.write(" • Export mask raster image to tiff file.")
                     
                     
    gallery_content = open(os.path.join(currentdir, 'ressources/gallery.json'))
    data  = json.load(gallery_content)
    
    for images_row in chunks(data['gallery']['images'], 3):
        c1, c2, c3 = st.columns([1, 1, 1])
        if len(images_row)>=1: c1.image(load_image(currentdir, images_row[0]['image-link']), caption=images_row[0]['image-desc'], use_column_width='always') 
        if len(images_row)>=2: c2.image(load_image(currentdir, images_row[1]['image-link']), caption=images_row[1]['image-desc'], use_column_width='always') 
        if len(images_row)==3: c3.image(load_image(currentdir, images_row[2]['image-link']), caption=images_row[2]['image-desc'], use_column_width='always')
