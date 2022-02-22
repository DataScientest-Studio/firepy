# :fire: Projet FirePy :fire:

## :mage: Contexte :mage:
![https://github.com/DataScientest-Studio/firepy/blob/main/resources/image6.png]
Ce projet a été réalisé dans le cadre de la formation Data Scientist de [Datascientest](https://datascientest.com/) (promotion continue Juin 2021) 

## :dart: Objectif :dart:
Construction d’un algorithme de détection automatique des zones brûlées (incendie) par Deep-Learning appliqué à des images optiques Sentinel 2.

## :office_worker: Business case :office_worker:
Le relevé manuel des périmètres de feu est une tâche fastidieuse et sujette à erreur humaine. Le niveau de détails obtenu est limité car des poches épargnées par les flammes peuvent se trouver à l’intérieur des zones de feu.

L’automatisation de la détection de surfaces brûlées par un algorithme permettrait d’alléger la charge de travail humaine, d’apporter de la robustesse dans l’analyse et de passer à l’échelle la zone d’analyse et permettrait d’apporter un estimation préliminaire quant aux dégâts (naturels, les biens, les infrastructures). Le traitement mathématique des images satellites est aussi un moyen d’aller au-delà d’une information binaire brûlé / non brûlé et d’affiner le niveau de brûlure.

Les méthodes traditionnelles de détection de zones brûlées ont des performances limitées. En fonctionnant à l’aide de seuils, il est difficile pour ces techniques de détecter des petites zones brûlées ou des brûlures de faible intensité. Certains algorithmes basés sur la détection d'anomalie sur le voisinage de pixels ont un taux élevé de fausse détection. Enfin, les méthodes exploitant les différences dans les séquences d’image dans le temps ont l’inconvénient de nécessiter beaucoup de données.
Face à ce constat, les algorithmes de deep learning semblent particulièrement prometteurs et font l’objet de nombreuses recherches et publications.

La bonne disponibilité des données des satellites Sentinel 2 financés par le programme Copernicus de l’ESA est un atout essentiel pour le lancement du projet. En effet, les images sont disponibles gratuitement et couvrent depuis 2015 une grande partie de la surface terrestre.



## :heavy_check_mark: Méthodologie et environnement de travail :heavy_check_mark:

Dans la cartographie des techniques de machine learning, le challenge du projet correspond à une tâche de classification supervisée et, plus particulièrement, de segmentation sémantique. Il s’agit de classifier chaque pixel d’une image (pixel brûlé / non brûlé).

Afin d’atteindre cet objectif, la méthodologie globale appliquée suivra les étapes ci-dessous:
- Recherche bibliographique sur les méthodes de détection de zones brûlées
- Constitution d’une base de données suffisamment propre et variée
- Entrainement d’un algorithme de Deep Learning à partir d’une région pour laquelle des données de vérité terrain (informations collectées par l’homme et non automatisées) sont disponibles,
- Application de l’algorithme à d’autres scènes et d’autres incendies pour produire une cartographie du contour de la zone brûlée une fois le feu maîtrisé par classification au pixel. 

La nature des données d’entrée a nécessité une montée en compétences sur les images géo-référencées. En effet, des structures de données particulières (Fichiers vecteur Shapefile, Raster, GeoDataframe…) et des outils dédiés (QGIS, Geopandas, Rasterio…) ont dû être mis en œuvre.

Enfin, afin de pouvoir travailler en collaboratif sur un environnement permettant les calculs de deep learning, nous avons utilisé les outils Google (Drive, Colab, Google Earth Engine) ainsi qu’un espace Github dédié.


## :page_with_curl: Description des données des satellites Sentinel 2 :page_with_curl:
Les satellites Sentinel 2A et 2B réalisent des acquisitions dans le domaine optique depuis 2015 (https://fr.wikipedia.org/wiki/Sentinel-2 ). Financées par le programme européen Copernicus, ces missions permettent de produire des images entièrement libres sans restriction d’usage ou de profil d’utilisateur (https://sentinel2.cnes.fr/fr).
La résolution spatiale est de 20 m, une image Sentinel 2 se compose d’un peu plus de 30 millions de pixels.
L’ensemble des caractéristiques techniques des images Sentinel 2 est présenté ici : 
https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument

Les caractéristiques des bandes spectrales :

Le capteur Sentinel 2 (MSI) permet de réaliser des acquisitions dans 13 bandes spectrales de résolutions spatiales différentes (de 10 à 60 m) dans les domaines du visible, du proche et du moyen infrarouge (https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial)
Le calcul de l’indice permettant de détecter les zones brûlées fera appel aux bandes 7 (NIR) et 12 (SWIR), toutes les deux à 20 m de résolution spatiale.
On pourra également utiliser les bandes du visible et du proche infrarouge à 10m (2,3,4 et 8) pour réaliser des compositions colorées permettant d’analyser visuellement les territoires à traiter ainsi que de calculer d’autres indices en lien avec la densité de végétation tels que le NDVI.

  ![spatial.jpg](https://user-images.githubusercontent.com/31386060/154951088-ab7d9541-b3e1-4021-afa2-87aba9d9bc46.png)
 
## :earth_americas: Description des données d'évenements de feux :earth_americas:
En tant que référence pour établir les datasets de training / validation / test, nous avons utilisé deux ressources principales :

- Pour la partie nord américaine: “Fire Perimeters in California Database CAL FIRE, provided by the Fire and Resource Assessment Program (FRAP)”

- Pour la partie Européenne, nous avons exploité la base de données des feux au Portugal de l’institut INCF.

Pour chaque source, il était possible de télécharger un fichier shapefile contenant l’ensemble des incendies. L’outil QGIS a permis de contrôler les géométries puis de récupérer les géométries de chaque zone brûlée dans un fichier dédié.

Ces périmètres vont nous aider à récupérer les images correspondant aux événements dans des limites d’emprises pertinentes, mais aussi à construire le jeu d'entraînement et à contrôler nos résultats.


## :hotsprings:Sélection des incendies pour la base de données d'entraînement :hotsprings:
La lecture des bases de données Shapefile de la Californie et du Portugal permet d’obtenir un “Geo-dataframe pandas” qui est une extension du dataframe Pandas avec un géo-référencement de chaque observation.
Pour chaque évènement, nous avons donc une colonne avec le périmètre de zones brûlées sous la forme d’une liste de polygones définis par des coordonnées
A l’issue de la récupération des Shapefiles contenant plusieurs centaines d’incendies, nous avons scripté l’extraction des éléments suivant : longitude_1 et longitude_2, latitude_1 et latitude_2 (afin d’obtenir la bounding box en coordonnées GPS), date de début de l’incendie, date de fin de l’incendie (pour dater et faciliter la recherche des images Sentinel 2 pré-fire et post-fire). Ces informations permettent de solliciter le service Google Earth Engine afin de télécharger les images Sentinel 2.

## :globe_with_meridians:Génération des images Sentinel 2 :globe_with_meridians:
Google Earth Engine est un service fournissant un catalogue d’images satellite et de dataset géo-référencés de plusieurs petabytes. Des capacités d’analyse de la surface de la Terre sont mises à la disposition des chercheurs et développeurs. 
Ce service gratuit est un bon moyen de collecte des gros volumes de données d’imagerie satellitaire Sentinel 2.

L’extraction des données Sentinel 2 a été codée de la façon suivante:

Requête du catalogue Sentinel 2
Filtrage sur la zone d’intérêt via les coordonnées GPS issues du géo-dataframe
Filtrage sur la période d’intérêt issue du géo-dataframe
Filtrage sur les images contenant moins de 10% de couverture nuageuse
Filtrage sur les bandes du capteur (3 canaux RGB + 2 infra-rouge NIR, SWI). D’après certaines publications, le choix de ces 5 fréquences produit en effet les meilleures performances de classification.
Reconstruction et fusion d’une mosaïque d’images (par empilement)
Découpage sur la zone d’intérêt

## :face_in_clouds: Génération des masques :face_in_clouds:
La génération du masque se déroule en 4 étapes:
- Préparation d’une image raster de masque construite sur les caractéristiques de l’image Sentinel 2 correspondante et contenant des valeurs nulles. La librairie GDAL contenant le driver “GTiff” a été utilisée. 
- Récupération de la géométrie issue du shapefile correspondant. La librairie OGR contenant le driver “ESRI shapefile” a été utilisée.
- Ajout de la géométrie de la zone brûlée à l’image raster de masque.
- Export de l’image raster de masque en fichier tiff.

## :chart: Pre-processing des données :chart:
- Verification de la Qualité des données
- Découpage en patchs
- Normalisation
- Augmentation des données
- Dimensions du dataset d’entrée

## :computer: Modélisation de type “segmentation sémantique” :computer:
## U-Net
La modélisation U-net a été proposée dans la publication “U-Net: Convolutional Networks for Biomedical Image Segmentation”. Cette méthode de classification est de type FCNN “Fully Convolutional Neural Network”, c'est-à-dire sans couches fully connected.

L’architecture U-Net semble pertinente pour la segmentation d’images satellites. En effet, ce type de modélisation a démontré de bons résultats pour des tâches similaires et pour des bases de données d'entraînement peu fournies.


## :bookmark_tabs: Description des fichiers :bookmark_tabs:
-	



## :floppy_disk: Google Drive :floppy_disk:
Le Google Drive du projet contient les fichiers de sauvegarde de nos modèles de classication entraînés, trop volumineux pour être hébergés sur GitHub. 

## :computer: Réalisation :computer:
Réalisé par :
*	:fairy_woman: Emmanuelle CANO [(LinkedIn)](https://www.linkedin.com/in/emmanuelle-cano-4b845940/)
*	:superhero_man: François FAUPIN [(LinkedIn)](https://www.linkedin.com/in/fran%C3%A7ois-faupin-03259418/)
*	:zombie_man: Thomas GOSSART [(LinkedIn)](https://www.linkedin.com/in/gossartt/)

Supervisé par :
*	:genie: Pierre ADEIKALAM [(LinkedIn)](https://www.linkedin.com/in/data-jesus/)

