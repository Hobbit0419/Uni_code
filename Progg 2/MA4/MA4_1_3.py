
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import concurrent.futures as future
from time import perf_counter as pc

def sphere_volume(n, d, rad=1):
    points = [[r.uniform(-rad,rad) for i in range(d)] for j in range(n)]
    inside = len(list(filter(lambda x: x < rad, map(lambda t: m.sqrt(float(sum(x**2 for x in t))), points))))
    
    V = ((2*rad)**d) * (inside/n)
    return V

def hypersphere_exact(n,d, rad=1):
    v = ((m.pi**(d/2))/(m.gamma((d/2)+1)))*rad**d
    return v

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    processes = []
    results = []
    with future.ProcessPoolExecutor() as ex:
        for k in range(np):
            p = ex.submit(sphere_volume, n, d)
            processes.append(p)
        
        for k in range(np):
            results.append(processes[k].result())
    return float(sum(results)/len(results))


def find_inside(n,d, rad=1):
        points = [[r.uniform(-rad,rad) for i in range(d)] for j in range(n)]
        inside = len(list(filter(lambda x: x < rad, map(lambda t: m.sqrt(float(sum(x**2 for x in t))), points))))
        return inside

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np, rad=1):
    processes = []
    results = []
    
    if n % np == 0:
        with future.ProcessPoolExecutor() as ex:
            for k in range(np):
                p = ex.submit(find_inside, n//np, d)
                processes.append(p)
                
            for k in range(np):
                results.append(processes[k].result())
    else:
        with future.ProcessPoolExecutor() as ex:
            for k in range(np-1):
                p = ex.submit(find_inside, n//np, d)
                processes.append(p)
            
            p = ex.submit(find_inside, n//np + n%np, d)
            processes.append(p)
            
            for k in range(np):
                results.append(processes[k].result())
    V = ((2*rad)**d) * (sum(results)/n)
    return V

def main():
    n = 10000
    d = 11
    for y in range (10):
        sphere_volume(n,d)
    
    print(sphere_volume_parallel2(10000, 11, 10))


if __name__ == '__main__':
	main()
