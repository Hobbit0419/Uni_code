import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as ode

# Visat under F9
# Introduktion till beräkningsvetenskap
# Runge-Kutta 4 (RK4) på testekvationen
# u_t=a*u+g(t)
#
# Egenvärdet till ODE här benämnt a (lambda på F)
# Sätt b=0 för g(t)=0
# 
# Notera att RK4 är stabilt för rent imaginära egenvärden
# för stabilt val av tidssteg (vi kommer till detta under F10)
def f(t,y,a,b):
    return a*y + b*np.sin(np.pi*t)

T=100
tspan = (0,T)
a=1j
b=0
y0 = 1+0j


fig = plt.figure()
SOL = ode.solve_ivp(f, tspan, np.array([y0]), method='RK45',args=(a,b), rtol=1e-10, atol=1e-10)
plt.plot(SOL.t,SOL.y[0].real,label='$u(t)$')
plt.grid()
plt.xlabel('t')
plt.ylabel('u')
plt.title('Med RK45')
plt.legend()


N=200;
k = T/N
t = np.linspace(tspan[0],tspan[1],N+1)

u = np.zeros(N+1,dtype = complex)
#u = np.zeros(N+1,dtype=np.complex128)
u[0] = y0


# Löser med RK4
for n in range(N):
	w1=f(t[n],u[n],a,b)
	w2=f(t[n]+k/2,u[n]+k/2*w1,a,b)
	w3=f(t[n]+k/2,u[n]+k/2*w2,a,b)
	w4=f(t[n+1],u[n]+k*w3,a,b)
	u[n+1] = u[n] + k/6*(w1+2*w2+2*w3+w4)


fig = plt.figure()
plt.plot(t,u.real,label='$v(t)$')
plt.grid()
plt.xlabel('t')
plt.ylabel('v')
plt.title('Med RK4')
plt.legend()


plt.show()
