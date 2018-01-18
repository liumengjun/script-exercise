#!/usr/bin/python
# -*- coding:utf-8 -*-
# coding=utf-8
#
# loan calculator

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
    return fixup and _fix_float(a) or a


def _fix_float(amount, n=2):
    '''
    保留n位小数，第(n+1)位小数向上取整
    '''
    import math
    nnn = 10**n
    return math.ceil(amount * nnn) / nnn


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


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Please input 4 params: ACPI|AC total month_count month_rate")
        exit(-1)

    l_type = sys.argv[1].upper()
    total = float(sys.argv[2])
    m_count = int(sys.argv[3])
    m_rate = float(sys.argv[4])

    import pprint as pp

    if l_type == 'ACPI':
        pp.pprint(calc_acpi_details(total, m_count, m_rate))
    else:
        pp.pprint(calc_ac_details(total, m_count, m_rate))
