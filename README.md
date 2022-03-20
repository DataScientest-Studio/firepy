# :fire: FirePy Project :fire:

## :mage: Context :mage:
![Datascientest_logo](https://github.com/DataScientest-Studio/firepy/blob/main/resources/image6.png)

This project was made out as part of training course at  [Datascientest.com](https://datascientest.com/) (Data Scientist program June '21) .

## :dart: Objectif :dart:
Create a deep learning model based on U-Net architecture for semantic segmentation of satellite images (Sentinel-2) to detect burned area.

## :office_worker: Business case :office_worker:
Manual surveying of fire perimeters is a tedious and tiring task and subject to human error. The level could be limited due to pockets spared by the flames found inside the fire zones.

The automation of the detection of burnt surfaces by an algorithm would make it possible to lighten the human workload, to bring robustness to the analysis and to scale the analysis area and would make it possible to provide a preliminary estimate of damage (natural, property, infrastructure). Mathematical processing of satellite images is also a way to go beyond burnt/unburnt binary information and refine the burn level.

Traditional burn area detection methods have limited performance. By operating using thresholds, it is difficult for these techniques to detect small burned areas or low intensity burns. Some algorithms based on anomaly detection on the neighborhood of pixels have a high rate of false detection. Finally, methods exploiting differences in image sequences over time have the disadvantage of requiring a lot of data. Faced with this observation, deep learning algorithms seem particularly promising and are the subject of numerous research and publications.

The good availability of data from the Sentinel 2 satellites financed by ESA's Copernicus program is an essential asset for the launch of the project. Indeed, the images are available free of charge and have covered a large part of the earth's surface since 2015.


## :bookmark_tabs: Files Descriptions :bookmark_tabs:
- [![Image1](https://github.com/DataScientest-Studio/firepy/blob/main/resources/colab.svg)](https://colab.research.google.com/github/icecore013/image-segmentation-keras/blob/master/1a_data_export.ipynb "1a_data_export") -	1a_data_export.ipynb 

- [![Image2](https://github.com/DataScientest-Studio/firepy/blob/main/resources/colab.svg)](https://colab.research.google.com/github/icecore013/image-segmentation-keras/blob/master/1b_patches_generation.ipynb "1b_patches_generation") -	1b_patches_generation.ipynb

- [![Image3](https://github.com/DataScientest-Studio/firepy/blob/main/resources/colab.svg)](https://colab.research.google.com/github/icecore013/image-segmentation-keras/blob/master/2c_model_training_with_patches%26albumentation.ipynb "2c_Unet_model_training_with_patches&albumentation") -	2c_Unet_model_training_with_patches&albumentation.ipynb 

- [![Image4](https://github.com/DataScientest-Studio/firepy/blob/main/resources/colab.svg)](https://colab.research.google.com/github/icecore013/image-segmentation-keras/blob/master/PSPNet_unaugmented.ipynb "2d_PSPNet_model_training_resize") -	2d_PSPNet_model_training_resize.ipynb 

- [![Image5](https://github.com/DataScientest-Studio/firepy/blob/main/resources/colab.svg)](https://colab.research.google.com/github/icecore013/image-segmentation-keras/blob/master/3_model_prediction.ipynb "3_model_prediction") -	3_model_prediction.ipynb 


## :cloud: Streamlit demo :cloud:

[![Image](https://github.com/DataScientest-Studio/firepy/blob/main/resources/streamlit-logo-primary-colormark-darktext.png)](https://share.streamlit.io/icecore013/firepy/main/streamlit/index.py "FirePy demo")

## :floppy_disk: Google Drive :floppy_disk:
The backup files and images used to train/test our models are hosted on Google drive because they are too large to be hosted on GitHub.

[![Image](https://github.com/DataScientest-Studio/firepy/blob/main/resources/302-3020172_compress-files-png-winrar-icon-transparent-png.jpg)](https://drive.google.com/file/d/1WNSpqYYKdbIODO08HnEXLcLgHTSFt5hv/view?usp=sharing "Download all data files") This file contains 27 fires, witch mean almost 1200 patchs (256*256) 


Despite the small number of images available, it was decided to favor the data quality.
Non-quality factors are related to the presence of elements between the burnt area and the satellite sensor.
Unlike other satellites with an active sensor (radar sending an electromagnetic wave crossing the elements), the Sentinel-2 images only receive emissions from Earth in different frequencies.
Any unwanted element between the sensor and the burnt area is therefore disturbing for the training of the model.

**The mask generation takes place in 4 steps:** 

- Preparation of a mask raster image built on the features of the corresponding Sentinel 2 image and containing null values. The GDAL10 library containing the “GTiff” driver was used.
- Recovery of geometry from the corresponding shapefile. The OGR11 library containing the “ESRI shapefile” driver was used.
- Added burnt area geometry to mask raster image.
- Export mask raster image to tiff file.

## :computer: Credits :computer:

*	:fairy_woman: Emmanuelle CANO [(LinkedIn)](https://www.linkedin.com/in/emmanuelle-cano-4b845940/)
*	:sunglasses: François FAUPIN [(LinkedIn)](https://www.linkedin.com/in/francois-faupin/)
*	:zombie_man: Thomas GOSSART [(LinkedIn)](https://www.linkedin.com/in/gossartt/)

Mentor :
*	:genie: Pierre ADEIKALAM [(LinkedIn)](https://www.linkedin.com/in/data-jesus/)





