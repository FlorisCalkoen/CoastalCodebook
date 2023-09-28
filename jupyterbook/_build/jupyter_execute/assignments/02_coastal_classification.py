#!/usr/bin/env python
# coding: utf-8

# # Coastal classification 

# In[1]:


import os
import pathlib
import sys

# Make coastmonitor library importable by appending root to path
cwd = pathlib.Path().resolve()
sys.path.append(str(cwd.parent))

from utils.geometries import geo_bbox

