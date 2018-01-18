import random

'''
# 微信或支付宝，随机红包（拼手气红包）算法
'''
def random_red_package(total: float, num: int):
    if total * 100 < num:
        raise Exception("total is too small")
    if num == 1:
        yield total
    else:
        # total * 100, unit is fen of RMB。each one has 1 fen at least
        rest = total * 100
        for i in range(0, num - 1):
            t = rest * 2 / (num - i) * random.random()
            f = int(t) or 1
            yield f / 100
            rest -= f
        yield rest / 100


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Please input params: total and count")
        exit(-1)

    total = float(sys.argv[1])
    num = int(sys.argv[2])

    if total <= 0 or num <= 0:
        print("Please input total (>=0.01) and count (>1)")
        exit(-2)

    total_fen = int(total * 100)
    if total_fen < num:
        print("The total at least may be %.2f" % (num / 100,))
        exit(-3)

    total = total_fen / 100
    print("total = %.2f, count = %d" % (total, num))
    for f in random_red_package(total, num):
        print(f)
