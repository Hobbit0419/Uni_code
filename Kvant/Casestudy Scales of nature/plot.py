import numpy as np
from matplotlib import pyplot as plt

# Data for the plot



chemical_matter = np.array([
    [5.3e-14, 1.67e-27],  # Hydrogen atom
    [2.75e-10, 2.99e-26], # Water molecule
    [1e-7, 1e-18],        # Virus
    [2e-6, 6.5e-16],      # Bacteria
    [0.01, 0.001],        # Ladybug
    [0.3, 4],             # Cat
    [1.7, 70],            # Human
    [30, 1.9e5],          # Blue whale
    [6.4e6, 6e24],        # Earth
    [7e7, 1.9e27],        # Jupiter
])

stars = np.array([
    [7e8, 2e30],                    # Sun
    [2.726*7*10**8, 2.12*2*10**30], # Vega
    [1.713*7*10**8, 2.063*2*10**30],# Sirius
    [650*7*10**8, 16*2*10**30],     # Betelgeuse
    [680*7*10**8,13*2*10**30],      # Antares
    [7e6, 2.4e30],        # White dwarf
    [1e4, 7e30],          # Neutron star
    [1e3, 3e31],          # Black hole
    [1e21, 1e37],         # Milky Way
    [1e22, 6e42],         # Local Group
    [1e23, 2e48],         # Virgo Supercluster
    [1e24, 1e54]          # Observable Universe
])

galaxies_clusters = np.array([
    [1e21, 1e37],                  # Milky Way
    [1.52 * 9.46*10**20, 3*10**42],# Andromeda
    [1e22, 6e42],                  # Local Group
    [1e23, 2e48],                  # Virgo Supercluster
    [5*9.46*10**23,2*10**47],      # Laniakea Supercluster
    [1.2*9.46*10**23, 2*10**40],   # Shapley Supercluster
    [2*9.46*10**22, 6.2*10*10**45],# Coma supercluster
    [1e24, 1e54]                   # Observable Universe
])

# Linear fit for chemical matter
coeffs_chemical = np.polyfit(np.log10(chemical_matter[:, 0]), np.log10(chemical_matter[:, 1]), 1)

# Plotting
fig, ax = plt.subplots()
ax.set_xscale('log')
ax.set_yscale('log')
ax.scatter(chemical_matter[:, 0], chemical_matter[:, 1], label='Chemical matter', color='mediumvioletred')
ax.scatter(stars[:, 0], stars[:, 1], label='Stars', color='hotpink')
ax.scatter(galaxies_clusters[:, 0], galaxies_clusters[:, 1], label='Galaxies and clusters', color='firebrick')
ax.plot(chemical_matter[:, 0], 10**(coeffs_chemical[0]*np.log10(chemical_matter[:, 0]) + coeffs_chemical[1]), color='mediumvioletred', linestyle='--', label='Fit: Chemical matter')
ax.legend()
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlabel('Size (m)')
ax.set_ylabel('Mass (kg)')
ax.set_title('Scales of Nature')
fig.savefig('Kvant/Casestudy Scales of nature/scales_of_nature.png')