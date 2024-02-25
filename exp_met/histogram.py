from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data5 = np.array([[0,1,2,0,1,0,1,0,0],[-8,-6,-4,-2,0,2,4,6,8]])
data10 = np.array([[0,1,2,2,3,1,1,0,0],[-8,-6,-4,-2,0,2,4,6,8]])
data = np.array([1,3,7,8,10,9,6,4,2])

hist = data
bin_centres = np.arange(-8,8,2) 

def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [1., 0., 1.]

coeff, var_matrix = curve_fit(gauss, bin_centres, hist, p0=p0)

# Get the fitted curve
hist_fit = gauss(bin_centres, *coeff)

plt.plot(bin_centres, hist, label='Test data')
plt.plot(bin_centres, hist_fit, label='Fitted data')