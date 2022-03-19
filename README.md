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
-	1a_data_export.ipynb
-	1b_patches_generation.ipynb
-	2c_Unet_model_training_with_patches&albumentation.ipynb
-	2d_PSPNet_model_training_resize.ipynb.ipynb

## Streamlit demo

![https://share.streamlit.io/icecore013/firepy/main/streamlit/index.py](https://github.com/DataScientest-Studio/firepy/blob/main/resources/streamlit-logo-primary-colormark-darktext.png)

## :floppy_disk: Google Drive :floppy_disk:
The backup files and images used to train/test our models are hosted on Google drive because they are too large to be hosted on GitHub. 

## :computer: Credits :computer:

*	:fairy_woman: Emmanuelle CANO [(LinkedIn)](https://www.linkedin.com/in/emmanuelle-cano-4b845940/)
*	:sunglasses: François FAUPIN [(LinkedIn)](https://www.linkedin.com/in/francois-faupin/)
*	:zombie_man: Thomas GOSSART [(LinkedIn)](https://www.linkedin.com/in/gossartt/)

Mentor :
*	:genie: Pierre ADEIKALAM [(LinkedIn)](https://www.linkedin.com/in/data-jesus/)








## :heavy_check_mark: Méthodologie et environnement de travail :heavy_check_mark:

Dans la cartographie des techniques de machine learning, le challenge du projet correspond à une tâche de classification supervisée et, plus particulièrement, de segmentation sémantique. Il s’agit de classifier chaque pixel d’une image (pixel brûlé / non brûlé).

Afin d’atteindre cet objectif, la méthodologie globale appliquée suivra les étapes ci-dessous:
- Recherche bibliographique sur les méthodes de détection de zones brûlées
- Constitution d’une base de données suffisamment propre et variée
- Entrainement d’un algorithme de Deep Learning à partir d’une région pour laquelle des données de vérité terrain (informations collectées par l’homme et non automatisées) sont disponibles,
- Application de l’algorithme à d’autres scènes et d’autres incendies pour produire une cartographie du contour de la zone brûlée une fois le feu maîtrisé par classification au pixel. 

La nature des données d’entrée a nécessité une montée en compétences sur les images géo-référencées. En effet, des structures de données particulières (Fichiers vecteur Shapefile, Raster, GeoDataframe…) et des outils dédiés (QGIS, Geopandas, Rasterio…) ont dû être mis en œuvre.

Enfin, afin de pouvoir travailler en collaboratif sur un environnement permettant les calculs de deep learning, nous avons utilisé les outils Google (Drive, Colab, Google Earth Engine) ainsi qu’un espace Github dédié.


## :satellite: Description des données des satellites Sentinel 2 :satellite:
Les satellites Sentinel 2A et 2B réalisent des acquisitions dans le domaine optique depuis 2015 (https://fr.wikipedia.org/wiki/Sentinel-2 ). Financées par le programme européen Copernicus, ces missions permettent de produire des images entièrement libres sans restriction d’usage ou de profil d’utilisateur (https://sentinel2.cnes.fr/fr).
La résolution spatiale est de 20 m, une image Sentinel 2 se compose d’un peu plus de 30 millions de pixels.
L’ensemble des caractéristiques techniques des images Sentinel 2 est présenté ici : 
https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument

Les caractéristiques des bandes spectrales :

Le capteur Sentinel 2 (MSI) permet de réaliser des acquisitions dans 13 bandes spectrales de résolutions spatiales différentes (de 10 à 60 m) dans les domaines du visible, du proche et du moyen infrarouge (https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial)
Le calcul de l’indice permettant de détecter les zones brûlées fera appel aux bandes 7 (NIR) et 12 (SWIR), toutes les deux à 20 m de résolution spatiale.
On pourra également utiliser les bandes du visible et du proche infrarouge à 10m (2,3,4 et 8) pour réaliser des compositions colorées permettant d’analyser visuellement les territoires à traiter ainsi que de calculer d’autres indices en lien avec la densité de végétation tels que le NDVI.

![image](https://user-images.githubusercontent.com/31386060/155057380-e61428af-56c1-4fcb-bf75-e28a9e670619.png)
 
## :earth_americas: Description des données d'évenements de feux :earth_americas:
En tant que référence pour établir les datasets de training / validation / test, nous avons utilisé deux ressources principales :

- Pour la partie nord américaine: “Fire Perimeters in California Database CAL FIRE, provided by the Fire and Resource Assessment Program (FRAP)”

- Pour la partie Européenne, nous avons exploité la base de données des feux au Portugal de l’institut INCF.

![Shapefile](https://github.com/DataScientest-Studio/firepy/blob/main/resources/image25.png?raw=true)

Pour chaque source, il était possible de télécharger un fichier shapefile contenant l’ensemble des incendies. L’outil QGIS a permis de contrôler les géométries puis de récupérer les géométries de chaque zone brûlée dans un fichier dédié.

Ces périmètres vont nous aider à récupérer les images correspondant aux événements dans des limites d’emprises pertinentes, mais aussi à construire le jeu d'entraînement et à contrôler nos résultats.


## :hotsprings:Sélection des incendies pour la base de données d'entraînement :hotsprings:
La lecture des bases de données Shapefile de la Californie et du Portugal permet d’obtenir un “Geo-dataframe pandas” qui est une extension du dataframe Pandas avec un géo-référencement de chaque observation.

![geodf](https://github.com/DataScientest-Studio/firepy/blob/main/resources/image11.png?raw=true)

Pour chaque évènement, nous avons donc une colonne avec le périmètre de zones brûlées sous la forme d’une liste de polygones définis par des coordonnées
A l’issue de la récupération des Shapefiles contenant plusieurs centaines d’incendies, nous avons scripté l’extraction des éléments suivant : longitude_1 et longitude_2, latitude_1 et latitude_2 (afin d’obtenir la bounding box en coordonnées GPS), date de début de l’incendie, date de fin de l’incendie (pour dater et faciliter la recherche des images Sentinel 2 pré-fire et post-fire). Ces informations permettent de solliciter le service Google Earth Engine afin de télécharger les images Sentinel 2.

## :globe_with_meridians:Génération des images Sentinel 2 :globe_with_meridians:
Google Earth Engine est un service fournissant un catalogue d’images satellite et de dataset géo-référencés de plusieurs petabytes. Des capacités d’analyse de la surface de la Terre sont mises à la disposition des chercheurs et développeurs. 
Ce service gratuit est un bon moyen de collecte des gros volumes de données d’imagerie satellitaire Sentinel 2.

L’extraction des données Sentinel 2 a été codée de la façon suivante:

![image](https://user-images.githubusercontent.com/31386060/155056296-37279b72-e34a-4485-a032-bb3bfce3208d.png)

Requête du catalogue Sentinel 2
- Filtrage sur la zone d’intérêt via les coordonnées GPS issues du géo-dataframe
- Filtrage sur la période d’intérêt issue du géo-dataframe
- Filtrage sur les images contenant moins de 10% de couverture nuageuse
- Filtrage sur les bandes du capteur (3 canaux RGB + 2 infra-rouge NIR, SWI). D’après certaines publications, le choix de ces 5 fréquences produit en effet les meilleures performances de classification.
- Reconstruction et fusion d’une mosaïque d’images (par empilement)
- Découpage sur la zone d’intérêt

## :face_in_clouds: Génération des masques :face_in_clouds:
La génération du masque se déroule en 4 étapes:
- Préparation d’une image raster de masque construite sur les caractéristiques de l’image Sentinel 2 correspondante et contenant des valeurs nulles. La librairie GDAL contenant le driver “GTiff” a été utilisée. 
- Récupération de la géométrie issue du shapefile correspondant. La librairie OGR contenant le driver “ESRI shapefile” a été utilisée.
- Ajout de la géométrie de la zone brûlée à l’image raster de masque.
- Export de l’image raster de masque en fichier tiff.

![image2](https://github.com/DataScientest-Studio/firepy/blob/main/resources/image8.png?raw=true)


## :chart: Pre-processing des données :chart:
- Verification de la Qualité des données (présence de fumée/neige/erreur de labellisation)
- Découpage en patchs : (𝑛𝑏 𝑏𝑎𝑡𝑐ℎ, 𝑛𝑏 𝑝𝑖𝑥𝑒𝑙𝑠 ℎ𝑎𝑢𝑡𝑒𝑢𝑟, 𝑛𝑏 𝑝𝑖𝑥𝑒𝑙𝑠 𝑙𝑎𝑟𝑔𝑒𝑢𝑟, 𝑛𝑏 𝑐𝑎𝑛𝑎𝑢𝑥) soit : (32, 256, 256, 5)
- Normalisation
- Augmentation des données
- Dimensions du dataset d’entrée

## :computer: Modélisation de type “segmentation sémantique” :computer:
## U-Net
La modélisation U-net a été proposée dans la publication “U-Net: Convolutional Networks for Biomedical Image Segmentation”. Cette méthode de classification est de type FCNN “Fully Convolutional Neural Network”, c'est-à-dire sans couches fully connected.

L’architecture U-Net semble pertinente pour la segmentation d’images satellites. En effet, ce type de modélisation a démontré de bons résultats pour des tâches similaires et pour des bases de données d'entraînement peu fournies.

![image_unet](https://github.com/DataScientest-Studio/firepy/blob/main/resources/image12.png?raw=true)

![image](https://user-images.githubusercontent.com/31386060/155056814-e708519e-fa47-46c3-b90a-45bf4904f97e.png)
![image](https://user-images.githubusercontent.com/31386060/155056833-8730237c-7d3f-4470-a4b6-5c17b1e210e9.png)
![image](https://user-images.githubusercontent.com/31386060/155056790-e3b1591b-d617-48b2-b571-51260a77fe8e.png)

## PSP-Net
Afin de confronter le modèle U-Net, il a été proposé (suite à plusieurs articles et Githubs mettant en avant ce modèle dans la segmentation d’images satellite) d’utiliser le modèle PSPNet (Pyramid Scene Parsing Network).

![image](https://user-images.githubusercontent.com/31386060/155057002-94959f73-2123-4ada-9739-4b66fd4b02a3.png)


La difficulté réside dans le fait que ce modèle peut s'avérer puissant mais uniquement sur des images constituées de 3 bandes (RGB) et devient trop gourmand en ressources sur nos fichiers en 5 bandes car là où le modèle U-Net nécessite 1,941,393 paramètres, le PSP requiert 31,203,073 paramètres.
La modélisation a été effectuée sur l’ensemble des données en Patch, mais s’est vite soldée par un échec car la RAM disponible sur les serveurs Colab n’était pas suffisante.
Afin de tout de même lui laisser ses chances, nous avons procédé à un redimensionnement des images afin d'alléger la charge mais les résultats n’étaient pas concluants non plus (nous pouvons constater que la prédiction a des artefacts et n’est pas aussi précise que pour le modèle U-Net)

![image](https://user-images.githubusercontent.com/31386060/155057035-a1190556-612e-45f7-9db0-6e152228c2d1.png)

## :mag: Prédiction sur de nouvelles images :mag:

Le modèle appris sur le dataset d'entraînement peut être appliqué à de nouvelles images. 

Cette tâche de prédiction se déroule en 3 étapes:
1. Découpage d’une image Sentinel 2 en patchs de 256 par 256 pixels
2. Prédiction des zones brûlées sur chaque patch à l’aide du modèle
3. Reconstitution d’une prédiction globale à partir des patchs prédits

Pour la dernière étape, 2 méthodes ont été mise en oeuvre:
Juxtaposition des patchs prédits. Le modèle est appliqué sur chaque patch et les résultats sont simplement collés en respectant l’ordre du découpage. Cette technique est disponible via la méthode unpatchify du package patchify. Bien que rapide, cette méthode fait apparaître des artéfacts sur les bords de chaque bord. Le modèle a en effet plus de difficultés à apprendre près des bords. De plus, les prédictions ne sont possibles que sur un nombre fini de patchs, ce qui peut exclure une partie de l’image. Voir image en bas à gauche.
“Smoothed blending” des patchs prédits. Dans cet algorithme, le modèle est appliqué sur une fenêtre glissante de l’image satellite avec un overlap entre chaque tuile. Ensuite, les résultats de prédiction sont recombinés ensemble avec une interpolation de type spline. L’algorithme utilisé est issu d’un projet open source (https://github.com/Vooban/Smoothly-Blend-Image-Patches). Bien que nécessitant plus de temps de calcul, cette méthode est plus performante et les images produites sont très réalistes. Voir image en bas à droite.

![image](https://github.com/DataScientest-Studio/firepy/blob/f49526d30c78fbaa1f4356544c7e5d84d3810c2e/resources/U_Net%20Prediction%20result%20on%20California%20imagery.png)

On remarque que le masque de zone brûlée issu de la prédiction est très proche de la vérité terrain. L’affichage de la probabilité de zone brûlée permet de faire apparaître des nuances dans le niveau de brûlure ainsi que des éléments internes (cours d’eau, routes…). Cette nouvelle connaissance est intéressante pour évaluer l'impact du feu sur les points stratégiques de la zone étudiée. Une meilleure gestion des conséquences de l’incendie est alors possible.





