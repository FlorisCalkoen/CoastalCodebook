from typing import Any, Dict, List, Union

import geopandas as gpd
import shapely
from pyproj import Transformer


def build_bbox(min_lon, min_lat, max_lon, max_lat, src_crs, crs):
    """
    Build a latitude / longitude bounding box from the coordinates.
    """
    # minimum / maximum points from the dataset
    # left, bottom, right, top = (-5802250.0, -622000.0, -5519250.0, -39000.0)
    points = [
        [min_lon, max_lon, max_lon, min_lon],
        [min_lat, min_lat, max_lat, max_lat],
    ]

    transformer = Transformer.from_crs(src_crs, crs, always_xy=True)
    lons, lats = transformer.transform(*points)

    west = min(lons)
    east = max(lons)
    north = max(lats)
    south = min(lats)
    return [west, south, east, north]


def geometry_to_bbox(geometry: Dict[str, Any]) -> List[float]:
    """Extract the bounding box from a geojson geometry

    Args:
        geometry : GeoJSON geometry dict

    Returns:
        list: Bounding box of geojson geometry, formatted according to:
        https://tools.ietf.org/html/rfc7946#section-5
    """
    coords = geometry["coordinates"]

    lats: List[float] = []
    lons: List[float] = []

    def extract_coords(coords: List[Union[List[float], List[List[Any]]]]) -> None:
        for x in coords:
            # This handles points
            if isinstance(x, float):
                assert isinstance(
                    coords[0], float
                ), f"Type mismatch: {coords[0]} is not a float"
                assert isinstance(
                    coords[1], float
                ), f"Type mismatch: {coords[1]} is not a float"
                lats.append(coords[0])
                lons.append(coords[1])
                return
            if isinstance(x[0], list):
                extract_coords(x)  # type:ignore
            else:
                lat, lon = x
                lats.append(lat)  # type:ignore
                lons.append(lon)  # type:ignore

    extract_coords(coords)

    lons.sort()
    lats.sort()

    bbox = [lats[0], lons[0], lats[-1], lons[-1]]

    return bbox


def bbox_to_geometry(bbox: List[float]) -> Dict:
    """Use shapely.geometry.shape to cast to shapeley geom"""
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [bbox[2], bbox[1]],
                [bbox[2], bbox[3]],
                [bbox[0], bbox[3]],
                [bbox[0], bbox[1]],
                [bbox[2], bbox[1]],
            ]
        ],
    }


def geo_bbox(
    min_lon: float,
    min_lat: float,
    max_lon: float,
    max_lat: float,
    src_crs="EPSG:4326",
    dst_crs="EPSG:4326",
) -> gpd.GeoDataFrame:
    """GeoDataFrame with a bounding box that can be used for various gis operations.
    Args:
        min_lon (float): most eastern longitude
        min_lat (float): most northern latitude
        max_lon (float): most wester longitude
        max_lat (float): most soutern latitude
        src_crs (str, optional): Valid EPSG string or number (int). Defaults to "EPSG:4326".
        dst_crs (str, optional): Valid EPSG string or number (int). Defaults to "EPSG:4326".

    Returns:
        gpd.GeoDataFrame: GeoDataFrame with bounding box as geometry.
    """

    bbox = [min_lon, min_lat, max_lon, max_lat]
    bbox = bbox_to_geometry(bbox)
    bbox = shapely.geometry.shape(bbox)
    return gpd.GeoDataFrame(geometry=[bbox], crs=src_crs).to_crs(dst_crs)


def get_xy_range(gdf):
    """min, max lon/lat formatted as xy range for geoviews."""
    x_range = tuple(gdf.total_bounds[[0, 2]])
    y_range = tuple(gdf.total_bounds[[1, 3]])
    return x_range, y_range
