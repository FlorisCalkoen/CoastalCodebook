import ipyleaflet
from ipyleaflet import Map, Marker, ScaleControl, basemaps
from ipywidgets import HTML


def plot_esri_basemap(
    lon: float, lat: float, zoom: int, name: str
) -> ipyleaflet.leaflet.Map:
    """Plot IPyleaflet map with ESRI basemap tiles.

    Args:
        lon (float): Longitude in degrees.
        lat (float): Latitude in degrees.
        zoom (int): Zoom level following OSM slippy map tiles.
        name (str): Name for the marker.

    Returns:
        ipyleaflet.leaflet.Map: Basemap with ESRI World Imagery.
    """
    m = Map(basemap=basemaps.Esri.WorldImagery, scroll_wheel_zoom=True)
    center = (lat, lon)
    marker = Marker(location=center)
    m.add_layer(marker)
    m.center = center
    m.zoom = zoom
    m.layout.height = "800px"
    m.add_control(ScaleControl(position="bottomleft"))
    title = HTML()
    title.value = name
    marker.popup = title
    return m
