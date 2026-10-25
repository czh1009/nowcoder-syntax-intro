# -*- coding: utf-8 -*-
"""
NC16538 记数问题
题目链接: https://ac.nowcoder.com/acm/problem/16538
分类: 数组、字符串及数据批量存储

【思路】统计数字 d 在 1..n 的所有整数中出现的总次数。
按"数位位置"统计：对每个位（个位、十位、...），把 n 拆成 high | cur | low 三段，
d 小于/等于/大于当前位数字时，该位上 d 的出现次数有经典闭式公式（注意 d=0 时最高位不能为 0）。
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
            if high > 0:  # 0 不能作为最高位，从第二位起才有意义
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
    n, d = map(int, input().split())
    print(count_digit(n, d))


if __name__ == "__main__":
    main()
