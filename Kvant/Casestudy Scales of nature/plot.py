import numpy as np
from matplotlib import pyplot as plt

size = np.array([5.3*10**-14,  2.75*10**-10, 10**-7,  2*10**-6,  1.7, 30,        6.4*10**6, 7*10**7,    7*10**8,  7*10**6,    10**4 ])
mass = np.array([1.67*10**-27, 2.99*10**-26, 10**-18, 6.5*10**-16, 70,  1.9*10**5, 6*10**24,  1.9*10**27, 2*10**30, 2.4*10**30, 7*10**30])

fig, ax = plt.subplots()
ax.set_xscale('log')
ax.set_yscale('log')
ax.scatter(size, mass)
ax.set_xlabel('Size (m)')
ax.set_ylabel('Mass (kg)')
ax.set_title('Scales of Nature')
fig.savefig('Kvant/Casestudy Scales of nature/scales_of_nature.png')

'''
* Hydrogen atom 5.3*10**-14, 1.67*10**-27
* Water molecule 2.75*10**-10, 2.99*10**-26
* Virus 10**-7, 10**-18
* Bacteria 2*10**-6, 6.5*10-16
* Human 1.7, 70
* Blue whale 30, 1.9*10**5
* Earth 6.4*10**6, 6*10**24
* Jupiter 7*10**7, 1.9*10**27
* Sun 7*10**8, 2*10**30
* White dwarf 7*10**6 2.4*10**30
* Neutron star 10**4 7*10**30
* Black hole 
* Milky Way
* Local Group
* Virgo Supercluster
* Observable Universe
'''