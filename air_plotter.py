#!/Applications/anaconda/bin/python

import numpy as np
import netCDF4 as netcdf
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic

fname = 'air.mon.mean.nc'
with netcdf.Dataset( fname, 'r' ) as fh:
    p_levs = fh.variables['level'][:]
    lat = fh.variables['lat'][:]
    lon = fh.variables['lon'][:]
    time = fh.variables['time'][:]
    air = fh.variables['air'][:]

air = (air * 0.01) + 127.65


fig, ax = plt.subplots( figsize=(15,12) )
cmap = plt.cm.gist_rainbow_r

#m = Basemap(projection='ortho',lat_0=60,lon_0=180)
m = Basemap(lat_0=0,lon_0=180)
m.drawcoastlines()
m.drawmeridians(range(0,360,45), labels=[1,0,0,1])
m.drawparallels(range(-90,90,30), labels=[1,0,0,1])

air_cyclic, lons_cyclic = addcyclic(air[0,0,:,:], lon)
lon2d, lat2d = np.meshgrid(lons_cyclic, lat)
x, y = m(lon2d, lat2d)

#m.imshow( air[0,0,:,:], interpolation='none', origin='upper' )
m.pcolor( x, y, air_cyclic, cmap=cmap )
#m.contourf( x, y, air[0,0,:,:])

labels = np.linspace( int(air_cyclic.min()), int(air_cyclic.max()), 11)
cb = m.colorbar( size='2%' )
cb.set_ticks(labels)
cb.set_ticklabels(labels)
plt.show()
