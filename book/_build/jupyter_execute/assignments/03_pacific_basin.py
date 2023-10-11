#!/usr/bin/env python

# In[1]:


import pathlib
import sys

# make coastpy library importable by appending root to path
cwd = pathlib.Path().resolve()
proj_dir = cwd.parent.parent
sys.path.append(str(proj_dir / "src"))


# In[2]:


# definitly not a best practice, but a workaround to avoid many warnings caused by shapely 2.0 release
import io
import warnings

import geopandas as gpd
import geoviews.tile_sources as gts
import numpy as np
import pandas as pd
import panel as pn
import requests
from tqdm import tqdm

from coastalcodebook.geometries import geo_bbox

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)


# In[3]:


DATA_DIR = proj_dir / "data"
coastsat_metadata_pacific_fp = DATA_DIR / "03_CoastSat_metadata_layer_Pacific.geojson"
metadata = gpd.read_file(coastsat_metadata_pacific_fp)

for c in ["Tier1Images", "Tier2Images", "S2Images", "pk"]:
    metadata[c] = metadata[c].astype("i8")

for c in ["TideRange", "WaveHeight", "RelativeTideRange"]:
    metadata[c] = metadata[c].astype("f8")

metadata.head()


# ## Part 1: compute relative tidal range with respect to waves
#
# todo: check with Kilian which waves heights he used
# mean_tidal_range / mean_wave_height

# In[4]:


metadata["RelativeTideRange"] = metadata["TideRange"] / metadata["WaveHeight"]
# metadata["RelativeTideRange"] = ...  # your code to compute tidal range over the wave height


# In[5]:


pn.extension()
title_bar = pn.Row(
    pn.pane.Markdown(
        "## Tide versus wave dominated coasts",
        style={"color": "black"},
        width=500,
        sizing_mode="fixed",
        margin=(10, 5, 10, 15),
    ),
    pn.Spacer(),
)

w_threshold = pn.widgets.FloatSlider(
    name="Threshold", start=0.1, end=10.0, step=0.1, value=1
)


@pn.depends(w_threshold.param.value)
def plot(threshold):
    wave_dominated = metadata[metadata["RelativeTideRange"] < threshold].copy()
    tide_dominated = metadata[metadata["RelativeTideRange"] > threshold].copy()

    return (
        gts.EsriImagery()
        * wave_dominated.hvplot(geo=True, color="blue", label="Wave dominated")
        * tide_dominated.hvplot(geo=True, color="green", label="Tide dominated")
    ).opts(legend_position="bottom_right")


app = pn.Column(
    title_bar,
    pn.Row(w_threshold),
    pn.Row(plot),
)
app


# In[6]:


from ipyleaflet import Map, basemaps

m = Map(basemap=basemaps.Esri.WorldImagery, scroll_wheel_zoom=True)
m.center = 37.768137, -122.511066
m.zoom = 16
m.layout.height = "800px"
m


# In[7]:


bbox = geo_bbox(m.west, m.south, m.east, m.north)


# In[8]:


bbox.explore()


# In[9]:


transects = gpd.read_file(DATA_DIR / "03_CoastSat_transect_layer.geojson")
transects_roi = gpd.sjoin(transects, bbox)


# In[10]:


transects_roi.explore()


# In[24]:


TIMEOUT_SEC = 5  # default timeount in seconds

# Get the transect id's by saving the transects in our region of interest as a list.
transect_ids = transects_roi.TransectId.to_list()

# Here we download the data per transect, but if it takes too long we default to Ocean beach, California.
try:
    data = []
    for transect_id in tqdm(transect_ids):
        url = url = f"http://coastsat.wrl.unsw.edu.au/time-series/{transect_id}/"
        # Pandas.read_csv() can handle url's but it doesn't accept a timeout argument,
        # so we download the data via requests.
        r = requests.get(url, timeout=TIMEOUT_SEC).content
        s = pd.read_csv(
            io.StringIO(r.decode("utf-8")),
            header=None,
            names=["date", "shoreline_position"],
        )
        s["date"] = pd.to_datetime(s["date"])
        s = s.set_index("date").replace({"None": np.nan}).astype("f8")
        s.name = transect_id
        data.append(s)
    column_names = [s.name for s in data]
    shorelines = pd.concat(data, axis=1)
    shorelines.columns = column_names

except:
    # If it takes too long to get the data from the server, default to Ocean Beach, California.
    # First set the map to that area, so that we have the correct bbox.
    m.center = 37.768137, -122.511066
    m.zoom = 16
    m.layout.height = "800px"
    bbox = geo_bbox(m.west, m.south, m.east, m.north)
    transects_roi = gpd.sjoin(transects, bbox)
    shorelines_fp = DATA_DIR / "03_shorelines_ocean_beach.parquet"
    shorelines = pd.read_parquet(shorelines_fp)


# In[25]:


shorelines.head()


# ##

# # check this for inspiration on how to clor the plot> https://foundations.projectpythia.org/core/xarray/enso-xarray.html

# In[26]:


pn.extension()
title_bar = pn.Row(
    pn.pane.Markdown(
        "## Historical shoreline series",
        style={"color": "black"},
        width=500,
        sizing_mode="fixed",
        margin=(10, 5, 10, 15),
    ),
    pn.Spacer(),
)

options = transects_roi.TransectId.to_list()
transect_slider = pn.widgets.Select(
    name="Transect", options=options, value=np.random.choice(options)
)


@pn.depends(transect_slider.param.value)
def plot_transects(transect_id):
    transect = transects_roi.loc[transects_roi["TransectId"] == transect_id].copy()

    return (
        gts.EsriImagery()
        * transects_roi.hvplot(geo=True, color="blue")
        * transect.hvplot(geo=True, color="red")
    )


@pn.depends(transect_slider.param.value)
def plot_series(transect_id):
    shoreline_selected = shorelines.hvplot(x="date", y=[transect_id], color="red")
    shorelines_ = shorelines[
        shorelines.columns.difference([transect_slider.value])
    ].hvplot(x="date", alpha=0.4)

    return shorelines_ * shoreline_selected


app = pn.Column(
    title_bar,
    pn.Row(transect_slider),
    pn.Row(pn.Column(plot_transects), plot_series),
)
app


# In[27]:


mei_fp = DATA_DIR / "03_meiv2.data"
mei = (
    pd.read_csv(mei_fp, delim_whitespace=True, index_col=0, header=None)
    .reset_index()
    .rename({0: "year"}, axis="columns")
    .melt(id_vars="year", var_name="month")
)
mei["date"] = pd.to_datetime(mei["year"].astype(str) + "-" + mei["month"].astype(str))
mei = (
    mei.drop(["year", "month"], axis="columns")
    .set_index("date")
    .sort_index()
    .replace({-999: np.nan})
)
mei.hvplot(x="date")


# In[28]:


mei_interp = mei.reindex(shorelines.index, method="nearest")


# In[29]:


shorelines_ = shorelines.copy()
shorelines_.index = mei_interp.value.to_list()
shorelines_.hvplot(kind="scatter")


# In[30]:


shorelines_ = shorelines.diff().copy()
shorelines_.index = mei_interp.value.to_list()
shorelines_.hvplot(kind="scatter", alpha=0.2, color="blue")


# In[ ]:


# In[ ]:
