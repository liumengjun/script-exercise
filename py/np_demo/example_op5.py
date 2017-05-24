import numpy as np


a = np.arange(12)**2                       # the first 12 square numbers
i = np.array( [ 1,1,3,8,5 ] )              # an array of indices
print(a[i])                                       # the elements of a at the positions i
# array([ 1,  1,  9, 64, 25])
j = np.array( [ [ 3, 4], [ 9, 7 ] ] )      # a bidimensional array of indices
print(a[j])                                       # the same shape as j
# array([[ 9, 16],
#        [81, 49]])


palette = np.array( [ [0,0,0],                # black
                      [255,0,0],              # red
                      [0,255,0],              # green
                      [0,0,255],              # blue
                      [255,255,255] ] )       # white
image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
                    [ 0, 3, 4, 0 ]  ] )
palette[image]                            # the (2,4,3) color image
# array([[[  0,   0,   0],
#         [255,   0,   0],
#         [  0, 255,   0],
#         [  0,   0,   0]],
#        [[  0,   0,   0],
#         [  0,   0, 255],
#         [255, 255, 255],
#         [  0,   0,   0]]])

