import numpy as np

a = np.floor(10*np.random.random((3,4)))
# array([[ 2.,  8.,  0.,  6.],
#        [ 4.,  5.,  1.,  1.],
#        [ 8.,  9.,  3.,  6.]])
a.shape
# (3, 4)

a.ravel() # flatten the array
# array([ 2.,  8.,  0.,  6.,  4.,  5.,  1.,  1.,  8.,  9.,  3.,  6.])
a.shape = (6, 2)
a.T       # the a.transpose
# array([[ 2.,  0.,  4.,  1.,  8.,  3.],
#        [ 8.,  6.,  5.,  1.,  9.,  6.]])

# note:
# The reshape function returns its argument with a modified shape, whereas the ndarray.resize method modifies the array itself:

a.resize((2,6))
a.reshape(3,-1)


a = np.floor(10*np.random.random((2,2)))
# array([[ 8.,  8.],
#        [ 0.,  0.]])
b = np.floor(10*np.random.random((2,2)))
# array([[ 1.,  8.],
#        [ 0.,  4.]])
np.vstack((a,b))
# array([[ 8.,  8.],
#        [ 0.,  0.],
#        [ 1.,  8.],
#        [ 0.,  4.]])
np.hstack((a,b))
# array([[ 8.,  8.,  1.,  8.],
#        [ 0.,  0.,  0.,  4.]])

## The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to vstack only for 1D arrays:
np.column_stack((a,b))   # With 2D arrays


a = np.array([4.,1.])
b = np.array([2.,8.])
a[:,newaxis]  # This allows to have a 2D columns vector
# array([[ 4.],
#        [ 1.]])
np.column_stack((a,b))
# array([[ 4.,  2.],
#        [ 1.,  8.]])
np.column_stack((a[:,newaxis],b[:,newaxis]))
# array([[ 4.,  2.],
#        [ 1.,  8.]])
np.vstack((a,b))
# array([[ 4.,  1.],
#        [ 2.,  8.]])
np.vstack((a[:,newaxis],b[:,newaxis])) # The behavior of vstack is different
# array([[ 4.],
#        [ 1.],
#        [ 2.],
#        [ 8.]])


