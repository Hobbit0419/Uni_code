import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

enkelspalt1 = pd.read_csv('Vågop/rapport/figures/data/vågoptik1.csv', delimiter=';').astype(float)
enkelspalt2 = pd.read_csv('Vågop/rapport/figures/data/vågoptik2.csv', delimiter=';').astype(float)
dubbelspalt1 = pd.read_csv('Vågop/rapport/figures/data/vågoptik3.csv', delimiter=';').astype(float)
kvadruppelspalt1 = pd.read_csv('Vågop/rapport/figures/data/vågoptik4.csv', delimiter=';').astype(float)

def enkelspalt(bred, lambda1):
    theta = np.linspace(-0.1,0.1, 500)
    beta = ((2*np.pi)/lambda1) * bred * np.sin(theta)
    I = (np.sin(beta/2)/(beta/2))**2
    
    return theta, I

enkelspalt1.sort_values('Light')
enkelspalt2.sort_values('Light')
dubbelspalt1.sort_values('Light')
kvadruppelspalt1.sort_values('Light')

enkelspaltt = enkelspalt(4*10**-5, 532*10**-9)

fig1, axs1 = plt.subplots()
axs1.plot(enkelspaltt[0], enkelspaltt[1], linestyle='dashdot', marker='.')
axs1.set_xlabel('Position [m]')
axs1.set_ylabel('Ljusintensitet [arbiträr enhet]')
axs1.set_title('Teoretisk diffraktion av enkelspalt')
fig1.savefig('Vågop/rapport/figures/enkelspaltt')

fig2, axs2 = plt.subplots()
axs2.plot(enkelspalt1['Position'], enkelspalt1['Light'],linestyle='dashdot', marker='.')
axs2.set_xlabel('Position [m]')
axs2.set_ylabel('Ljusintensitet [arbiträr enhet]')
axs2.set_title('Diffraktion av enkelspalt')
axs2.set_xlim(0.05, 0.15)
fig2.set_figwidth(10)
fig2.savefig('Vågop/rapport/figures/enkelspalt')

fig3, axs3 = plt.subplots()
axs3.plot(dubbelspalt1['Position'], dubbelspalt1['Light'], linestyle='dashdot', marker='.')
axs3.set_xlabel('Position [m]')
axs3.set_ylabel('Ljusintensitet [arbiträr enhet]')
axs3.set_title('Diffraktion och interferens av dubbelspalt')
axs3.set_xlim(0.03, 0.09)
fig3.set_figwidth(15)
fig3.savefig('Vågop/rapport/figures/dubbelspalt')

fig4, axs4 = plt.subplots()
axs4.plot(kvadruppelspalt1['Position'], kvadruppelspalt1['Light'], linestyle='dashdot', marker='.')
axs4.set_xlabel('Position [m]')
axs4.set_ylabel('Ljusintensitet [arbiträr enhet]')
axs4.set_title('Diffraktion och interferens hos kvadruppelspalt')
axs4.set_xlim(0.04, 0.14)
fig4.set_figwidth(8)
fig4.savefig('Vågop/rapport/figures/kvadruppelspalt')