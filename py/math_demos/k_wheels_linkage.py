from dataclasses import dataclass
import math
import tkinter as TK
from turtle import Turtle, done

_COLORS = ['orange', 'green', 'blue', 'red', 'gold', 'violet', 'cyan', 'brown']
_LOCUS_COLOR = 'fuchsia'  # 轨迹颜色
_TIP_COLOR = 'purple'  # 模拟笔尖, 比 locus_color 颜色深
_ONE_UNIT = 30  # 1单位像素数
_FACTOR = 50  # 1弧度步数


@dataclass
class Wheel:
    # i: int = 0  # id
    r: float = 1.0  # radius
    s: float = 0.0  # speed


def paint_arrow(pen, o, end, arraw_rad=0.0, size=10):
    pen.teleport(o[0], o[1])
    pen.goto(end[0], end[1])
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


def _save_file(screen, k_wheels, one_unit, rounds=None, ends=None):
    """保存为 postscript 文件"""
    k = len(k_wheels)
    filename = 'var/k_%d-[%s]-unit_%dpx%s%s.ps' % (
        k,
        ','.join(['r%.1f_s%.1f' % (w.r, w.s) for w in k_wheels]),
        one_unit,
        rounds and ('-rounds_%.2f' % rounds) or '',
        ends or '',
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


_turtle_inited = False
_turtle_cached = ()


def _init_turtle(k_wheels, paused_wrap=None, rounds_wrap=None):
    global _turtle_inited, _turtle_cached
    if not _turtle_inited:
        # 两个 Turtle
        main_t = Turtle(visible=False)  # 画滚动的圆
        locus_t = Turtle(visible=False)  # 画轨迹
        # print(main_t.getscreen() == locus_t.getscreen())  # True
        screen = main_t.getscreen()
        screen.setup(1.0, 1.0)
        _pause_tk_var = TK.BooleanVar()  # 创建 tkinter 变量
    else:
        main_t, locus_t, screen, _pause_tk_var = _turtle_cached
    screen.tracer(0, 0)  # 加快动画速度, 关闭`tracing`, 手动`update`
    screen.reset()  # 不使用 clear(), 否则有问题
    main_t.hideturtle()  # 使用`reset()`后, 须重新调用`hideturtle()`
    locus_t.hideturtle()

    # rounds_wrap 变了, save 需要重新绑定。(后面的 pause 无所谓)
    def __save_file(*args):
        if not rounds_wrap:
            return
        _save_file(screen, k_wheels, _ONE_UNIT, rounds_wrap[0])
    screen.onkeyrelease(__save_file, 's')

    if _turtle_inited:
        return main_t, locus_t, screen

    print(_pause_tk_var, _pause_tk_var.get())

    def __toggle_paused(*args):
        if not paused_wrap:
            return
        print('is_paused:', paused_wrap[0])
        if not paused_wrap[0]:
            paused_wrap[0] = True
            print('is_paused:', paused_wrap[0])
            screen.cv.master.wait_variable(_pause_tk_var)
        else:
            paused_wrap[0] = False
            print('is_paused:', paused_wrap[0])
            _pause_tk_var.set(False)

    screen.onkeypress(__toggle_paused, 'space')
    screen.onclick(__toggle_paused)
    screen.listen()
    _turtle_cached = (main_t, locus_t, screen, _pause_tk_var)
    _turtle_inited = True
    return main_t, locus_t, screen


def _paint_locus(locus_t, r_vec_end, locus_begin_wrap=None):
    locus_begin = locus_begin_wrap and locus_begin_wrap[0]
    if locus_begin:
        locus_t.goto(r_vec_end[0], r_vec_end[1])
    else:
        locus_t.teleport(r_vec_end[0], r_vec_end[1])
        locus_t.color(_LOCUS_COLOR)
        locus_t.dot(4)
        locus_t.width(4)
        if locus_begin_wrap:
            locus_begin_wrap[0] = True


def _paint_k_wheels_1ce(main_t, screen, k_wheels, t_factor, once=False):
    k = len(k_wheels)
    k_vecs = [(0, 0)]*k  # 用于计算存储半径向量
    for seq, w in enumerate(k_wheels):
        radius = w.r*_ONE_UNIT
        rad = w.s*t_factor
        r_vec = k_vecs[seq] = (math.cos(rad)*radius, math.sin(rad)*radius)
        # print("r_vec[%d]: %s" % (seq, r_vec))
        # 计算圆心, 前面的几个圆半径向量相连即是当前圆的圆心
        o = [0, 0]
        for _i in range(seq):
            o[0] += k_vecs[_i][0]
            o[1] += k_vecs[_i][1]
        # print("origin[%d]: %s" % (seq, o))
        main_t.color(_COLORS[seq % len(_COLORS)])
        if seq > 0:
            paint_circle(main_t, o[0], o[1], radius)
        elif once:
            paint_circle(main_t, o[0], o[1], radius)
        # 画半径向量
        r_vec_end = (o[0]+r_vec[0], o[1]+r_vec[1])
        paint_arrow(main_t, o, r_vec_end, rad)
        # 绘制轨迹, 最后一个圆, 其半径向量终点, 返回坐标外层绘制
        if seq == k-1:
            main_t.dot(6, _TIP_COLOR)  # 模拟笔尖, 比 locus_color 颜色深
    if once:
        screen.update()
        _save_file(screen, k_wheels, _ONE_UNIT, ends='-at%.2f' % t_factor)
    return r_vec_end  # 返回坐标外层绘制


def paint_k_wheels(k_wheels, append_info=None):
    if not k_wheels:
        return
    paused_wrap = [False]
    locus_begin_wrap = [False]
    rounds_wrap = [0.0]
    main_t, locus_t, screen = _init_turtle(k_wheels, paused_wrap, rounds_wrap)

    max_rounds = _calc_max_rounds(k_wheels)
    iter_count = int(math.pi*2*_FACTOR*max_rounds)+2

    # 绘制 k_wheels 和 append_info 文字到屏幕上
    sw, sh = screen.window_width(), screen.window_height()
    locus_t.teleport(-sw/2+20, -sh/2+20)  # 左下角
    locus_t.write(str(k_wheels)+str(append_info or ''),
                  font=("Arial", 16, "normal"))

    # 画第一个圆(不动), 从圆的最低点开始画的
    locus_t.teleport(0, 0)
    locus_t.dot(3, 'black')
    locus_t.color(_COLORS[0])
    locus_t.width(1)
    paint_circle(locus_t, 0, 0, k_wheels[0].r*_ONE_UNIT)
    for t in range(iter_count):
        # 使用`tk.wait_variable`实现暂停, 下面`input`方式就不用了
        # if paused_wrap[0]:
        #     print('is_paused:', paused_wrap[0])
        #     input("按回车继续...\n")  # 暂停绘制，在终端回车继续
        #     paused_wrap[0] = False
        #     print('is_paused:', paused_wrap[0])
        t_factor = t/_FACTOR
        rounds_wrap[0] = t_factor/math.pi/2
        if t_factor % (math.pi/4) <= 0.01:  # 粗略估计进度
            print('t: %d, t_factor: %.2f, rounds: %.2f' %
                  (t, t_factor, rounds_wrap[0]))
        main_t.clear()
        r_vec_end = _paint_k_wheels_1ce(main_t, screen, k_wheels, t_factor)
        _paint_locus(locus_t, r_vec_end, locus_begin_wrap)
        screen.update()  # 手动update
    _save_file(screen, k_wheels, _ONE_UNIT)


def gen_k_wheels(r_start: int, r_end: int, s_start: int, s_end: int, arr: list[Wheel]):
    """
    生成一组`wheel`(生成器方式), 保存到`arr`内, yield arr 本身:
    个数`k=len(arr)`
    特殊处理:
        - 第一个轮不转的情况, 跳过
        - 所有轮速度都相同的情况, 跳过
    """
    def _gen_wheels_r(r_depth, r_start, r_end):
        for a in range(r_start, r_end + 1):
            arr[r_depth-1].r = a
            if r_depth == len(arr):
                yield arr
                continue
            # 层次(或下标)加一
            for ele in _gen_wheels_r(r_depth+1, r_start, r_end):
                yield ele

    def _gen_wheels_s(s_depth, s_start, s_end):
        for a in range(s_start, s_end + 1):
            if a == 0 and s_depth == 1:
                continue  # 第一个轮不转的情况, 跳过
            arr[s_depth-1].s = a
            if s_depth == len(arr):
                s_same = True
                for i in range(s_depth-1):
                    s_same = s_same and (arr[i].s == a)
                if s_same:
                    continue  # 所有轮速度都相同的情况, 跳过
                for ele in _gen_wheels_r(1, r_start, r_end):
                    yield ele
                continue
            # 层次(或下标)加一
            for ele in _gen_wheels_s(s_depth+1, s_start, s_end):
                yield ele

    for ele in _gen_wheels_s(1, s_start, s_end):
        yield ele


def explore_k_wheels_kinds(k_wheels, r, s, skip_count=0):
    # 由 gen_k_wheels 生成多种组合, 然后绘制图形
    k = len(k_wheels)
    # 计算生成预计数量着实难, 生成时过滤其实不如绘制时过滤简单
    expect_count = (r[1]-r[0]+1)**k*(s[1]-s[0]+1)**k - \
        (r[1]-r[0]+1)**k*(s[1]-s[0]+1)**(k-1) - \
        ((r[1]-r[0]+1)**k*(s[1]-s[0]+1)-(r[1]-r[0]+1)**k)
    # 首先空跑一遍计算总数
    total_count = 0
    for _ in gen_k_wheels(r[0], r[1], s[0], s[1], k_wheels):
        total_count += 1
    ok = total_count == expect_count
    print('k: %d, total_count: %d, expect_count: %d, ok: %s' %
          (k, total_count, expect_count, ok))
    if not ok:
        return
    # 绘制
    for i, wheels in enumerate(gen_k_wheels(r[0], r[1], s[0], s[1], k_wheels), 1):
        skip = i <= skip_count
        print('\n%d/%d: %s, skip: %s' % (i, total_count, wheels, skip))
        if skip:
            continue
        paint_k_wheels(k_wheels, '-No.'+str(i))


if __name__ == "__main__":
    k_wheels = [
        # Wheel(r=2.3, s=1),
        # Wheel(r=1, s=-2.5),
        # Wheel(r=3, s=3),
        # Wheel(r=3, s=-1),
        # Wheel(r=2, s=2),
        # Wheel(r=2, s=-1),
        # Wheel(r=1, s=-3),
        Wheel(r=1, s=1),
        Wheel(r=1, s=-3),
        Wheel(r=2, s=4),
    ]
    print(len(k_wheels), k_wheels, '\n')

    # main_t, locus_t, screen = _init_turtle(k_wheels)
    # _paint_k_wheels_1ce(main_t, screen, k_wheels, 0.785, True)
    # paint_k_wheels(k_wheels)

    explore_k_wheels_kinds(k_wheels, [1, 3], [-5, 5], 70)

    done()
