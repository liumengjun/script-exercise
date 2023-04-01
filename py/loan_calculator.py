#!/usr/bin/python
# -*- coding:utf-8 -*-
# coding=utf-8
#
# loan calculator
# 处理浮点数还有一种做法是乘以100转换为分这样变为整数处理，这里没有那样做

###################################
# 等额本息: (Average Capital Plus Interest)
# 等额本金: (Average Capital)
###################################


def calc_acpi_per_month(total_pri, months, month_rate, fixup=True):
    '''
    计算`等额本息`每月还款额

    total_pri: 贷款总额
    months: 月数
    month_rate: 月利率

    return 每月还款额
    '''
    com_rate = (1 + month_rate)**months
    a = total_pri * month_rate * com_rate / (com_rate - 1)
    return fixup and _fix_float(a, mode='UP') or a


def _fix_float(amount, n=2, mode='ROUND'):
    '''
    保留n位小数，第(n+1)位小数mode: UP 向上取整, DOWN 向下取整, ROUND 四舍五入
    '''
    import math
    nnn = 10**n
    mode = mode.upper()
    if mode == 'UP':
        return math.ceil(amount * nnn) / nnn
    if mode == 'DOWN':
        return math.floor(amount * nnn) / nnn
    # if mode == 'ROUND':
    return round(amount * nnn) / nnn


def calc_acpi_details(total_pri, months, month_rate):
    '''
    计算`等额本息`还款详情

    total_pri: 贷款总额
    months: 月数
    month_rate: 月利率

    return 各月还款详情
    '''
    per_month_amount = calc_acpi_per_month(total_pri, months, month_rate)
    details = []
    remaining = total_pri
    for i in range(months):
        if i == months - 1:
            pri = remaining
            interest = _fix_float(per_month_amount - pri)
            remaining = 0.0
        else:
            interest = _fix_float(remaining * month_rate)
            pri = _fix_float(per_month_amount - interest)
            remaining = _fix_float(remaining - pri)
        details.append({
            'seq': (i + 1),
            'gross': _fix_float(per_month_amount),
            'principal': pri,
            'interest': interest,
            'remaining': remaining,
        })
    return details


def calc_ac_details(total_pri, months, month_rate):
    '''
    计算`等额本金`还款详情

    total_pri: 贷款总额
    months: 月数
    month_rate: 月利率

    return 各月还款详情
    '''
    pri_per_month = _fix_float(total_pri / months)
    details = []
    remaining = total_pri
    for i in range(months):
        interest = _fix_float(remaining * month_rate)
        if i == months - 1:
            pri_per_month = remaining
            remaining = 0.0
        else:
            remaining = _fix_float(remaining - pri_per_month)
        details.append({
            'seq': (i + 1),
            'gross': _fix_float(pri_per_month + interest),
            'principal': pri_per_month,
            'interest': interest,
            'remaining': remaining,
        })
    return details


def _test():
    total = 123.45
    rate = 0.03
    for m in range(1,1001):
        details = calc_acpi_details(total, m, rate)
        total_pri = round(sum(x['principal'] for x in details),2)
        if total != total_pri:
            print('ACPI', m, total, total_pri)
        details = calc_ac_details(total, m, rate)
        total_pri = round(sum(x['principal'] for x in details),2)
        if total != total_pri:
            print('AC', m, total, total_pri)
    # print(details)

if __name__ == "__main__":
    # _test()
    # exit()
    import sys

    if len(sys.argv) < 4:
        print("Please input 4~5 params: ACPI|AC total month_count month_rate [finish_months]")
        exit(-1)

    l_type = sys.argv[1].upper()
    total = float(sys.argv[2])
    m_count = int(sys.argv[3])
    m_rate = float(sys.argv[4])
    finish_months = len(sys.argv)>=6 and int(sys.argv[5]) or None

    import pprint as pp

    if l_type == 'ACPI':
        details = calc_acpi_details(total, m_count, m_rate)
    else:
        details = calc_ac_details(total, m_count, m_rate)
    pp.pprint(details)
    print('total principal: ', _fix_float(sum(x['principal'] for x in details)))
    print('total interest: ', _fix_float(sum(x['interest'] for x in details)))
    print('total cost: ', _fix_float(sum(x['gross'] for x in details)))
    if finish_months and finish_months>0:
        details = details[:finish_months]
        print('finish principal: ', _fix_float(sum(x['principal'] for x in details)))
        print('finish interest: ', _fix_float(sum(x['interest'] for x in details)))
        print('finish cost: ', _fix_float(sum(x['gross'] for x in details)))
