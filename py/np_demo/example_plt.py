
def x(t):
    return a*(2*np.cos(t)-cos(2*t));

def y(t):
    return a*(2*sin(t)-sin(2*t))


xs = np.fromfunction(x,(100,),dtype=float)
ys = np.fromfunction(y,(100,),dtype=float)

plot(xs,ys,'r.')
