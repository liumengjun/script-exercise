import turtle, time
# 初始不更新画面
turtle.tracer(0)

# 地板墙
wall = turtle.Pen()
wall.pencolor('red')
wall.pensize(10)
wall.hideturtle()
wall.penup()
wall.goto(-300, -200)
wall.pendown()
wall.forward(600)

# 小球
R = 15
ball = turtle.Turtle('circle')
ball.shapesize(R / 10)
ball.penup()
pos_x, pos_y = [100, 100]
pos_x, pos_y = ball.pos()
ball.goto(pos_x, pos_y)
wall_x, wall_y = wall.pos()

# 球参数
FPS = 60  # 每秒60帧
G = 9.80665  # 模拟重力加速度
DRAG = 0.1956 # 阻力
v_y = 1 # 初始速度

while True:

    # 清除印章
    ball.clearstamps()

    v_y += G  # 模拟重力加速度
    if pos_y - R - 10 < wall_y:  # 撞地面
        v_y *= -1

    pos_x, pos_y = pos_x, pos_y - v_y
    ball.goto(pos_x, pos_y)
    v_y = v_y * DRAG

    # 通过印章显示球
    ball.stamp()

    # 更新画面信息
    turtle.update()
    time.sleep(1 / FPS)