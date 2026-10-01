import math
import decimal

decimal.getcontext().prec = 128

"""
计算自然常数(e)小数点后128位数值。
math.e 的数值只保留到小数点后15位，对于双精度浮点数足够了。
"""


def _f1n(n: int):
    return 1 / math.factorial(n)


def _dec_f1n(n: int):
    return decimal.Decimal(1) / decimal.Decimal(math.factorial(n))


def calc_by_pri(count=100) -> float:
    return sum([_f1n(n) for n in range(1 + count)])


def calc_by_dec(count=100) -> decimal.Decimal:
    return sum([_dec_f1n(n) for n in range(1 + count)], start=decimal.Decimal(0))


if __name__ == '__main__':
    print('math.e:', math.e)

    print()
    print('1, calculate e by primitive type'.center(80, '='))
    print('calculate e by primitive type, result =', calc_by_pri())
    print('primitive type double float precision in radix 10 is:', math.log10(2) * 52)
    for c in range(30):
        print("N:", c, calc_by_pri(c))

    print()
    print('2, calculate e by decimal'.center(80, '='))
    print("decimal's Context:\n", decimal.getcontext())
    print("decimal's precision:", decimal.getcontext().prec)
    print('calculate e by decimal:\n', calc_by_dec())
    for c in range(100):
        print("N:", c, calc_by_dec(c))

    print()
    print('note'.center(80, '-'))
    dec_e = calc_by_dec()
    print(dec_e)
    print('radix is:', dec_e.radix())
    print(dec_e.as_tuple())
