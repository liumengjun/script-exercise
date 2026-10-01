from dataclasses import dataclass
import math
from turtle import Turtle, done


@dataclass
class Wheel:
    i: int = 0  # id
    r: int = 1  # radius
    s: int = 0  # speed


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


def _save_file(main_t, k_wheels):
    """保存为 postscript 文件"""
    k = len(k_wheels)
    filename = 'var/k_%d-[%s].ps' % (k, ','.join(['r%d_s%d' %
                                                  (w.r, w.s) for w in k_wheels]))
    print(filename)
    main_t.getscreen().save(filename, overwrite=True)


def paint_k_wheels(k_wheels):
    colors = ['orange', 'green', 'blue', 'red',
              'yellow', 'violet', 'cyan', 'brown']
    locus_color = 'fuchsia'
    one_unit = 50
    factor = 1/30
    iter_count = int(math.pi*2/factor)+2
    k = len(k_wheels)
    k_vecs = [(0, 0)]*k
    locus_begin = False

    # 两个 Turtle
    main_t = Turtle(visible=False)  # 画滚动的圆
    locus_t = Turtle(visible=False)  # 画轨迹
    main_t.speed(0)
    locus_t.speed(0)
    # print(main_t.getscreen() == locus_t.getscreen())  # True
    main_t.getscreen().tracer(1, 0)  # 加快动画速度

    locus_t.dot(3)
    # 画第一个圆, 从圆的最低点开始画的
    locus_t.color(colors[0])
    paint_circle(locus_t, 0, 0, k_wheels[0].r*one_unit)
    for t in range(iter_count):
        print('t:', t)
        main_t.clear()
        for seq, w in enumerate(k_wheels):
            radius = w.r*one_unit
            rad = t*w.s*factor
            r_vec = k_vecs[seq] = (math.cos(rad)*radius, math.sin(rad)*radius)
            # print("r_vec[%d]: %s" % (seq, r_vec))
            # 计算圆心, 前面的几个圆半径向量相连即是当前圆的圆心
            o = [0, 0]
            for _i in range(seq):
                o[0] += k_vecs[_i][0]
                o[1] += k_vecs[_i][1]
            # print("origin[%d]: %s" % (seq, o))
            main_t.color(colors[seq])
            if seq > 0:
                paint_circle(main_t, o[0], o[1], radius)
            # 画半径向量
            r_vec_end = (o[0]+r_vec[0], o[1]+r_vec[1])
            main_t.teleport(o[0], o[1])
            main_t.goto(r_vec_end[0], r_vec_end[1])
            paint_arrow(main_t, r_vec_end[0], r_vec_end[1], rad)
            # 绘制轨迹, 最后一个圆, 其半径向量终点
            if seq == k-1:
                if locus_begin:
                    locus_t.goto(r_vec_end[0], r_vec_end[1])
                else:
                    locus_t.teleport(r_vec_end[0], r_vec_end[1])
                    locus_t.color(locus_color)
                    locus_t.dot(4)
                    locus_t.width(4)
                    locus_begin = True
    _save_file(main_t, k_wheels)
    done()


if __name__ == "__main__":
    k_wheels = [
        # Wheel(r=4, s=1),
        Wheel(r=2, s=1),
        Wheel(r=1, s=-2),
    ]
    print(k_wheels)

    paint_k_wheels(k_wheels)
