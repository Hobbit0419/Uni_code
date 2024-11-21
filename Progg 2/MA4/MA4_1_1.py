
"""
Solutions to module 4
Review date:
"""

student = "Anton Lindbro"
reviewer = ""

import math
import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    points = []
    inside = []
    outside = []
    N=n
    
    while N >= 0:
        points.append((r.uniform(-1,1), r.uniform(-1,1)))
        N-=1
        
    
    for point in points:
        if point[0]**2 + point[1]**2 <= 1:
            inside.append(point)
        else:
            outside.append(point)
    
    pi = 4*len(inside)/len(points)
    
    fig, ax =  plt.subplots()
    
    print(f'Using {n} points we approximate pi as {pi} and the true value is {math.pi}')
    
    ax.scatter(*zip(*inside), color='red')
    ax.scatter(*zip(*outside), color='blue')
    ax.set_aspect('equal')
    fig.savefig(f'{n}.png')
    
    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
