# :fire: Projet FirePy :fire:

## :mage: Contexte :mage:
Ce projet a été réalisé dans le cadre de la formation Data Scientist de [Datascientest](https://datascientest.com/) (promotion continue Juin 2021) 

## :dart: Objectif :dart:
Construction d’un algorithme de détection automatique des zones brûlées (incendie) par Deep-Learning appliqué à des images optiques Sentinel 2.

## :heavy_check_mark: Les étapes théoriques :heavy_check_mark:
- Constitution d’une banque d’images Sentinel 2 (cf data) sur un site cible, la Californie, à partir de 6 bandes spectrales : (B,V,R,NIR,SWIR)
- Prétraitements des images
- Constitution d’une base de données exploitable de zones brûlées de plus de 10 000 échantillons (pixels), par calcul du dNBR (Difference Normalized Burn Ratio)
- Etude visant à identifier le modèle le plus adapté pour réaliser une classification supervisée par pixel des images
- Apprentissage du modèle avec la base de données
- Application du modèle sur d’autres dates et d’autres lieux (Australie)
- Calcul du Burn Severity par diachronie (entre deux dates, comme illustré ci-dessous)
- Récupération de données géographiques vecteur (polygones) de contour des zones brûlées détectées.

   ![exemple.jpg](https://github.com/DataScientest-Studio/firepy/blob/01dc7975c51abd21e72d47f828e7672913d1049b/exemple.jpg)
 
## :page_with_curl: Jeux de données :page_with_curl:
Les satellites Sentinel 2A et 2B réalisent des acquisitions dans le domaine optique depuis 2015 (https://fr.wikipedia.org/wiki/Sentinel-2 ). Financées par le programme européen Copernicus, ces missions permettent de produire des images entièrement libres sans restriction d’usage ou de profil d’utilisateur (https://sentinel2.cnes.fr/fr).
La résolution spatiale est de 20 m, une image Sentinel 2 se compose d’un peu plus de 30 millions de pixels.
L’ensemble des caractéristiques techniques des images Sentinel 2 est présenté ici : 
https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument

Les caractéristiques des bandes spectrales :

Le capteur Sentinel 2 (MSI) permet de réaliser des acquisitions dans 13 bandes spectrales de résolutions spatiales différentes (de 10 à 60 m) dans les domaines du visible, du proche et du moyen infrarouge (https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial)
Le calcul de l’indice permettant de détecter les zones brûlées fera appel aux bandes 7 (NIR) et 12 (SWIR), toutes les deux à 20 m de résolution spatiale.
On pourra également utiliser les bandes du visible et du proche infrarouge à 10m (2,3,4 et 8) pour réaliser des compositions colorées permettant d’analyser visuellement les territoires à traiter ainsi que de calculer d’autres indices en lien avec la densité de végétation tels que le NDVI.

Les différents niveaux de qualité : 

Level-1C product provides orthorectified Top-Of-Atmosphere (TOA) reflectance, with sub-pixel multispectral registration. Cloud and land/water masks are included in the product.
Level-2A product provides orthorectified Bottom-Of-Atmosphere (BOA) reflectance, with sub-pixel multispectral registration. A Scene Classification map (cloud, cloud shadows, vegetation, soils/deserts, water, snow, etc.) is included in the product.
Level-1C and Level-2A products are made available to users via the Copernicus Open Access Hub (SciHub). Images can also be downloaded here:
peps.cnes.fr/
https://catalogue.theia-land.fr/
https://earthexplorer.usgs.gov/
Pour notre étude, on privilégiera tant que possible le niveau L2A, toutefois ces images sont plus longues à obtenir que le niveau inférieur.

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

