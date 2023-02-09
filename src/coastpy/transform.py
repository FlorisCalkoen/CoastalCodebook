from typing import Union

import geopandas as gpd
import pandas as pd
from geopandas.array import GeometryDtype
from shapely import wkb, wkt
from shapely.geometry import Point


def geometry_to_coords(data: Union[gpd.GeoDataFrame, gpd.GeoSeries, GeometryDtype]):
    """Explode linestring geometry and return lon, lat coordinates as seperate variables."""

    if isinstance(data, GeometryDtype):
        data = gpd.GeoSeries(data)

    exploded = data.geometry.apply(lambda x: x.coords).explode()

    if isinstance(data, gpd.GeoSeries):
        gs = gpd.GeoSeries(exploded.apply(lambda x: Point(x)))
        return (gs.x.values, gs.y.values)

    elif isinstance(data, gpd.GeoDataFrame):
        df = pd.DataFrame(
            exploded.to_list(), index=exploded.index, columns=["lon", "lat"]
        )
        return data.join(df).reset_index().rename(columns={"index": "group"})


def to_geodataframe(df, crs, geometry="geometry"):
    df = df.copy()

    if len(df) > 0:
        if isinstance(df[geometry].iloc[0], bytes):
            df[geometry] = df[geometry].apply(wkb.loads)

        elif isinstance(df[geometry].iloc[0], str):
            df[geometry] = df[geometry].apply(wkt.loads)

    return gpd.GeoDataFrame(df, geometry=geometry, crs=crs)


def to_dataframe(df, encoder, geometry="geometry"):
    df = df.copy()
    df = pd.DataFrame(df)
    df[geometry] = df[geometry].apply(encoder)
    return df


def to_utm_zone(geometry: GeometryDtype, src_crs: Union[str, int]) -> tuple:
    """Transform caostline to local UTM CRS.

    Args:
        coastlinestring (LineString): Coastline described by Shapely LineString.
        crs (str): pyproj crs string # TODO: type check argument for pyproj.crs

    Returns:
        tuple: (coastline, local_utm)
    """
    cl = gpd.GeoDataFrame(geometry=[coastline], crs=datum_crs)
    local_utm = cl.estimate_utm_crs()
    cl = cl.to_crs(local_utm)
    return cl.iloc[0]["geometry"], local_utm


def mask_not_bbox(df: gpd.GeoDataFrame, bbox: list) -> gpd.GeoDataFrame:
    df = df.copy()
    xmin, ymin, xmax, ymax = bbox
    df = df.cx[xmin:xmax, ymin:ymax]
    return df
