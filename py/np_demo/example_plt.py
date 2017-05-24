import numpy as np
import matplotlib.pyplot as plt

a = 1
def x(t):
    return a*(2*np.cos(t)-np.cos(2*t));

def y(t):
    return a*(2*np.sin(t)-np.sin(2*t))


xs = np.fromfunction(x,(300,),dtype=float)
ys = np.fromfunction(y,(300,),dtype=float)

plt.plot(xs,ys,'r.')
plt.show()
