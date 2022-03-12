import streamlit as st 
import os                      #+Deployment
import inspect                 #+Deployment


def page_dashboard():
    st.title("FirePy")
    st.header("Ce projet a été réalisé dans le cadre de la formation Data Scientist de Datascientest (promotion continue Juin 2021)")
    st.write("\n\n")  
    st.write(
    "Le relevé manuel des périmètres de feu est une tâche fastidieuse et sujette à erreur humaine. Le niveau de détails obtenu est limité car des poches épargnées par les flammes peuvent se trouver à l’intérieur des zones de feu."
    "\n\n"    
    "L’automatisation de la détection de surfaces brûlées par un algorithme permettrait d’alléger la charge de travail humaine, d’apporter de la robustesse dans l’analyse et de passer à l’échelle la zone d’analyse et permettrait d’apporter un estimation préliminaire quant aux dégâts (naturels, les biens, les infrastructures). Le traitement mathématique des images satellites est aussi un moyen d’aller au-delà d’une information binaire brûlé / non brûlé et d’affiner le niveau de brûlure."
     "\n\n"
    "Les méthodes traditionnelles de détection de zones brûlées ont des performances limitées. En fonctionnant à l’aide de seuils, il est difficile pour ces techniques de détecter des petites zones brûlées ou des brûlures de faible intensité. Certains algorithmes basés sur la détection d'anomalie sur le voisinage de pixels ont un taux élevé de fausse détection. Enfin, les méthodes exploitant les différences dans les séquences d’image dans le temps ont l’inconvénient de nécessiter beaucoup de données. Face à ce constat, les algorithmes de deep learning semblent particulièrement prometteurs et font l’objet de nombreuses recherches et publications."
    "\n\n"
    "La bonne disponibilité des données des satellites Sentinel 2 financés par le programme Copernicus de l’ESA est un atout essentiel pour le lancement du projet. En effet, les images sont disponibles gratuitement et couvrent depuis 2015 une grande partie de la surface terrestre."
    "\n\n"
    "C’est tout l’objectif de notre projet.", unsafe_allow_html=True)  
