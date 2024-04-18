import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import scipy.integrate as ode

# Lösning under F5, block 3
# y_tt=gamma*y, y(0)=1, y_t(0)=0
# Lös med RK4
# Introduktion till beräkningsvetenskap
#
# Man kan visa att största möjliga (stabila) tidssteg ges av k=2.8/sqrt(-gamma)
# 
# egenvärdena till ODE gea av lambda_1=sqrt(gamma), lambda_2=-sqrt(gamma), 
# dvs 10i och -10i. Stabilitets området RK4 går till 2.8i (och -2.8i) på
# imaginära axeln. 
#
# Om metod=2 så används istället RK2 (Heun) som är instabil i detta fall 

def F5(t,u,gamma):
		y  = u[0]
		vy = u[1]
		return np.array([vy,gamma*y])

metod=4 # 2 betyder RK2, 4 betyder RK4		

gamma=-100
f = np.array([1,0])

T=10
tspan = (0,T)


fig = plt.figure()
SOL = ode.solve_ivp(F5, tspan, f, method='RK45',args=(gamma,), rtol=1e-10, atol=1e-10)
#plt.plot(SOL.t,SOL.y[1].real,label='$u(t)$')
plt.plot(SOL.t,SOL.y[1].real,label='$y(t)$')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Harmonisk oscillator med RK45')
plt.legend()



#N=200;
k = 0.1
N = int(ceil(T/k)) # number of intervals
t = np.linspace(0,T,N+1)

#u = np.zeros((N+1,2),dtype = complex)
u = np.zeros((N+1,2),dtype = float)
u[0,:] = f

if metod==4:
# Löser med RK4
#
	for n in range(N):
		w1=F5(t[n],u[n,:],gamma)
		w2=F5(t[n]+k/2,u[n,:]+k/2*w1,gamma)
		w3=F5(t[n]+k/2,u[n,:]+k/2*w2,gamma)
		w4=F5(t[n+1],u[n,:]+k*w3,gamma)
		u[n+1,:] = u[n,:] + k/6*(w1+2*w2+2*w3+w4)

	fig = plt.figure()
	#plt.plot(t,u[:,1],label='$v(t)$')
	plt.plot(t[:],u[:,0],label='$y^n$')
	plt.grid()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Harmonisk oscillator med RK4')
	plt.legend()

else:

# Löser med RK2
#
	for n in range(N):
		w1=F5(t[n],u[n,:],gamma)
		w2=F5(t[n+1],u[n,:]+k*w1,gamma)
		u[n+1,:] = u[n,:] + k/2*(w1+w2)


	fig = plt.figure()
	#plt.plot(t,u[:,1],label='$v(t)$')
	plt.plot(t[:],u[:,0],label='$y^n$')
	plt.grid()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Harmonisk oscillator med RK2')
	plt.legend()



plt.show()
