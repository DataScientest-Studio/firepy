# Projet FirePy

## Contexte
Ce projet a été réalisé dans le cadre de la formation Data Scientist de [Datascientest](https://datascientest.com/) (promotion continue Juin 2021) 
Objectif
Construction d’un algorithme de détection automatique des zones brûlées (incendie) par Deep-Learning appliqué à des images optiques Sentinel 2.

## Les étapes théoriques 
- Constitution d’une banque d’images Sentinel 2 (cf data) sur un site cible, la Californie, à partir de 6 bandes spectrales : (B,V,R,NIR,SWIR)
- Prétraitements des images
- Constitution d’une base de données exploitable de zones brûlées de plus de 10 000 échantillons (pixels), par calcul du dNBR (Difference Normalized Burn Ratio)
- Etude visant à identifier le modèle le plus adapté pour réaliser une classification supervisée par pixel des images
- Apprentissage du modèle avec la base de données
- Application du modèle sur d’autres dates et d’autres lieux (Australie)
- Calcul du Burn Severity par diachronie (entre deux dates, comme illustré ci-dessous)
- Récupération de données géographiques vecteur (polygones) de contour des zones brûlées détectées.
 
## Jeux de données
Les satellites Sentinel 2A et 2B réalisent des acquisitions dans le domaine optique depuis 2015 (https://fr.wikipedia.org/wiki/Sentinel-2 ). Financées par le programme européen Copernicus, ces missions permettent de produire des images entièrement libres sans restriction d’usage ou de profil d’utilisateur (https://sentinel2.cnes.fr/fr).
La résolution spatiale est de 20 m, une image Sentinel 2 se compose d’un peu plus de 30 millions de pixels.

## Description des fichiers
-	…
-	…
-	…

## Google Drive
Le Google Drive du projet contient les fichiers de sauvegarde de nos modèles de classication entraînés, trop volumineux pour être hébergés sur GitHub. 

## Réalisation
Réalisé par :
*	Emmanuelle CANO [(LinkedIn)](https://www.linkedin.com/in/emmanuelle-cano-4b845940/)
*	François FAUPIN [(LinkedIn)](https://www.linkedin.com/in/fran%C3%A7ois-faupin-03259418/)
*	Thomas GOSSART [(LinkedIn)](https://www.linkedin.com/in/gossartt/)

Supervisé par :
*	Thibault VENET [(LinkedIn)](https://www.linkedin.com/in/thibault-venet-49b1b5188/)

