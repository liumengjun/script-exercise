"""
欧拉猜想
莱昂哈德·欧拉于1769年提出的数论猜想，
断言n>2时，n-1个正整数的n次幂之和不可能等于另一个正整数的n次幂，
但该猜想已被反例推翻。


27^5 + 84^5 + 110^5 + 133^5 = 144^5    (1966年，美国数学家L. J. Lander和T. R. Parkin)

2682440^4 + 15365639^4 + 18796760^4 = 20615673^4    (1988年，哈佛大学的Noam Elkies, n=4时方程存在无穷多个整数解)

95800^4 + 217519^4 + 414560^4 = 422481^4    (Roger Frye找到该方程的最小整数解)


尝试寻找最小k值，使得
    A1^n + A2^n + A3^n + ... + Ak^n = B^n
"""


import math
from config import timing


@timing(pattern="方法%s运行耗时%.2f秒")
def search4p5to1p5():
    """
    寻找 a^5 + b^5 + c^5 + d^5 = e^5
    """
    found = False
    N = 200
    for a in range(1, N):
        print("progress %d of %d: %.2f%%" % (a, N, a*100/N,))
        if found:
            break
        for b in range(a, N):
            if found:
                break
            for c in range(b, N):
                if found:
                    break
                for d in range(c, N):
                    sumM = a**5+b**5+c**5+d**5
                    tmpE = math.pow(sumM, 1/5)
                    if int(tmpE)**5 == sumM:
                        print("%d^5 + %d^5 + %d^5 + %d^5 = %d^5" %
                              (a, b, c, d, tmpE))
                        found = True
                        break


@timing(pattern="方法%s运行耗时%.2f秒")
def search3p4to1p4(N=200):
    """
    寻找 a^4 + b^4 + c^4 = d^4
    """
    found = False
    for a in range(1, N):
        print("progress %d of %d: %.2f%%" % (a, N, a*100/N,))
        if found:
            break
        for b in range(a, N):
            if found:
                break
            for c in range(b, N):
                sumM = a**4+b**4+c**4
                tmpD = math.pow(sumM, 1/4)
                if int(tmpD)**4 == sumM:
                    print("%d^4 + %d^4 + %d^4 = %d^5" %
                            (a, b, c, tmpD))
                    found = True
                    break


@timing(pattern="方法%s运行耗时%.2f秒")
def searchKNumPowNSum(k, n, search_max=200, search_min=1, found_end=True):
    """
    寻找k个整数的n次幂和恰好是另一个整数的n次幂
      A1^n + A2^n + A3^n + ... + Ak^n = B^n
    """
    A = [0]*k
    # print(A)

    def genNextKNum(depth, start):
        """生成一组数"""
        for a in range(start, search_max + 1):
            if depth == 1:
                print("progress %d of %d~%d: %.2f%%" %
                      (a, search_min, search_max, (a-search_min)*100/(search_max-search_min),))
            A[depth-1] = a
            if depth == k:
                yield A
                continue
            # 层次(或下标)加一, 后面的数不小于前面的数
            for ele in genNextKNum(depth+1, a):
                yield ele

    found = False
    found_count = 0
    for arr in genNextKNum(1, search_min):
        # print(arr)
        if found and found_end:
            break
        # calc
        sumM = 0
        for a in A:
            sumM += a**n
        tmpE = math.pow(sumM, 1/n).__round__()
        # 此处用`round`, `s^(1/5)`会比实际值偏大还好, 但是`s^(1/3), s^(1/6)`会比实际值偏小
        if tmpE**n == sumM:
            found = True
            found_count += 1
            # 输出
            text = "found %d^%d" % (A[0], n)
            for i in range(1, k):
                text += " + %d^%d" % (A[i], n)
            text += " = %d^%d" % (tmpE, n)
            print(text)
    print("found_count: %d" % found_count)


if __name__ == '__main__':
    # search4p5to1p5()  # 27^5 + 84^5 + 110^5 + 133^5 = 144^5
    # searchKNumPowNSum(2, 2, 100, 3, False)  # 100以内勾股数, 63组
    # searchKNumPowNSum(3, 3, 100, 1, False)  # 100以内三数立方和等立方, 98组
    # searchKNumPowNSum(4, 4, 200, 1, False)  # 200以内四数四次方和等四次方, 无解
    # searchKNumPowNSum(5, 5, 100, 1, False)  # 100以内五数五次方和等五次方, 3组
    # searchKNumPowNSum(6, 6, 100, 1, False)  # 100以内6数6次方和等6次方, 太慢了
    # searchKNumPowNSum(4, 5, 200)  # 和 search4p5to1p5() 效果相同
    searchKNumPowNSum(4, 5, 150, 20)  # 和 search4p5to1p5() 效果相同
    # searchKNumPowNSum(5, 6, 200)  # 太慢了
    # searchKNumPowNSum(3, 4, 200)  # 无解
    # searchKNumPowNSum(3, 4, 2000)  # 太慢了
    # search3p4to1p4(50000)  # 太慢了
    pass
