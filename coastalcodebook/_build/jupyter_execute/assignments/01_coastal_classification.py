#!/usr/bin/env python
# coding: utf-8

# # Stacking 6 years of imagery into a GIF
# 
# We'll load all the [Landsat-8 (Collection 2, Level 2)](https://planetarycomputer.microsoft.com/dataset/landsat-8-c2-l2) data that's available from [Microsoft's Planetary Computer](https://planetarycomputer.microsoft.com/) over a small region on the coast of [Cape Cod](https://www.google.com/maps/place/Chatham,+MA/@41.7498076,-70.2026227,10.73z/data=!4m13!1m7!3m6!1s0x89fb15440149e94d:0x1f9c0efa001cb20b!2sCape+Cod!3b1!8m2!3d41.6687897!4d-70.2962408!3m4!1s0x89fb142168afbe53:0x714436ec7d485a53!8m2!3d41.6821432!4d-69.9597359), Massachusetts, USA.
# 
# 
# Using nothing but standard xarray syntax, we'll mask cloudy pixels with the Landsat QA band and reduce the data down to biannual median composites.
# 
# [Animated](https://geogif.readthedocs.io/en/latest/) as a GIF, we can watch the coastline move over the years due to [longshore drift](https://en.wikipedia.org/wiki/Longshore_drift).
# 
# Planetary Computer is Microsoft's open Earth data initiative. It's particularly nice to use, since they also maintain a [STAC API](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/) for searching all the data, as well as a browseable [data catalog](https://planetarycomputer.microsoft.com/catalog). It's free for anyone to use, though you have to [sign your requests](https://planetarycomputer.microsoft.com/docs/concepts/sas/) with the `planetary_computer` package to prevent abuse. If you [sign up](https://planetarycomputer.microsoft.com/account/request), you'll get faster reads.

# In[1]:


get_ipython().run_line_magic('config', "InlineBackend.figure_formats = ['png2x']")


# In[2]:


# import coiled
import distributed
import dask
import pystac_client
import planetary_computer as pc
import ipyleaflet
import IPython.display as dsp
# import geogif
import stackstac


# Using a cluster will make this _much_ faster. Particularly if you're not in Europe, which is where this data is stored.
# 
# You can sign up for a Coiled account and run clusters for free at https://cloud.coiled.io/ — no credit card or username required, just sign in with your GitHub or Google account, then connect to your cloud provider account (AWS or GCP).

# In[3]:


# cluster = coiled.Cluster(
#     name="stackstac-eu",
#     n_workers=20,
#     package_sync=True,
#     backend_options={"region": "eu-central-1"},
#     # ^ Coiled doesn't yet support Azure's West Europe region, so instead we'll run on a nearby AWS data center in Frankfurt
# )
# client = distributed.Client(cluster)
# client


# Interactively pick the area of interest from a map. Just move the map around and re-run all cells to generate the timeseries somewhere else!

# In[4]:


m = ipyleaflet.Map(scroll_wheel_zoom=True)
m.center = 41.64933994767867, -69.94438630063088
m.zoom = 12
m.layout.height = "800px"
m


# In[5]:


bbox = (m.west, m.south, m.east, m.north)


# ## Search for STAC items
# 
# Use [pystac-client](https://github.com/stac-utils/pystac-client) to connect to Microsoft's STAC API endpoint and search for Landsat-8 scenes.

# In[6]:


catalog = pystac_client.Client.open('https://planetarycomputer.microsoft.com/api/stac/v1')

search = catalog.search(
    collections=['landsat-8-c2-l2'],
    bbox=bbox,
)


# Load and sign all the STAC items with a token from Planetary Computer. Without this, loading the data will fail.

# In[7]:


get_ipython().run_cell_magic('time', '', 'items = pc.sign(search)\nlen(items)\n')


# These are the footprints of all the items we'll use:

# In[8]:


dsp.GeoJSON(items.to_dict())


# ## Create an xarray with stacksatc
# 
# Set `bounds_latlon=bbox` to automatically clip to our area of interest (instead of using the full footprints of the scenes).

# In[9]:


# %%time
# stack = stackstac.stack(items, bounds_latlon=bbox)
# stack


# And that's it for stackstac! Everything from here on is just standard xarray operations.

# In[10]:


# # use common_name for bands
# stack = stack.assign_coords(band=stack.common_name.fillna(stack.band).rename("band"))
# stack.band


# See how much input data there is for just RGB. This is the amount of data we'll end up processing

# In[11]:


# stack.sel(band=["red", "green", "blue"])


# ## Mask cloudy pixels using the QA band
# 
# Use the bit values of the Landsat-8 QA band to mask out bad pixels. We'll mask pixels labeled as dilated cloud, cirrus, cloud, or cloud shadow. (By "mask", we mean just replacing those pixels with NaNs).
# 
# See page 14 on [this PDF](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-1619_Landsat-8-9-C2-L2-ScienceProductGuide-v4.pdf) for the data table describing which bit means what.

# In[12]:


# # Make a bitmask---when we bitwise-and it with the data, it leaves just the 4 bits we care about
# mask_bitfields = [1, 2, 3, 4]  # dilated cloud, cirrus, cloud, cloud shadow
# bitmask = 0
# for field in mask_bitfields:
#     bitmask |= 1 << field

# bin(bitmask)


# In[13]:


# qa = stack.sel(band="QA_PIXEL").astype("uint16")
# bad = qa & bitmask  # just look at those 4 bits
# good = stack.where(bad == 0)  # mask pixels where any one of those bits are set


# In[14]:


# # What's the typical interval between scenes?
# good.time.diff("time").dt.days.plot.hist();


# ## Make biannual median composites
# 
# The Landsat-8 scenes appear to typically be 5-15 days apart. Let's composite that down to a 6-month interval.
# 
# Since the cloudy pixels we masked with NaNs will be ignored in the `median`, this should give us a decent cloud-free-ish image for each.

# In[15]:


# # Make biannual median composites (`2Q` means 2 quarters)
# composites = good.resample(time="2Q").median("time")
# composites


# Pick the red-green-blue bands to make a true-color image.

# In[16]:


# rgb = composites.sel(band=["red", "green", "blue"])
# rgb


# Some final cleanup to make a nicer-looking animation:
# 
# * Forward-fill any NaN pixels from the previous frame, to make the animation look less jumpy.
# * Also skip the first frame, since its NaNs can't be filled from anywhere.

# In[17]:


# cleaned = rgb.ffill("time")[1:]


# ## Render the GIF
# 
# Use [GeoGIF](https://geogif.readthedocs.io/en/latest/) to turn the stack into an animation. We'll use [dgif](https://geogif.readthedocs.io/en/latest/api.html#dask-dgif) to render the GIF on the cluster, so there's less data to send back. (GIFs are a lot smaller than NumPy arrays!)

# In[18]:


# client.wait_for_workers(20)


# In[19]:


# %%time
# gif_img = geogif.dgif(cleaned).compute()


# In[20]:


# we turned ~7GiB of data into a 4MB GIF!
# dask.utils.format_bytes(len(gif_img.data))


# In[21]:


# gif_img


# In[ ]:




