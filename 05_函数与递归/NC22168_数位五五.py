# -*- coding: utf-8 -*-
"""
NC22168 数位五五
题目链接: https://ac.nowcoder.com/acm/problem/22168
分类: 函数与递归

【思路】求 [x, y] 中"数位之和是 5 的倍数"的数的个数。
用前缀和：f(y) - f(x-1)。f(n) 为数位 DP：
从高位到低位枚举第一个小于 n 对应位的数字，其后各位自由，
自由位的数字和 mod 5 均匀分布（每位 10 个数字，5 个余数各 2 个），
故剩余 rem 位时的方案数为 2 * 10^(rem-1)；rem = 0 时按余数是否为 0 判定。
前缀前导零不影响数位和，天然把所有不足位数的数也覆盖到。
"""


def count_upto(n):
    """[0, n] 中数位之和是 5 的倍数的数的个数。"""
    if n < 0:
        return 0
    s = str(n)
    length = len(s)
    tight_mod = 0  # 与 n 的前缀完全一致时的数位和 mod 5
    ans = 0
    for i, ch in enumerate(s):
        digit = int(ch)
        remaining = length - 1 - i
        for dd in range(digit):  # 在当前位取比 n 小的数字，其后各位自由
            need = (-(tight_mod + dd)) % 5
            if remaining == 0:
                ans += 1 if need == 0 else 0
            else:
                ans += 2 * 10 ** (remaining - 1)
        tight_mod = (tight_mod + digit) % 5
    if tight_mod == 0:  # n 本身
        ans += 1
    return ans


def main():
    x, y = map(int, input().split())
    print(count_upto(y) - count_upto(x - 1))


if __name__ == "__main__":
    main()
