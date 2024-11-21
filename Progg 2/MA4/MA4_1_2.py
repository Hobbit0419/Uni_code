
"""
Solutions to module 4
Review date:
"""

student = "Anton Lindbro"
reviewer = ""

import math as m
import random as r
import functools as f

def sphere_volume(n, d, rad=1):
    points = [[r.uniform(-rad,rad) for i in range(d)] for j in range(n)]
    inside = len(list(filter(lambda x: x < rad, map(lambda t: m.sqrt(float(sum(x**2 for x in t))), points))))
    
    V = ((2*rad)**d) * (inside/n)
    return V
    
def hypersphere_exact(n,d, rad=1):
    v = ((m.pi**(d/2))/(m.gamma((d/2)+1)))*rad**d
    return v
    
def main():
    n = [100000, 100000]
    d = [2, 11]
    
    for sphere in zip(n,d):
        print(f'We approximate the {sphere[1]} dimensional sphere volume using {sphere[0]} points as {sphere_volume(*sphere)} and the actura value is {hypersphere_exact(*sphere)}')


if __name__ == '__main__':
	main()
