import numpy as np
import cmath as cm
import matplotlib.pyplot as plt

w = 2*np.pi*1000
E1 = 5*cm.exp(1j*0)
E2 = 3*cm.exp(1j*cm.pi/2)
E3 = 1*cm.exp(1j*cm.pi)
R1 = 50
R2 = 150
R3 = 100
R4 = 50
L1 = 1*10**-3
L2 = 2*10**-3
C1 = 10*10**-6
C2 = 100*10**-6
C3 = np.linspace(1*10**-6,100*10**-6,10000)
ZC1 = 1/(1j*w*C1)
ZC2 = 1/(1j*w*C2)
ZC3 = 1/(1j*w*C3)
ZL1 = 1j*w*L1
ZL2 = 1j*w*L2


Z = np.array([[R1+ZC1,ZC1,0,0],[ZC1,R4+R2+ZL1+ZC1,R2,0],[0,R2,R3+ZC3+ZC2+R2,ZC3],[0,0,ZC3, ZL2+ZC3]])
V = np.array([E1,E3,E3,E2])
I = np.linalg.solve(Z,V)

U5 = I[3]*ZC3+I[2]*ZC3
U5p = cm.polar(U5)
print(U5p[0],np.rad2deg(U5p[1]))

U3 = -I[2]*ZC2
U3p = cm.polar(U3)
print(U3p[0],np.rad2deg(U3p[1]))

U2 = U5+I[2]*R3
U2p = cm.polar(U2)
print(U2p[0],np.rad2deg(U2p[1]))

U1 = U2-I[1]*R4
U1p = cm.polar(U1)
print(U1p[0],np.rad2deg(U1p[1]))

U4 = U1-I[0]*ZC1-I[1]*ZC1
U4p = cm.polar(U4)
print(U4p[0],np.rad2deg(U4p[1]))

P = R2 * (I[1]+I[2])**2
plt.plot(C3,P)
plt.show()