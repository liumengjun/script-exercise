import numpy as np

B = np.arange(3)
# array([0, 1, 2])
np.exp(B)
# array([ 1.        ,  2.71828183,  7.3890561 ])
np.sqrt(B)
# array([ 0.        ,  1.        ,  1.41421356])
C = np.array([2., -1., 4.])
np.add(B, C)
# array([ 2.,  0.,  6.])



# See also
# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount,
# ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor,
# inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero,
# outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where

