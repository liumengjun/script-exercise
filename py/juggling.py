#!/usr/bin/python
# a is list, b is list
# l is list of combined with a before b
# then turn l to make b before a
l = []
a1 = 1
a2 = 6
b1 = 3  # a1 < b1 < a2
b2 = 10 # b2 > a2

aLen = a2 - a1
bLen = b2 - b1
lLen = aLen + bLen

for i in range(a1,a2):
    l.append(i)
for i in range(b1,b2):
    l.append(i)


def show(l=l, aLen=aLen):
    print('[', end='')
    for i in range(0, aLen):
        print(str(l[i])+',', end='')
    print('  ', end='')
    for i in range(aLen, len(l)):
        print(str(l[i])+',', end='')
    print(']')


show()

# 旋转a
for i in range(0, aLen//2):
    t = l[i]
    l[i] = l[aLen - 1 - i]
    l[aLen - 1 - i] = t

# 旋转b
for i in range(0, bLen//2):
    t = l[aLen + i]
    l[aLen + i] = l[lLen - 1 - i]
    l[lLen - 1 - i] = t

# 旋转l
for i in range(0, lLen//2):
    t = l[i]
    l[i] = l[lLen - 1 - i]
    l[lLen - 1 - i] = t

show(l, bLen)

