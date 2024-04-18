#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:07:42 2024

@author: Ken Mattsson
"""

import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import scipy.integrate as ode

# Introduktion till beräkningsvetenskap
# Projektövning: Ickelinjär Oscillator, block 2
#
# y'' = -y**3 -y**2*y', y(0)=1, y'(0)=0
# Lös med RK3 och testa felet genom att använda
# solve_ivp som referenslösning. Detta är lösningen 
# till deluppgift 4. Här finns ingen analtyisk lösning

def F(t,u):
		y  = u[0]
		v  = u[1]
		return np.array([v,-y**3-y**2*v])
  
f = np.array([1,0]) # Begynnelsedata  

T=20
tspan = (0,T)

fig = plt.figure()
SOL = ode.solve_ivp(F, tspan, f, method='RK45', rtol=1e-10, atol=1e-10)
plt.plot(SOL.t,SOL.y[0].real,label='$y(t)$')
plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.title('Ickelinjär oscillator med RK45')
plt.legend()

k = 0.02 # Tidssteget. Med 0.02 och T=20 blir detta N=1000
N = int(ceil(T/k)) # Antalet intervall (OBS: se till så T/k blir ett heltal! )
t = np.linspace(0,T,N+1)
u = np.zeros((N+1,2),dtype = float)
u[0,:] = f

# Löser med RK3
for n in range(N):
	 w1=F(t[n],u[n,:])
	 w2=F(t[n]+k/2,u[n,:]+k/2*w1)
	 w3=F(t[n]+k,u[n,:]-k*w1+2*k*w2)
	 u[n+1,:] = u[n,:] + k/6*(w1+4*w2+w3)
     
fig = plt.figure()
plt.plot(t[:],u[:,0],label='$y^{(n)}$')
plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.title('Ickelinjär oscillator med RK3')
plt.legend()

felet=np.abs(SOL.y[0,-1]-u[N,0])

print("Felet blir {}.".format(felet))

plt.show()
