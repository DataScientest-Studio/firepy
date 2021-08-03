# :fire: Projet FirePy :fire:

## :mage: Contexte :mage:
Ce projet a été réalisé dans le cadre de la formation Data Scientist de [Datascientest](https://datascientest.com/) (promotion continue Juin 2021) 
Objectif
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

   ![exemple.jpg](https://raw.githubusercontent.com/DataScientest-Studio/firepy/main/exemple.jpg?token=AHPOTTHVED75FDOAWCFXHDLBBCEJI)
 
## :page_with_curl: Jeux de données :page_with_curl:
Les satellites Sentinel 2A et 2B réalisent des acquisitions dans le domaine optique depuis 2015 (https://fr.wikipedia.org/wiki/Sentinel-2 ). Financées par le programme européen Copernicus, ces missions permettent de produire des images entièrement libres sans restriction d’usage ou de profil d’utilisateur (https://sentinel2.cnes.fr/fr).
La résolution spatiale est de 20 m, une image Sentinel 2 se compose d’un peu plus de 30 millions de pixels.

## :bookmark_tabs: Description des fichiers :bookmark_tabs:
-	…
-	…
-	…

## :floppy_disk: Google Drive :floppy_disk:
Le Google Drive du projet contient les fichiers de sauvegarde de nos modèles de classication entraînés, trop volumineux pour être hébergés sur GitHub. 

## :computer: Réalisation :computer:
Réalisé par :
*	:fairy_woman: Emmanuelle CANO [(LinkedIn)](https://www.linkedin.com/in/emmanuelle-cano-4b845940/)
*	:superhero_man: François FAUPIN [(LinkedIn)](https://www.linkedin.com/in/fran%C3%A7ois-faupin-03259418/)
*	:zombie_man: Thomas GOSSART [(LinkedIn)](https://www.linkedin.com/in/gossartt/)

Supervisé par :
*	:genie: Thibault VENET [(LinkedIn)](https://www.linkedin.com/in/thibault-venet-49b1b5188/)

