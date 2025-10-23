from turtle import *
from math import *
color("red")
def draw(a,end):
    t=0
    while t<(14*end):
        x=a*sin(t*3.14)*cos(t)
        y=a*sin(t*3.14)*sin(t)
        goto(x,y)
        t=t+0.03

draw(100,3.14)
done()