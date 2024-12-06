import numpy as np

def f(x):
    if x%2 == 0:
        return x/2
    elif x%3 == 0:
        return x/3
    else:
        return x + 10
    
def g(x):
    return f(f(f(x)))
    
X = np.arange(0,1000)

image = []

for x in X:
    image.append(g(x))


image = np.array(image)

print(len(set(image)))