# -*- coding: utf-8 -*-


pip install earthpy

from glob import glob

import earthpy as epy  
import earthpy.plot as eplt
   

import rasterio as ras

import matplotlib.pyplot as plt    
import numpy as np
# to use colors to differentiate
from matplotlib.colors import ListedColormap

import plotly.graph_objects as go     

#Treatment for division by zero
#Treatment for invalid floating-point operation
np.seterr(divide='ignore', invalid='ignore')

#Read bands and stack them to numpy array
sent_band = glob("/content/data*?*.tiff")

sent_band.sort()
print(sent_band)

arry = []

for i in sent_band:
  with ras.open(i, 'r') as f:
    arry.append(f.read(1))
    
nar = np.stack(arry)

# bands visualization
#cmap is for colormap instance
eplt.plot_bands(nar, 
              cmap = 'terrain', 
              figsize = (20, 12), 
              cols = 6, 
              cbar = False)
plt.show()

# Red is band 3, green is band 2, blue is band 1

rgb = eplt.plot_rgb(nar, 
                  rgb=(3,2,1), 
                  figsize=(10, 16))

plt.show()

# RGB Composite Image with Strech

eplt.plot_rgb(nar,
            rgb=(3, 2, 1),
            stretch=True,
            str_clip=0.2,
            figsize=(10, 16))

plt.show()

colors = ['orange', 'grey', 'lightsteelblue', 'coral', 'greenyellow', 'blue',
          'plum', 'firebrick', 'sienna', 'crimson', 'darksalmon', 'olive']
          
#hist method to form histogram
eplt.hist(nar, 
        colors = colors,        
        title=[f'band-{i}' for i in range(1, 13)], 
        cols=3, 
        alpha=0.5, 
        figsize = (12, 10))

plt.show()

#MNDWI = (Green - SWIR) / (Green + SWIR)
#green is band 3 and SWIR is band 11

mndwi =  epy.spatial.normalized_diff(nar[2], nar[10])

#to plot all bands in a stack
eplt.plot_bands(mndwi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
