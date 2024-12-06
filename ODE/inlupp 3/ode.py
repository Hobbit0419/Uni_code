import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp as sip

def ak (k):
    a = 0.3
    if k == 0:
        return 1
    else:
        return -ak(k-1) * ((a - 2*k)*(a+2*k+1))/((2*k+1)*(2*k+2))
    

def series(x, K):
    result = 0
    for k in range(K):
        result += ak(k)*x**(2*k)
    return result

def ode(x, y):
    alpha = 0.3
    
    y1, y2 = y  # y[0] = y1, y[1] = y2
    dydx = [
        y2,  # y1' = y2
        (2 * x * y2 - alpha * (alpha + 1) * y1) / (1 - x**2)  # y2'
    ]
    return dydx

x0 = 0.5
x1 = 0.7

y0 = sip(ode, [-0.999999,0.999999], [1,0], 'RK45', [0.5]).y[0]
y1 = sip(ode, [-0.999999,0.999999], [1,0], 'RK45', [0.7]).y[0]

for i in range(100):
    print(series(0.5, i))