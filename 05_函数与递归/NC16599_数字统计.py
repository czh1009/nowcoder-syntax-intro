# -*- coding: utf-8 -*-
"""
NC16599 数字统计
题目链接: https://ac.nowcoder.com/acm/problem/16599
分类: 函数与递归

【思路】统计数字 2 在 [L, R] 所有整数的十进制表示中出现的总次数。
用前缀和思想：f(R) - f(L-1)。f(n) 按"数位位置"统计，
每个位把 n 拆成 high | cur | low 三段，用经典闭式公式计数。
"""


def count_digit(n, d):
    """数字 d 在 1..n 的十进制表示中出现的总次数。"""
    total = 0
    p = 1  # 当前处理的位：1=个位, 10=十位, ...
    while p <= n:
        high = n // (p * 10)
        cur = (n // p) % 10
        low = n % p
        if d == 0:
            if high > 0:
                if cur > 0:
                    total += high * p
                else:
                    total += (high - 1) * p + low + 1
        else:
            if cur > d:
                total += (high + 1) * p
            elif cur == d:
                total += high * p + low + 1
            else:
                total += high * p
        p *= 10
    return total


def main():
    left, right = map(int, input().split())
    print(count_digit(right, 2) - count_digit(left - 1, 2))


if __name__ == "__main__":
    main()
