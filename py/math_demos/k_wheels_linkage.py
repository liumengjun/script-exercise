from dataclasses import dataclass
import math
from turtle import Turtle, done


@dataclass
class Wheel:
    i: int = 0  # id
    r: float = 1.0  # radius
    s: float = 0.0  # speed


def paint_arrow(pen, x, y, arraw_rad=0.0, size=10):
    pen.setheading(0)
    pen.left(30+arraw_rad*180/math.pi)
    for _ in range(3):
        pen.left(120)
        pen.forward(size)


def paint_circle(pen, ox, oy, radius):
    # 画圆, 从圆的最低点开始画的
    pen.teleport(ox, oy-radius)
    pen.setheading(0)
    pen.circle(radius)


def _save_file(screen, k_wheels, one_unit, rounds=None):
    """保存为 postscript 文件"""
    k = len(k_wheels)
    filename = 'var/k_%d-[%s]-unit_%dpx%s.ps' % (
        k,
        ','.join(['r%.1f_s%.1f' % (w.r, w.s) for w in k_wheels]),
        one_unit,
        rounds and ('-rounds_%.2f' % rounds) or '',
    )
    print(filename)
    screen.save(filename, overwrite=True)


def _calc_max_rounds(k_wheels):
    """
    根据 w.s Wheel 的 speed 判断最大圈数
    w.s都是整数时为1, w.s不是整数时todo
    默认其精确到小数点后1位(再细分的不考虑), _save_file()中同样
    """
    max_rounds = 1
    has5 = False
    has2 = False
    for w in k_wheels:
        f = abs(w.s)  # type: float
        # print(f)
        if f.is_integer():
            continue
        ff = round((f-int(f))*10, 2)  # 使用`round()`防止`n.999999999999999`的情况`
        # print(ff)
        if ff.is_integer():
            if ff == 5:
                has5 = True
            elif int(ff) % 2 == 0:
                has2 = True
            else:
                max_rounds = max(10, max_rounds)
        else:
            max_rounds = 100  # 不再细分
            break
    if has5:
        max_rounds = max(2, max_rounds)
    if has2:
        max_rounds = max(5, max_rounds)
    if has5 and has2:
        max_rounds = max(10, max_rounds)
    print('max_rounds:', max_rounds)
    return max_rounds


def paint_k_wheels(k_wheels):
    colors = ['orange', 'green', 'blue', 'red',
              'gold', 'violet', 'cyan', 'brown']
    locus_color = 'fuchsia'
    one_unit = 30
    factor = 1/150
    max_rounds = _calc_max_rounds(k_wheels)
    iter_count = int(math.pi*2/factor*max_rounds)+2
    k = len(k_wheels)
    k_vecs = [(0, 0)]*k
    locus_begin = False
    is_paused = False
    rounds = 0

    # 两个 Turtle
    main_t = Turtle(visible=False)  # 画滚动的圆
    locus_t = Turtle(visible=False)  # 画轨迹
    # print(main_t.getscreen() == locus_t.getscreen())  # True
    screen = main_t.getscreen()
    screen.setup(1.0, 1.0)
    screen.tracer(0, 0)  # 加快动画速度, 关闭`tracing`, 手动`update`

    def __toggle_paused(*args):
        nonlocal is_paused
        is_paused = True  # not is_paused
        print('is_paused:', is_paused)

    def __save_file(*args):
        _save_file(screen, k_wheels, one_unit, rounds)

    screen.listen()
    screen.onkeypress(__toggle_paused, 'space')
    screen.onclick(__toggle_paused)
    screen.onkeyrelease(__save_file, 's')

    locus_t.dot(3)
    # 画第一个圆, 从圆的最低点开始画的
    locus_t.color(colors[0])
    paint_circle(locus_t, 0, 0, k_wheels[0].r*one_unit)
    for t in range(iter_count):
        if is_paused:
            print('is_paused:', is_paused)
            input("按回车继续...\n")  # 暂停绘制，在终端回车继续
            is_paused = False
            print('is_paused:', is_paused)
        t_factor = t*factor
        rounds = t_factor/math.pi/2
        if t_factor % (math.pi/4) <= 0.01:  # 粗略估计进度
            print('t: %d, t_factor: %.2f, rounds: %.2f' %
                  (t, t_factor, rounds))
        main_t.clear()
        for seq, w in enumerate(k_wheels):
            radius = w.r*one_unit
            rad = w.s*t_factor
            r_vec = k_vecs[seq] = (math.cos(rad)*radius, math.sin(rad)*radius)
            # print("r_vec[%d]: %s" % (seq, r_vec))
            # 计算圆心, 前面的几个圆半径向量相连即是当前圆的圆心
            o = [0, 0]
            for _i in range(seq):
                o[0] += k_vecs[_i][0]
                o[1] += k_vecs[_i][1]
            # print("origin[%d]: %s" % (seq, o))
            main_t.color(colors[seq % len(colors)])
            if seq > 0:
                paint_circle(main_t, o[0], o[1], radius)
            # 画半径向量
            r_vec_end = (o[0]+r_vec[0], o[1]+r_vec[1])
            main_t.teleport(o[0], o[1])
            main_t.goto(r_vec_end[0], r_vec_end[1])
            paint_arrow(main_t, r_vec_end[0], r_vec_end[1], rad)
            # 绘制轨迹, 最后一个圆, 其半径向量终点
            if seq == k-1:
                main_t.dot(6, 'purple')  # 模拟笔尖, 比 locus_color 颜色深
                if locus_begin:
                    locus_t.goto(r_vec_end[0], r_vec_end[1])
                else:
                    locus_t.teleport(r_vec_end[0], r_vec_end[1])
                    locus_t.color(locus_color)
                    locus_t.dot(4)
                    locus_t.width(4)
                    locus_begin = True
        screen.update()  # 手动update
    _save_file(screen, k_wheels, one_unit)
    done()


if __name__ == "__main__":
    k_wheels = [
        Wheel(r=2.3, s=1),
        Wheel(r=1, s=-2.5),
        # Wheel(r=3, s=3),
        # Wheel(r=3, s=-1),
        # Wheel(r=2, s=2),
        # Wheel(r=2, s=-1),
        # Wheel(r=1, s=-3),
        # Wheel(r=1, s=1),
    ]
    print(k_wheels)

    paint_k_wheels(k_wheels)
