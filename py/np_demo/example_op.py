import numpy as np
from numpy import pi

a = np.array( [20,30,40,50] )
print(a)
b = np.arange( 4 )
print(b)
# array([0, 1, 2, 3])
c = a-b
print(c)
# array([20, 29, 38, 47])
print(b**2)
# array([0, 1, 4, 9])
print(10*np.sin(a))
# array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
print(a<35)
# array([ True, True, False, False], dtype=bool)



A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
               [3,4]] )
print(A)
print(B)
# elementwise product
print(A*B)
# array([[2, 0],
#        [0, 4]])
# matrix product
print(A.dot(B))
# array([[5, 4],
#        [3, 4]])
# another matrix product
print(np.dot(A, B))
# array([[5, 4],
#        [3, 4]])



# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

a = np.ones((2,3), dtype=int)
print(a)
b = np.random.random((2,3))
print(b)
a *= 3
print(a)
# array([[3, 3, 3],
#        [3, 3, 3]])
b += a
print(b)
# array([[ 3.417022  ,  3.72032449,  3.00011437],
#        [ 3.30233257,  3.14675589,  3.09233859]])
# a += b                  # b is not automatically converted to integer type
# Traceback (most recent call last):
#   ...
# TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'



a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
# 'float64'
c = a+b
print(c)
# array([ 1.        ,  2.57079633,  4.14159265])
print(c.dtype.name)
# 'float64'
d = np.exp(c*1j)
print(d)
# array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
#        -0.54030231-0.84147098j])
print(d.dtype.name)
# 'complex128'



a = np.random.random((2,3))
print(a)
print(a.sum())
print(a.min())
print(a.max())



b = np.arange(12).reshape(3,4)
print(b)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
print(b.sum(axis=0))                            # sum of each column
# array([12, 15, 18, 21])
print(b.min(axis=1))                            # min of each row
# array([0, 4, 8])
print(b.cumsum(axis=1))                         # cumulative sum along each row
# array([[ 0,  1,  3,  6],
#        [ 4,  9, 15, 22],
#        [ 8, 17, 27, 38]])
