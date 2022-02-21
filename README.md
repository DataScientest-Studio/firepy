# :fire: Projet FirePy :fire:

## :mage: Contexte :mage:
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


   ![exemple.jpg](https://github.com/DataScientest-Studio/firepy/blob/01dc7975c51abd21e72d47f828e7672913d1049b/exemple.jpg)
 
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
*	:genie: Thibault VENET [(LinkedIn)](https://www.linkedin.com/in/thibault-venet-49b1b5188/)

