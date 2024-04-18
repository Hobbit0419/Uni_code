import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as ode

# Problem 6+7+8
def f(t,y,N,b,d,beta,u,v):
    S = y[0]
    I = y[1]
    R = y[2]
    return np.array([b*N - d*S - beta*I/N*S - v*S, beta*I/N*S - u*I - d*I, u*I - d*R + v*S])

tspan = (0,60)
N = 1000
beta = 0.3
u = 1/7
v = 0
b = 0.002/365
d = 0.0016/365

I0 = 5
S0 = N - I0
R0 = 0
y0 = np.array([S0,I0,R0])

SOL = ode.solve_ivp(f, tspan, y0, method='RK45', args=(N,b,d,beta,u,v), max_step=1)

plt.plot(SOL.t,SOL.y[0,:],label='$S(t)$')
plt.plot(SOL.t,SOL.y[1,:],label='$I(t)$')
plt.plot(SOL.t,SOL.y[2,:],label='$R(t)$')
plt.grid()
plt.xlabel('Time [days]')
plt.ylabel('Number of people')
plt.legend()
plt.show()