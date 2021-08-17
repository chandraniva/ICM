"""
This script:
    -> Familiarizes the user with the basic usage of FITS file and the data it contains
    -> The various statistical properties of the data such as maximum, minimum,
       average and Standard deviation.

WARNING: The y map FITS file being called must be present in 'data'   
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

f = fits.open('../data/map2048_MILCA_Coma_20deg_G.fits')

f.info()    
print('\n')
print(f[1])     
print('\n')
print(f[1].header)
print('\n')

data = f[1].data

print(type(data))
print(data.shape)
print(data.dtype.name)
print("\nMin:",np.min(data))
print("\nMax:",np.max(data))
print("\nMean:",np.mean(data))
print("\nStd:",np.std(data))

from matplotlib.colors import TwoSlopeNorm

x_ticks = ['-10', '-5', '0', '5', '10' ]        
y_ticks = ['-10', '-5', '0', '5', '10' ]
t11 = [0,175,350,525,699]

plt.xticks(ticks=t11, labels=x_ticks, size=7)
plt.yticks(ticks=t11, labels=y_ticks, size=7)

norm = TwoSlopeNorm(vmin=data.min(), vcenter=0, vmax=data.max())
pc = plt.pcolormesh(data, norm=norm, cmap="seismic")
plt.imshow(data, cmap = 'seismic')
#plt.colorbar(pc)
cbar = plt.colorbar()
for t in cbar.ax.get_yticklabels():
     t.set_fontsize(7)
plt.xlabel("degrees",fontsize=8)
plt.ylabel("degrees",fontsize=8)
#plt.title("MILCA y map of Coma",fontsize=8)
plt.savefig("../images/figure 1.png", dpi = 600)
plt.show()