# -*- coding: utf-8 -*-

# Import libraries
import os
from pathlib import Path
import pandas as pd
import geopandas as gpd
import folium

# Read the MTA Subway Stations data
columns = ["Line", "Stop Name",	"GTFS Latitude", "GTFS Longitude"]

path_parent = Path(os.path.dirname(os.path.abspath(__file__))).parent
path_data = os.path.join(path_parent, 'data', 'MTA_Subway_Stations.csv')

df = pd.read_csv(path_data, usecols=columns)

df.rename(columns={"GTFS Latitude": "Latitude", "GTFS Longitude": "Longitude"}, inplace=True)

# Create geometry column
geometry = gpd.points_from_xy(df["Longitude"], df["Latitude"])

# Create GeoDataFrame
geo_df = gpd.GeoDataFrame(df, geometry=geometry)

# Create Marker column
geo_df["Marker"] = geo_df.apply(lambda row: folium.Marker(
    location=[row["Latitude"], row["Longitude"]],
    popup="Stop Name: {0}<br>Line: {1}".format(row["Stop Name"], row["Line"])), 
    axis=1)

# Create a Map instance
map_marker = folium.Map(location=[40.755290, -73.987495], 
    tiles="CartoDB Positron", zoom_start=10)

# Add markers to map instance
for rows in geo_df.iterrows():
    map_marker.add_child(rows[1]["Marker"])

# Save the map to an HTML file
path_html = os.path.join(path_parent, 'html', 'nyc_marker.html')
map_marker.save(path_html)
