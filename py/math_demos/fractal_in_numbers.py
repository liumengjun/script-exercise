"""
受到"漫士】二进制里隐藏的分形：到底什么是分数维度？"视频启发, 写了这个 python 程序
把数字以2进制表示, 从0到N, bit_count是偶数前进奇数转向绘制图形...
视频链接: https://www.bilibili.com/video/BV1tuab6rEAY/

base(进制) = 2
rotateM(360几等分): 1,2没啥意义, 3,6差不多(科赫雪花), 4,8闭环, 5??(魔王三角), 7??(妖怪角), 9,11 一坨, 10??(疙瘩) 12??看不到全貌(粗麻绳大雪花)应该是科赫雪花
2进制时, bit_count表意唯一, 绘制时策略也无歧义: 偶数前进, 奇数转向
>=3进制时, bit_count有两种实现: 1, 不为0的位数的数字和; 2, 不为0的位数的数量。
>=3进制时, 绘制时也有两种策略: 1, mod(base)==0前进, 其他转向; 2, 偶数前进, 奇数转向。
base>=3进制时, rotateM=6, 图形结果有时base和base加6貌似, 大致相似起点和密度不一样。
有些看似图形闭环了, 但是把N调大可能还会扩大。
参数分项太多, 没有探索完...
"""
from turtle import *


# 调整以下参数, 观察绘制图形变化。 (可能需要调整初始位置和方向以便绘制不出界, 见`_init()`函数)
base = 2  # 数进制, 二进制
rotateM = 6  # 圆周几等分, 转向时只转一份
rotate = 360/rotateM
one_unit = 10  # 前进一步的像素数
N = 1000  # 迭代多少步
version = "2.2"  # >=3进制时的实现版本


def _parse_args():
    import sys
    args_cnt = len(sys.argv)
    print(args_cnt, sys.argv)
    if args_cnt > 1:
        global base
        base = int(sys.argv[1])
    if args_cnt > 2:
        global rotateM, rotate
        rotateM = int(sys.argv[2])
        rotate = 360/rotateM
    if args_cnt > 3:
        global one_unit
        one_unit = int(sys.argv[3])
    if args_cnt > 4:
        global N
        N = int(sys.argv[4])
    if args_cnt > 5:
        global version
        version = sys.argv[5]


def dec_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    is_negative = n < 0
    n = abs(n)
    while n:
        digits.append(str(n % base) if n %
                      base < 10 else chr(ord('a') + n % base - 10))
        n //= base
    if is_negative:
        digits.append('-')
    return ''.join(reversed(digits))


def dec_to_base_bit_count(n, base):
    """
    base进制表示时, 不为零的位数相加
    """
    if n == 0:
        return 0
    bit_count = 0
    n = abs(n)
    while n:
        bit_count += n % base
        n //= base
    return bit_count


def dec_to_base_bit_count_v2(n, base):
    """
    base进制表示时, 不为零的位的数量
    """
    if n == 0:
        return 0
    bit_count = 0
    n = abs(n)
    while n:
        if n % base:
            bit_count += 1
        n //= base
    return bit_count


def _init():
    # init window & canvas
    setup(1.0, 1.0)  # 窗口是整个屏幕
    ww = window_width()
    wh = window_height()
    speed(0)
    screensize(ww-50, wh-100)  # 画布大小
    sw, sh = screensize()

    # 初始位置和方向
    penup()
    # 初始位置, 默认从画布中央开始画
    # teleport(sw/2-100, -sh/2+100)  # 左下角开始
    # teleport(sw/2-50, 100)  # 右上部分开始
    pendown()
    # right(rotate)  # 初始方向


def main():
    _parse_args()
    _init()

    dot(3, 'green')  # 开始画个绿点
    color('blue')  # 行走线条是蓝色
    # loop run
    for i in range(N):
        if i % 100 == 0:
            print(i)  # 显示进度
        # bit_count = i.bit_count()
        # print(i, bin(i), bit_count)
        # base_str = dec_to_base(i, base)
        if base == 2:
            bit_count = i.bit_count()
        else:
            if version.startswith("1."):
                bit_count = dec_to_base_bit_count(i, base)
            else:
                bit_count = dec_to_base_bit_count_v2(i, base)
        # print(i, base_str, bit_count)
        mod = base
        if base >= 3 and version.endswith(".2"):
            mod = 2
        if bit_count % mod == 0:
            forward(one_unit)
        else:
            left(rotate)
    dot(3, 'red')  # 结束画个红点

    hideturtle()
    _save_file()
    done()


def _save_file():
    """保存为 postscript 文件"""
    version_str = '-v'+version if base != 2 else ''
    filename = 'var/base_%d-rotateM_%d-unit_%dpx-count_%d%s.ps' % (
        base, rotateM, one_unit, N, version_str)
    print(filename)
    save(filename, overwrite=True)


if __name__ == '__main__':
    main()
