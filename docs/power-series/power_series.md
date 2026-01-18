## 幂级数

> 通项为幂函数的函数项级数:

$$
\sum_{n=0}^{\infty} a_{n}(x-x_{0})^{n} = a_{0}+a_{1}(x-x_{0})+a_{2}(x-x_{0})^{2}+a_{3}(x-x_{0})^{3}+\cdots
$$

> 我们常取 $x_{0}=0$, 得到:

$$
\sum_{n=0}^{\infty} a_{n}x^{n} = a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots
% flalign 左对齐 有的工具不支持
%\require{ams}
%\begin{flalign*}
%& \quad \sum_{n=0}^{\infty} a_{n}x^{n} = a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\cdots & \\
%\end{flalign*}
$$


### 泰勒(Taylor)级数, 麦克劳林(Maclaurin)级数

> 若函数$f(x)$在$x_{0}$处有任意阶导数, 则可以构造以下幂级数, 称为$f(x)$在$x_{0}$处的`泰勒级数`。
> 通常把有限项加**余项**的形式叫作`泰勒展开式`, 或称`泰勒公式`。

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n} = f(x_{0})+f'(x_{0})(x-x_{0})+\frac{f''(x_{0})}{2!}(x-x_{0})^{2}+\cdots
$$

> 特别地, $x_{0}=0$时, 称级数为`麦克劳林级数`。

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^{n} = f(0)+f'(0)x+\frac{f''(0)}{2!}x^{2}+\frac{f'''(0)}{3!}x^{3}+\cdots
$$


### 常见幂级数

$$
\begin{align}
& e^{x} = \sum_{n=0}^{\infty}\frac{x^{n}}{n!} = 1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+\cdots, \quad (x \in R) \\
& \ln(1+x) = \sum_{n=0}^{\infty}(-1)^{n}\frac{x^{n+1}}{n+1} = x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\frac{x^{5}}{5}-\cdots, \quad (x \in(-1,1]) \\
% & \qquad\qquad \stackrel{\text{or}}{=} \sum_{n=1}^{\infty}(-1)^{(n-1)}\frac{x^{n}}{n} \\
& \sin(x) = \sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n+1}}{(2n+1)!} = x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\frac{x^{9}}{9!}-\cdots, \quad (x \in R) \\
& \cos(x) = \sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n}}{(2n)!} = 1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\frac{x^{8}}{8!}-\cdots, \quad (x \in R) \\
& \arctan(x) = \sum_{n=0}^{\infty}(-1)^{n}\frac{x^{2n+1}}{2n+1} = x-\frac{x^{3}}{3}+\frac{x^{5}}{5}-\frac{x^{7}}{7}+\frac{x^{9}}{9}-\cdots, \quad (x \in[-1,1]) \\
& \arcsin(x) = x+\sum_{n=1}^{\infty}\frac{(2n-1)!!}{(2n)!!}\frac{x^{2n+1}}{2n+1} = x+\frac{x^{3}}{6}+\frac{3}{40}x^{5}+\frac{5}{112}x^{7}+\frac{35}{1152}x^{9}+\cdots, \quad x \in[-1,1] \\
& \frac{1}{1-x} = 1+\sum_{n=1}^{\infty}x^{n} = 1+x+x^{2}+x^{3}+x^{4}+\cdots, \quad x\in(-1,1) \\
& \frac{1}{1+x} = 1+\sum_{n=1}^{\infty}(-1)^{n}x^{n} = 1-x+x^{2}-x^{3}+x^{4}-\cdots, \quad x\in(-1,1) \\
& \sqrt{1+x} = 1+\sum_{n=1}^{\infty}(-1)^{(n-1)}\frac{(2n-3)!!}{(2n)!!}x^{n} = 1+\frac{x}{2}-\frac{x^{2}}{8}+\frac{x^{3}}{16}+\cdots, \quad x \in[-1,1] \\
& \frac{1}{\sqrt{1+x}} = 1+\sum_{n=1}^{\infty}(-1)^{n}\frac{(2n-1)!!}{(2n)!!}x^{n} = 1-\frac{x}{2}+\frac{3}{8}x^{2}-\frac{5}{16}x^{3}+\cdots, \quad x \in(-1,1] \\
& (1+x)^{k} = 1+\sum_{n=1}^{\infty}\left(\begin{array}{l}k\\n\end{array}\right)x^{n} = 1+kx+\frac{k(k-1)}{2!}x^{2}+\frac{k(k-1)(k-2)}{3!}x^{3}+\cdots, \quad |x|<1 \\
\end{align}
$$

> 上面的公式可能渲染不出来, 可以查看以下图片, 还有一些网络收集的(图片样式不一, 此处没有直接渲染, 请各个打开查看), 如下:

- [常见幂级数](常见幂级数.png)
- [幂级数补充2](幂级数补充2.png)
- [幂级数补充n](幂级数补充n.jpg)


### 参考

> 拾人牙慧, 稍加整理。
> 想来是计算一下`自然指数(e)`高精度数值(比如小数点后128位), 见脚本[calc_e.py](../../py/power_series/calc_e.py)。
> 然后就收集了一些幂级数的知识点。毕竟计算机计算指数对数三角函数等是依靠此数学理论的。
> 另外之前还有个计算`圆周率(π)`的脚本, 在[calc_pi.py](../../py/calc_pi/calc_pi.py)。

- [`教案`函数的幂级数展开及其应用](https://pdf.hanspub.org/pm2024148_11252537.pdf)
- [`教案`幂级数与Taylor展开式](http://staff.ustc.edu.cn/~rui/ppt/math-analysis/chap7_3.html)
- [`教案`幂级数](https://math.fudan.edu.cn/_upload/article/files/8a/c7/b6bc60b64933acee041a351adda9/66ceeb73-64e3-4a1a-b59c-a341e9914deb.pdf)
- [`博客`万字长文看够幂级数](https://zhuanlan.zhihu.com/p/186219101)
- [`百科`幂级数](https://baike.baidu.com/item/%E5%B9%82%E7%BA%A7%E6%95%B0/1044925)
- [`百科`泰勒级数](https://baike.baidu.com/item/%E6%B3%B0%E5%8B%92%E7%BA%A7%E6%95%B0/7289427)
- [`百科`麦克劳林公式](https://baike.baidu.com/item/%E9%BA%A6%E5%85%8B%E5%8A%B3%E6%9E%97%E5%85%AC%E5%BC%8F/3430023)
