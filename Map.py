import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
import folium

st.set_page_config(layout="wide")

geo_data_path = 'Data/south_africa_Province_level_1/south_africa_Province_level_1.shp'

@st.cache_resource
def read_geo_data(file_path):
    gdf = gpd.read_file(file_path)
    return gdf

def show_map_page():
    st.markdown("# Discover South Africa's Places 🌍")

    province_boundaries = read_geo_data(geo_data_path)

    my_map = folium.Map(
        location=[-30.5595, 22.9375],  # You can set the initial map location based on your data
        zoom_start=6,
        tiles="OpenStreetMap",
    )

    folium.GeoJson(province_boundaries).add_to(my_map)

    st_folium(my_map, width=1500, height=800)

show_map_page()
