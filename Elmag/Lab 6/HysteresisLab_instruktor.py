import numpy as np
import matplotlib.pyplot as plt
import hysteresis as hys

N1 = 1000         #Varv primärspole
N2 = 420          #Varv sekundärspole
R1 = 1.8          #[Ohm]
RC = 0.0026        #[s] - Varierar från integrator till integrator ändra till erat värde!
langd_prov= 0.21  #[Meter]
bredd_prov= 0.03  #[Meter]
magnetisk_langd_prov= 0.15  #[Meter] Den del av provet som är i fält

prov=['l','t','c','d','m','mj','cu']

densitet = np.array([7.6*10**(3), 7.6*10**(3), 7.9*10**(3), 7.9*10**(3), 8.8*10**(3), 7.5*10**(3), 8.9*10**(3)])      #[kg/m^3] Ändra för varje prov!
hojd_prov = np.array([0.62*10**(-3), 0.5*10**(-3), 0.64*10**(-3), 0.65*10**(-3), 1*10**(-3), 0.34*10**(-3), 0.65*10**(-3)])       #[Meter] Ändra för varje prov!
Area_prov = bredd_prov*hojd_prov #[Meter^2]

H_shift = [0,0,0,0,0,0,0]          #Ändra för varje prov!
sampel_pkt=25000     #[Sa] avläses från Oscilloskopet

#Importera data
path = 'Elmag/Lab 6/'


for n in range(len(prov)):
    matData = np.loadtxt(path + prov[n] + '.csv', dtype=str, delimiter=',', skiprows = 2)

    spanning_1 = matData[:,1]
    spanning_2 = matData[:,2]
    U1 = spanning_1.astype(float)
    U2 = spanning_2.astype(float)

    #Skala om till rätt värden
    H = -N1*U1/(magnetisk_langd_prov*R1)
    B = RC*U2/(N2*Area_prov[n])
    HB = np.column_stack((H,B))
    
    #Centrerar kurvorna
    H = H-(max(H) + min(H))/2 + H_shift[n]
    B = B-(max(B) + min(B))/2
    
    #Hitta axel skärningarna
    H_index = np.abs(H - 0).argmin()
    B_index = np.abs(B - 0).argmin()

    #Beräkna alla efterfrågade värden
    Bm = max(B)
    Br = abs(B[H_index])
    Hc = abs(H[B_index])
    
    reversal_points = [np.where(B == max(B)), np.where(B == min(B))]
    
    text = f'Bm = {Bm.round(3)} \n Br = {Br.round(3)} \n Hc = {Hc.round(3)}'
    
    #Ritar upp kurvorna
    fig, ax = plt.subplots()
    ax.scatter(H, B)
    ax.set_title(prov[n])
    ax.set_xlabel('H (A/m)', fontsize = 15)
    ax.set_ylabel('B (T)', fontsize = 15)
    ax.grid()
    ax.text(0.95, 0.05, text,
        transform=ax.transAxes,  # Use axis-relative coordinates
        fontsize=12,            # Adjust font size
        verticalalignment='bottom',
        horizontalalignment='right')
    plt.savefig('Elmag/Lab 6/' + prov[n])