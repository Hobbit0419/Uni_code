import matplotlib.pyplot as plt
import math
import numpy as np

size = np.array([math.log10(0.43*10**-18), math.log10(2.8*10**-15), math.log10(0.84*10**-15), math.log10(0.073*10**-9), math.log10(50*10**-6), math.log10(5*10**-3), math.log10(46*10**-2), math.log10(11.5), math.log10(6.3*10**3), math.log10(1737.5*10**3), math.log10(6378*10**3), math.log10(617*10**9), math.log10(3*10**13), math.log10(10**21)])
mass = np.array([math.log10(3.845*10**-30), math.log10(9.11*10**-31), math.log10(1.67*10**-27), math.log10(2.657*10**-26), math.log10(2*10**-13), math.log10(0.75*10**-3), math.log10(4.5), math.log10(15*10**3), math.log10(1.5*10**15), math.log10(7.35*10**22), math.log10(6*10**24), math.log10(3.28*10**31), math.log10(2*10**37), math.log10(6*10**42)])

a, b = np.polyfit(size, mass, 1)

plt.scatter(size,mass, color='hotpink')
plt.plot(size, a*size+b,color='mediumvioletred')
plt.title('Scales of Nature')
plt.xlabel("Size (log10(m))")
plt.ylabel("Mass (log10(kg))")
plt.axhline(color='green', linestyle='--')
plt.axvline(color='green', linestyle='--')
plt.show()
