import numpy as np
from numpy import pi


a = np.arange(15).reshape(3, 5)
print(a)
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
print(a.shape)
# (3, 5)
print(a.ndim)
# 2
print(a.dtype.name)
# 'int64'
print(a.itemsize)
# 8
print(a.size)
# 15
print(type(a))
# <type 'numpy.ndarray'>
b = np.array([6, 7, 8])
print(b)
# array([6, 7, 8])
print(type(b))
# <type 'numpy.ndarray'>

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
# dtype('float64')

c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)
print(c.dtype)
# complex128

print(np.zeros( (3,4) ))

print(np.ones( (2,3,4), dtype=np.int16 ))

print(np.empty( (2,3) ))

# To create sequences of numbers,
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))
# use the function linspace that receives as an argument the number of elements
print(np.linspace( 0, 2, 9 ))
x = np.linspace( 0, 2*pi, 32 )
print(x)
f = np.sin(x)
print(f)

a = np.arange(6)
print(a)
b = np.arange(12).reshape(4,3)
print(b)
c = np.arange(24).reshape(2,3,4)
print(c)

# To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.
print(np.arange(10000))
# np.set_printoptions(threshold='nan')
print(np.arange(10000).reshape(100,100))

