#!/usr/bin/python
# -*- coding:utf-8 -*-
# coding=utf-8
#
# loan calculator

###################################
# 等额本息: (Average Capital Plus Interest)
# 等额本金: (Average Capital)
###################################


def calc_acpi_per_month(total_pri, months, month_rate):
    '''
    计算`等额本息`每月还款额

    total_pri: 贷款总额
    months: 月数
    month_rate: 月利率

    return 每月还款额
    '''
    com_rate = (1 + month_rate)**months
    a = total_pri * month_rate * com_rate / (com_rate - 1)
    return round(a, 2)


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
        interest = remaining * month_rate
        pri = per_month_amount - interest
        remaining -= pri
        remaining_shown = round(remaining, 2)
        # 防止显示-0.0或负数
        if remaining_shown <= 0:
            remaining_shown = 0.0
        details.append({
            'seq': (i + 1),
            'gross': per_month_amount,
            'principal': round(pri, 2),
            'interest': round(interest, 2),
            'remaining': remaining_shown,
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
    pri_per_month = round(total_pri / months, 2)
    details = []
    remaining = total_pri
    for i in range(months):
        interest = remaining * month_rate
        remaining -= pri_per_month
        remaining_shown = round(remaining, 2)
        # 防止显示-0.0或负数
        if remaining_shown <= 0:
            remaining_shown = 0.0
        details.append({
            'seq': (i + 1),
            'gross': round(pri_per_month + interest, 2),
            'principal': round(pri_per_month, 2),
            'interest': round(interest, 2),
            'remaining': remaining_shown,
        })
    return details
