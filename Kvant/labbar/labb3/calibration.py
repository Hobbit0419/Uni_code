import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

def linear(x, a, b):
    return a * x + b

peaks = [209, 519]
energy = [6403, 17479]

popt, pcov = curve_fit(linear, peaks, energy, p0=[1, 0])

print(f"Fitted parameters: a = {popt[0]}, b = {popt[1]}")