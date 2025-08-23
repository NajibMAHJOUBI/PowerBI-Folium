# Power BI - Folium

Créer une carte avec la librairie Python Folium et comment l'insérer dans un rapport Power BI Desktop (en préversion).

Les éléments de ce repo servent à accompagner un article Linkedin sur l'insertion de cartes Folium dans Power BI Desktop.

## Prérequis

- Python : 

    - pandas
    - geopandas
    - folium   

- Power Bi Desktop

## Données

Dans le répertoire [data](data/), vous trouverez les données utilisées pour l'article :

- [MTA_Subway_Stations.csv](data/MTA_Subway_Stations.csv) : données de géolocalisations des stations de métro de la ville de New York City

Dans le répertoire [power_bi](power_bi), vous trouverez les fichiers *.pbix* :

- [nyc_subway.pbix](power_bi/nyc_subway.pbix) : rapport reprenant l'exemple présenté dans l'artcicle

- [all_maps.pbix](power_bi/nyc_subway.pbix) : rapport avec des cartes Folium avanccées (clustered et heatmap)

Dans le répertoire [html](html/), vous trouverez les fichiers *html* de cartes Folium : 

- [nyc_marker.html](html/nyc_marker.html) : carte Folium  des marqueurs des stations de métro

- [nyc_heamap.html](html/nyc_heatmap.html) : heatmap Folium des marqueurs des stations de métro

- [nyc_clusterhtml](html/nyc_marker.html) : carte Folium  des clusters des  marqueurs de stations de métro


## Rappport Power BI

Avant d'uiliser les rapports pbix disponibles dans [power_bi](power_bi/), vous devez lancer un serveur web local en Python : 

- Identifier le dossier dans lequel est placé le fichier [nyc_marker.html](html/nyc_marker.html) est placé, par exemple C:\PowerBI-Folium\html

- Ouvrir l'invite de commande (CMD) et naviguer jusqu'à ce dossier :

````bash
cd C:\PowerBI-Folium\htm
````


- Démarrer un serveur HTTP avec Python :

````python
python -m http.server 8000
````

La carte Folium est maintenant accessible à l'adresse : http://localhost:8000/nyc_marker.html






