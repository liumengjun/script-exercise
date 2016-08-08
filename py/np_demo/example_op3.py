import numpy as np

a = np.arange(10)**3
# array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
a[2]
# 8
a[2:5]
# array([ 8, 27, 64])
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
# array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
a[ : :-1]                                 # reversed a
# array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
for i in a:
    print(i**(1/3.))
# nan
# 1.0
# nan
# 3.0
# nan
# 5.0
# 6.0
# 7.0
# 8.0
# 9.0


def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
# array([[ 0,  1,  2,  3],
#        [10, 11, 12, 13],
#        [20, 21, 22, 23],
#        [30, 31, 32, 33],
#        [40, 41, 42, 43]])
b[2,3]
# 23
b[0:5, 1]                       # each row in the second column of b
# array([ 1, 11, 21, 31, 41])
b[ : ,1]                        # equivalent to the previous example
# array([ 1, 11, 21, 31, 41])
b[1:3, : ]                      # each column in the second and third row of b
# array([[10, 11, 12, 13],
#        [20, 21, 22, 23]])

b[-1]                                  # the last row. Equivalent to b[-1,:]
# array([40, 41, 42, 43])


# The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is a rank 5 array (i.e., it has 5 axes), then
#
#     x[1,2,...] is equivalent to x[1,2,:,:,:],
#
#     x[...,3] to x[:,:,:,:,3] and
#
#     x[4,...,5,:] to x[4,:,:,5,:].

for row in b:
    print(row)

# the flat attribute which is an iterator over all the elements of the array:

for element in b.flat:
    print(element)

