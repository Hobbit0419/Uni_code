import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
import random

def phasor_diagram_rect(phasors, labels=[], colors=[]):
    
    if len(colors) == len(phasors) and len(labels) == len(phasors):
        polar = []
        for phasor in zip(phasors,labels,colors):
            polar.append((abs(phasor[0]), cm.phase(phasor[0]), phasor[1], phasor[2]))
            
        sorted_polar = sorted(polar, key=lambda x: x[0], reverse=True)
        
        fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))
        for phasor in sorted_polar:
            r = [0,phasor[0]]
            phi = [360 + phasor[1]]
            print(r,phi)
            ax.plot(r, phi, label=phasor[2], color=phasor[3])
        ax.legend()
        
    elif len(labels) == len(phasors):
        polar = []
        for phasor in zip(phasors,labels):
            polar.append((abs(phasor[0]), cm.phase(phasor[0]), phasor[1]))
            
        sorted_polar = sorted(polar, key=lambda x: x[0], reverse=True)
        
        fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))
        for phasor in sorted_polar:
            r = [0,phasor[0]]
            phi = [0, 360 + phasor[1]]
            print(r,phi)
            random_color = (random.random(), random.random(), random.random())
            ax.plot(r, phi, label=phasor[2], color=random_color)
        ax.legend()
        
    elif len(colors) == len(phasors):
        polar = []
        for phasor in zip(phasors,colors):
            polar.append((abs(phasor[0]), cm.phase(phasor[0]), phasor[1]))
            
        sorted_polar = sorted(polar, key=lambda x: x[0], reverse=True)
        
        fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))
        for phasor in sorted_polar:
            r = [0,phasor[0]]
            phi = [0, 360 + phasor[1]]
            print(r,phi)
            ax.plot(r, phi, color=phasor[2])
            
    else:
        polar = []
        for phasor in phasors:
            polar.append((abs(phasor), cm.phase(phasor)))
            
        sorted_polar = sorted(polar, key=lambda x: x[0], reverse=True)
        
        fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))
        for phasor in sorted_polar:
            r = [0,phasor[0]]
            phi = [0, 360 + phasor[1]]
            print(r,phi)
            random_color = (random.random(), random.random(), random.random())
            ax.plot(r, phi, color=random_color)



def main():
    T = complex(4, 6)
    S = complex(2, -1)
    phasors = [T, S]
    colors = ['green', 'red']
    labels = ['Test', 'test']
    print(abs(S), 2*np.pi + cm.phase(S))
    
    phasor_diagram_rect(phasors)
    
    plt.show()
    
if __name__ == '__main__':
    main()