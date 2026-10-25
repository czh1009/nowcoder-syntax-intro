# -*- coding: utf-8 -*-
"""
NC13584 日历中的数字
题目链接: https://ac.nowcoder.com/acm/problem/13584
分类: 函数与递归

【思路】多组输入，每组给 y m x。
日期格式形如 2017-04-04：月份、日期不足两位补前导 0。
先按闰年规则求出 y 年 m 月的天数，再逐日拼出日期字符串统计数字 x 的出现次数。
"""


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    import sys
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 3:
            continue
        y, m, x = map(int, parts[:3])
        days = DAYS_IN_MONTH[m - 1] + (1 if m == 2 and is_leap(y) else 0)
        count = sum(
            f"{y}-{m:02d}-{d:02d}".count(str(x)) for d in range(1, days + 1)
        )
        print(count)


if __name__ == "__main__":
    main()
