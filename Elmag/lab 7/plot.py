import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def exp_up(k,x):
    return 1-np.exp(-k*x)

def exp_down(k,x):
    return np.exp(-k*x)

#Uppgift 1
U = np.array([498*10**-3, 499*10**-3, 491*10**-3, 493*10**-3, 488*10**-3, 491*10**-3, 490*10**-3, 480*10**-3, 475*10**-3, 465*10**-3, 485*10**-3])
UR = np.array([143*10**-4, 297*10**-4, 604*10**-4, 147*10**-3, 257*10**-3, 375*10**-3, 468*10**-3, 451*10**-3, 451*10**-3, 442*10**-3, 481*10**-3])
y = UR/U
T = np.array([20*10**-3, 996*10**-5, 5*10**-3, 198*10**-5, 980*10**-6, 496*10**-6, 200*10**-6, 100*10**-6, 80*10**-6, 572*10**-7, 50*10**-6])
x = 1/T

initial_guess = [0.001]  # Initial guess for k
params, covariance = curve_fit(exp_up, x, y, p0=initial_guess)

k = params[0]
print(f"Fitted parameter k = {k}")

xline = np.linspace(0, 20000, 10000)
yline = exp_up(k,xline)

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.plot(xline,yline)
ax.set_title('Förhållande mellan in och ut spänning som funktion av frekvens')
ax.set_ylabel('Spänning [V]')
ax.set_xlabel('Frekvens [Hz]')
plt.savefig('Elmag/lab 7/plt1.png')


#Uppgift 2
Uin = np.array([489*10**-3, 488*10**-3, 488*10**-3, 486*10**-3, 480*10**-3, 468*10**-3, 451*10**-3, 443*10**-3, 442*10**-3, 439*10**-3, 438*10**-3])
Uut = np.array([489*10**-3, 488*10**-3, 485*10**-3, 464*10**-3, 408*10**-3, 294*10**-3, 141*10**-3, 71*10**-3, 56*10**-3, 37*10**-3, 31*10**-3])
F = np.abs(Uut/Uin)
FdB = 20 * np.log(F)

initial_guess = [0.001]  # Initial guess for k
params, covariance = curve_fit(exp_down, x, F, p0=initial_guess)

k = params[0]
print(f"Fitted parameter k = {k}")

xline = np.linspace(0, 20000, 10000)
yline1 = exp_down(k,xline)

flim = np.log(np.sqrt(2))/k

print(f'Gränsfrekvensen är {flim.round(0)}[Hz]')

fig, ax = plt.subplots()
ax.scatter(x,y, color = 'b', label='Förstärkning högpass')
ax.plot(xline,yline)
ax.scatter(x, F, color = 'r', label='Förstärkning lågpass')
ax.plot(xline,yline1, color='r')
ax.set_title('Förstärkning för högpass och lågpass filter')
ax.set_ylabel('Spänning [V]')
ax.set_xlabel('Frekvens [Hz]')
ax.vlines(flim,0,1, label='Gräns frekvens')
ax.legend()
plt.savefig('Elmag/lab 7/plt2.png')

fig, ax = plt.subplots()
ax.scatter(x, F, color = 'r', label='Förstärkning lågpass')
ax.plot(xline,yline1, color='r')
ax.set_title('Förstärkning för högpass och lågpass filter')
ax.set_ylabel('Spänning [V]')
ax.set_xlabel('Frekvens [Hz]')
ax.set_yscale('log')
ax.legend()
plt.savefig('Elmag/lab 7/plt3.png')

fig, ax = plt.subplots()
ax.quiver(218,5, 421,6)