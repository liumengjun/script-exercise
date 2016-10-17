#!/usr/bin/python
import random
i=1.0
c=0
ops = ['+','-','*','/']
while True:
    op = random.choice(ops)
    # print(op)
    if op == '+':
        i+=i
    elif op == '-':
        i-=1.0
    elif op == '*':
        i*=i
    elif op == '/':
        i/=2.0
    else:
        i+=1.0
    # print(i)
    c+=1
    if str(i) == 'inf':
        print(c)
        i=1.0
        c=0

