import turtle
from turtle import *  #从turtle中导出所有模块
radius = 100     #半径为100
color("black", "black")  #画线颜色黑色，填充颜色黑色
begin_fill()  #开始填充
circle(radius/2, 180)  #逆时针画圈，半径为50,180°
circle(radius, 180)  #逆时针画圈，半径为100,180°
left(180)  #转向180°
circle(-radius/2, 180)  #顺时针画圈，半径50,180°
end_fill()  #填充结束
#移动到画太极图黑色的小圈位置，开始画小白圈
left(90)#左转向90°，海龟头垂直水平线向上
penup()#提笔，不留痕迹
forward(radius*0.35)#向前，半径的0.35=35像素
right(90)#右转向90°，海龟头与右侧水平线同向
pendown()#落笔，开始画线
#开始画太极图黑色部分的小白圈
color("white", "white")#画线颜色为白色，填充颜色为白色
begin_fill()#开始填充
circle(radius*0.15)#逆时针画圈，半径的0.15=15像素（35+15+15+35=100）
end_fill() #填充结束

left(90)#左转向90°
penup()#提笔，不留痕迹
backward(radius*0.7)#后退往下走，为半径的0.7=70，此时海龟头朝上与水平垂直
pendown()#落笔，开始留下痕迹
left(90)#左转90°，此时海龟头与左侧水平同向
#开始画太极图白色部分里的小黑圈
color("black", "black")#画线颜色为黑色，填充为黑色
begin_fill()#开始填充
circle(radius*0.15)#开始逆时针画圈，半径的0.15=15个像素
end_fill() #填充完毕

right(90)#再右转90°，此时海龟头垂直水平线向上
penup()#提笔，不留痕迹
backward(radius*0.65)#后退为半径的0.65=65个像素，往下到达太极图黑色半圈的底点处
right(90)#右转90°，海龟头与右侧水平线同向
pendown()#落笔，开始留下痕迹
circle(radius, 180)#逆时针画圈，半径100,180°，画太极图的白色部分的大圈
hideturtle()#隐藏笔头hideturtle
turtle.done()