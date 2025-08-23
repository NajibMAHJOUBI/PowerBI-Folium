# -*- coding: utf-8 -*-

# Import libraries
import os
from pathlib import Path
import pandas as pd
from folium.plugins import HeatMap
import folium

# Read the MTA Subway Stations data
columns = ["Line", "Stop Name",	"GTFS Latitude", "GTFS Longitude"]

path_parent = Path(os.path.dirname(os.path.abspath(__file__))).parent
path_data = os.path.join(path_parent, 'data', 'MTA_Subway_Stations.csv')

df = pd.read_csv(path_data, usecols=columns)

df.rename(columns={"GTFS Latitude": "Latitude", "GTFS Longitude": "Longitude"}, inplace=True)

# Create a list of coordinate pairs
locations = list(zip(df["Latitude"], df["Longitude"]))


# Create a Map instance
maps_heat = folium.Map(location=[40.755290, -73.987495], tiles="CartoDB Positron", zoom_start=10)

# Add heatmap to map instance
HeatMap(locations).add_to(maps_heat)

# Save the map to an HTML file
path_html = os.path.join(path_parent, 'html', 'nyc_heatmap.html')
maps_heat.save(path_html)
