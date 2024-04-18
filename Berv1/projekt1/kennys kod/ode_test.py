import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as ode

# Visat under F9
# Introduktion till beräkningsvetenskap
# Euler framåt (RK1) på testekvationen
# u_t=a*u+g(t)
#
# Egenvärdet till ODE här benämnt a (lambda på F)
# Sätt b=0 för g(t)=0
# 
# Notera att RK1 är instabilt för rent imaginära egenvärden

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


N=200
k = T/N
t = np.linspace(tspan[0],tspan[1],N+1)

tn=np.linalg.norm(t)
print("Final time t = {:f} reached.".format(tn))

u = np.zeros(N+1,dtype = complex)
#u = np.zeros(N+1,dtype=np.complex128)
u[0] = y0


# Löser med Euler framåt (RK1)
for n in range(N):
	u[n+1] = u[n] + k*f(t[n],u[n],a,b)


fig = plt.figure()
plt.plot(t,u.real,label='$v(t)$')
plt.grid()
plt.xlabel('t')
plt.ylabel('v')
plt.title('Med RK1')
plt.legend()


plt.show()
