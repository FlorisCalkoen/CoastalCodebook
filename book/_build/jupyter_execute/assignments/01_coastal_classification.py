#!/usr/bin/env python

# # Characterization of Coastal Systems
#
# Welcome to the first notebook exercise of Coastal Systems (TU Delft, MSc Coastal Engineering)! This is the first year that we will experiment with notebooks in this course. With these notebooks we hope to provide you with interactive course material that helps you better understand the processes and concepts that we teach in this course. Please let us know how you find the notebooks - we appreciate your feedback!
#
# Chapter 2 of [Coastal Dynamics Open Textbook](https://textbooks.open.tudelft.nl/textbooks/catalog/view/37/92/383-1) describes the large geographical variation of coasts across the world. It explains how the coasts that we have today are shaped by both present-day processes and processes millions years ago. It distinguishes between three different order of features, which are associated to different orders of of time. In this notebook we will look at coastal systems at these different orders of scale.

# ## Import libraries that we use for our analysis
#
# In the two cells below we import the libraries that we need for the analysis. We also set some path settings to load the data and source code. For example, in the cell below we add the `src` directory to the system path, which allows us to import generic functions from `../../src/coastpy`.

# In[1]:


import os
import pathlib
import sys

# make coastpy library importable by appending root to path
cwd = pathlib.Path().resolve()
proj_dir = cwd.parent.parent  # this is the root of the CoastalCodeBook
sys.path.append(str(proj_dir / "src"))


# In[2]:


import warnings

os.environ["USE_PYGEOS"] = "0"  # use shapely 2.0 instead of PYGEOS and silence warnings

import colorcet as cc
import dask.dataframe as dd
import geopandas as gpd
import numpy as np
import pandas as pd
import panel as pn

pn.extension()

from coastalcodebook.geometries import geo_bbox

# definitly not a best practice, but a workaround to avoid many warnings triggered by shapely 2.0 release
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

DATA_DIR = proj_dir / "data"
coastal_systems_fp = DATA_DIR / "01_coastal_systems.gpkg"


# ## Exercise 1: Plate tectonics

# In this notebook we will start with the broadest (or first order) features of the coast that cover large geographical distances (thousands of kilometres) and are linked to the long-term geological process of plate tectonics. We will do so by using earthquake data from the [USGS](https://earthquake.usgs.gov/earthquakes/search/). The dataset we load contains a sample (10\%) of observed eartquakes between Jan 2000 and Dec 2018. Why earthquake data? Earthquake data reveals geologists the mysteries of the deep, but also for coastal researchers the data is insightful. Let's first load the data by running the next cells.

# ### Load the earthquake data
#
# We load the data (tabular data including geometries) and index the columns to only keep the data in memory that we actually need. In total the dataset contains 2.2 million earthquakes, but here we use a sample (10\%), so the data contains approx. 220k eartquake entries. If you find that the interactive panel responds slow to how you adjust the widgets, please consider to take another sample. You can do so by uncommenting the sample line in the next cell. So if you set frac=0.1 you have a dataframe with approx. 22k unique earthquakes over the world.
#

# In[3]:


WEB_MERCATOR_LIMITS = (
    -20037508.342789244,
    20037508.342789244,
)  # max polar latitudes that can be handled in World Mercator

df = (
    dd.read_parquet(DATA_DIR / "01_earthquakes_sample.parquet")
    .sample(
        frac=0.1
    )  # uncomment this line if loading the data takes too long on your computer
    .set_index("time")
    .compute()
    .tz_localize(None)
    .sort_index()
)


# To save memory we drop most of the columns. Also we drop the polar latitudes that cannot be displayed in the web mercator projection.
df = df[["mag", "depth", "latitude", "longitude", "place", "type"]][
    df["northing"] < WEB_MERCATOR_LIMITS[1]
]
df.head()


# ### Visualization of the earthquake data
#
# To explore the data we use visualization tools from the [Holoviz project](https://holoviz.org/) that makes high-level tools to simplify visualization in Python. In the next cell we enable the interactive mode on the data dataframe, create widgets to explore the data and filter the dataframe accordingly. To explore the eartquake data we create an overlay of the eartquakes on a tileset of ESRI Imagery. Please note that the code in the next cell will only do the computations and store the result in an object called `panel`. To actually see the results you have to run one more cell; the one that calls this object panel.
#
#

# In[4]:


pn.extension()
title_bar = pn.Row(
    pn.pane.Markdown(
        "## Exercise 1: Plate tectonics & first-order coastal features",
        style={"color": "black"},
        width=800,
        sizing_mode="fixed",
        margin=(10, 5, 10, 15),
    ),
    pn.Spacer(),
)

# define widgets that can be used to index the data
magnitude_slider = pn.widgets.RangeSlider(
    name="Earthquake magnitude [Richter]", start=0.1, end=10
)
depth_slider = pn.widgets.RangeSlider(name="Earthquake depth [km]", start=0.1, end=650)
date_slider = pn.widgets.DateRangeSlider(
    name="Date", start=df.index[0], end=df.index[-1]
)
column_types = pn.widgets.Select(options=["mag", "depth"])


@pn.depends(
    magnitude_slider.param.value_start,
    magnitude_slider.param.value_end,
    depth_slider.param.value_start,
    depth_slider.param.value_end,
    date_slider.param.value_start,
    date_slider.param.value_end,
    column_types.param.value,
)
def plot_earthquake_panel(
    magnitude_start,
    magnitude_end,
    depth_start,
    depth_end,
    date_start,
    date_end,
    column_type,
):
    panel = df[(df.mag > magnitude_start) & (df.mag < magnitude_end)]

    panel = df[
        (df.mag > magnitude_start)
        & (df.mag < magnitude_end)
        & (df.depth > depth_start)
        & (df.depth < depth_end)
        & (df.index >= date_start)
        & (df.index <= date_end)
    ]
    # inverted fire colormap from colorcet
    cmap = cc.CET_L4[::-1]
    colorbar_labels = {"mag": "Magnitude [Richter]", "depth": "Earthquake depth [km]"}

    return panel.hvplot.points(
        x="longitude",
        y="latitude",
        geo=True,
        color=column_type,
        global_extent=True,
        tiles="ESRI",
        frame_width=900,
        ylabel="Latitude [deg]",
        xlabel="Longitude [deg]",
        cmap=cmap,
        tools=["tap"],
        hover_cols=["place", "time"],
        logz=True,
        clim=(1, None),
        clabel=colorbar_labels[column_type],
    )


cmap = cc.CET_L4[::-1]  # inverted fire colormap from colorcet

earthquake_panel = pn.Column(
    title_bar,
    pn.Row(column_types),
    pn.Row(pn.Column(magnitude_slider, depth_slider)),
    pn.Row(depth_slider),
    pn.Row(date_slider),
    pn.Row(plot_earthquake_panel),
)


# **If the visualization is too slow, please follow the instructions in loading the data for taking a sample.**
#
# After running the cell below you will have a panel with several widgets to index the eartquake data; by magnitude, depth and time, while the colors on the map show either the magintude or the depth of the earthquakes.

# In[5]:


earthquake_panel


# ### Explore the earthquake data & questions
#
# 1) How do the earthquake magnitude and earthquake depth relate to the coasts that we see? (Hint: See Figure 2.3 in the textbook and consider how deep under the ground the plates are moving. Extra hint: How do earthquake magnitude and depth differ for convergent and divergent plate boundaries?)
#
# 2) Earthquake data support one of the most fundamental processes in the geology: plate tectonics. Although plate tectonics is a relatively slow process that acts on the [geological time scale](https://cdn.britannica.com/67/73167-050-B9A74092/chart.jpg), it has had an enormous impact on the formation of coastlines and determines the broadest features of the coast. What are two important inherited aspects of this process? (Hint: see Figure 2.10 and Sec. 2.3.3 in the textbook.)
#
# 3) In 1971 Inman, D. L. & Nordstrom, C. E. used plate tectonics to classify the coast. Explain the classification that they introduced. What are the three different classes that they distinguish? How do they match with the earthquake data as you can explore in the panel?
#
# 4) Can you identify or predict areas around the world where you will find the coasts that are distinguished by Inman, D. L. & Nordstrom, C. E.? For instance, what kind of coasts do you have in Chili? And how are they different to the east coast of the USA? And what is characteristic about the East China sea?
#
# 5) Inman, D. L. & Nordstrom (1971) further distinguish Afro-trailing-edge coasts and Amero-trailing-edge coasts based on differences in sediment supplies. What is the main cause of these differences in sediment supply? And how do you expect the differences in sediment input to show in the coastal geomorphology?

# ## Exercise 2: Process-based coastal classification
#
# In the section part of this notebook we will explore several coastal systems around the world considering the second and third order scale of features. In chapter two of the Coastal Dynamics open textbook it is explained how coastal systems can be classified according to the processes that characterize these systems. For example, one of the figures (below) shows how the relative influence of fluvial, wave and tidal processes influences the shape of coastal features. The idea of this exercise is that you identify the signatures of the processes that are introduced in chapter 2 in several coastal systems around the world.
#
# ![image](./figures/01_coastal_forcing.png)

# ### The coastal systems data
#
# In the cell below we define a small plot function that generates a ESRI World Imagery basemap given a longitude, latitude, zoom level and name. Also, a small sheet of coastal systems around the world is loaded into `geopandas`, a Python library for geospatial tabular data. In the cells afterwards we sample this dataframe and show the coastal system on a map. Since the sample is random you might encounter the same coastal system multiple times; then you can just run the cell again to get another 'coastal draw'.
#

# In[6]:


coastal_systems = gpd.read_file(coastal_systems_fp)


# In[7]:


pn.extension()
title_bar = pn.Row(
    pn.pane.Markdown(
        "## Exercise 2: Coastal system characterization",
        style={"color": "black"},
        width=800,
        sizing_mode="fixed",
        margin=(10, 5, 10, 15),
    ),
    pn.Spacer(),
)

options = coastal_systems.name.to_list()
coastal_systems_slider = pn.widgets.Select(
    name="Coastal system", options=options, value=np.random.choice(options)
)


@pn.depends(coastal_systems_slider.param.value)
def plot_coastal_system(name):
    system = coastal_systems.loc[coastal_systems["name"] == name].copy()
    west, south, east, north = system[
        ["west", "south", "east", "north"]
    ].values.flatten()

    return system.hvplot.points(
        x="lon",
        y="lat",
        geo=True,
        color="red",
        alpha=0,
        xlim=(west, east),
        ylim=(south, north),
        tiles="ESRI",
        frame_width=1100,
        ylabel="Latitude [deg]",
        xlabel="Longitude [deg]",
    )


app = pn.Column(
    title_bar,
    pn.Row(coastal_systems_slider),
    pn.Row(plot_coastal_system),
)
app


# ### Explore the coastal systems
#
# While sampling over a range of coastal systems, try to answer the following questions.
#
# 1. Find and compare a heavily engineered river-dominated delta and a more natural river-dominated delta
# 2. Compare the scale of the biggest and smallest tidal basin in the dataset
# 3. Find the estuarine and deltaic systems with a spit
# 4. Compare and contrast wave-dominated deltas with high and low sediment supply. How can you tell?
# 5. Find a tidal estuary with large fine (muddy) sediment supply, then find one with a large coarse (sandy) sediment supply. How can you tell the difference?
# 6. The eastern and western tips of the Dutch and German Wadden Islands are very different beach ridge environments. How might differences in sediment supply explain this? Where is the sediment coming from?
# 7. The Dune du Pilat in France is one of the world's largest coastal sand dunes (it is also one of the coolest and you should definitely visit if you get the chance!). Why is it located on the east side of Arcachon Inlet and not the west?
# 8. Look at the northern Jiangsu coast in China. What might explain the limited sediment supply in this location?
# 9. Find an estuary or tidal bay with extensive intertidal flats. Do you see salt marshes or mangrove forests nearby?  Why or why not?
# 10. Find an inlet with jetties. How might this affect the way it evolves?
# 11. Find a delta/estuary/inlet whose shape is constrained by the presence of rocky coastal features.
# 12. The Albufeira Lagoon in Portugal opens and closes seasonally. In the image shown, is it open or closed? When and how might it open or close?
# 13. Find examples of heavily urbanized estuaries. How might these human interventions influence the natural processes there?
# 14. Based on these satellite images, which is the most beautiful site? Taking a moment to appreciate the beauty of these natural systems is an important part of your job as coastal engineers.

# In[8]:


from coastal_dynamics.visualization import plot_esri_basemap

# In[9]:


m = plot_esri_basemap(-9.181333, 38.510379, 13, "Lagoa de Albufeira")
m


# In[10]:


bbox = geo_bbox(m.west, m.south, m.east, m.north)


# In[11]:


bbox.explore()


# In[12]:


m.west, m.south, m.east, m.north


# In[13]:


import shapely

albufeira = {
    "name": "Lagoa de Albofeira",
    "lon": -9.181333,
    "lat": 38.510379,
    "zoom": 13,
    "west": -9.276924133300783,
    "south": 38.483560395392516,
    "east": -9.085865020751955,
    "north": 38.53729004998249,
    "geometry": shapely.geometry.point.Point([-9.181333, 38.510379]),
}
albufeira = gpd.GeoDataFrame([albufeira], crs=4326)


# In[14]:


coastal_systems = pd.concat([albufeira, coastal_systems])
coastal_systems = coastal_systems[coastal_systems["name"] != "Albufeira"]


# In[15]:


coastal_systems.drop_duplicates().to_file(38.53729004998249)


# In[51]:


coastal_systems2


# In[50]:


coastal_systems2.explore()


# In[ ]:
