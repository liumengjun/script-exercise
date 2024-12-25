# -*- coding: utf-8 -*-
from decimal import *

"""
割圆术，就是不断倍增圆内接正多边形的边数求出圆周率的方法。
- 按周长算, `π = C/d = n*sin(180/n)`。
- 按面积算, 圆的面积为`S=πr^2`, 单位圆的面积就是`π`; `π = n*sin(360/n)/2 = n*sin(180/n)*cos(180/n)`。

下面，用圆内接`正3*2^n边形`的面积去求取圆周率。
对于任意`n(n>=1)`,有:
``S正3*2^n边形 = S正3*2^(n-1)边形/cos(60/2^(n-1))``
记 `a(n) = cos(60/2^(n-1)) => S正3*2^n边形 = S正六边形/(a1*...*a(n))`
``S正六边形 = 3*sin(60) = 3/2*√3``
根据半角公式，可得`a(n) = √(a(n-1)+1)/2)`
---
余弦半角公式`cos(α/2) = ±√((cos(α)+1)/2)`
"""

"""
传统计算圆周率的方法依赖于几何构造、简单的数列展开或解析方法，例如割圆术、泰勒级数法等。
现代计算圆周率的方法主要依赖于复杂的迭代算法、快速收敛的级数与强大的计算机的计算能力，例如查德诺夫斯基算法 (Chudnovsky Algorithm)、高斯-勒让德算法等。
参考:
- 百科 https://baike.baidu.com/item/%E5%9C%86%E5%91%A8%E7%8E%87/139930
- 博客 https://www.cnblogs.com/Nikola-K/p/16842536.html
"""

# print(getcontext())  # 默认`prec` = 28
getcontext().prec = 256  # 小数长度


def calc_s3_2_n(n=1024):
    a, p = Decimal('0.5'), Decimal('1')
    for _ in range(n):
        a = ((a+1)/2)**Decimal('0.5')
        p *= a
    pi = Decimal('1.5')*(Decimal('3')**Decimal('0.5'))/p
    print('π ≈ '+str(pi))


def calc_leibniz_pi(n=10240):
    s = Decimal(0)
    for i in range(n):
        a = Decimal(i)
        s += (-1)**(i & 1)*Decimal(1)/(2*a+1)
    pi = 4*s
    print('π ≈ '+str(pi))


def calc_gauss_legendre(n=5):
    a0 = Decimal(1)
    b0 = Decimal(2).sqrt()/2  # 1/√2
    t0 = Decimal(1)/4
    p0 = Decimal(1)
    for _ in range(n):
        pi0 = (a0+b0)**2/4/t0
        print("%.14f %.14f %.14f --- %.16f" % (a0, b0, t0, pi0))
        a = (a0+b0) / 2
        b = (a0*b0).sqrt()
        t = t0 - (a0-a)**2*p0
        p = 2*p0
        a0, b0, t0, p0 = a, b, t, p
        pi = (a0+b0)**2/4/t0
        print("Δ = %.14g" % (pi-pi0))
    print('π ≈ '+str(pi))


def calc_wallis(n=10240):
    pi = Decimal(2)
    for i in range(1, n+1):
        t = (Decimal(i)*2)**2
        pi *= t/(t-1)
    print('π ≈ '+str(pi))


def calc_machin_like(n=1024):
    # also typed Maqin
    a = Decimal(1)/Decimal(5)
    b = Decimal(1)/Decimal(239)
    s = Decimal(0)
    for i in range(n):
        t = Decimal(2*i+1)
        s += (-1)**(i & 1)*(a**t*4-b**t)/t
    pi = 4*s
    print('π ≈ '+str(pi))


def calc_chudnovsky(n=10):
    import math
    s = Decimal(0)
    for k in range(n):
        p = math.factorial(6*k)*(545140314*k+13591409)
        q = math.factorial(3*k)*(math.factorial(k)**3) * (640320**(3*k))
        s += (-1)**(k & 1)*Decimal(p)/Decimal(q)
    pi = Decimal(53360)*(Decimal(640320).sqrt())/s
    print('π ≈ '+str(pi))


def calc_bbp(n=10):
    getcontext().prec = 80
    s = Decimal(0)
    for k in range(n + 1):
        k8 = Decimal(k)*8
        m1 = Decimal(4) / (k8 + 1)
        m2 = Decimal(2) / (k8 + 4)
        m3 = Decimal(1) / (k8 + 5)
        m4 = Decimal(1) / (k8 + 6)
        p = Decimal(1) / Decimal(16)**k
        s += p*(m1 - m2 - m3 - m4)
    print(n, s)


if __name__ == "__main__":
    # calc_s3_2_n()
    # calc_leibniz_pi()
    # calc_gauss_legendre(10)
    # calc_wallis()
    # calc_machin_like()
    # calc_chudnovsky()
    for i in range(15):
        calc_bbp(i)
    pass
    import math
    print(math.pi)
