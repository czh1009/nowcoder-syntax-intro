# -*- coding: utf-8 -*-
"""
NC18929 排列式
题目链接: https://ac.nowcoder.com/acm/problem/18929
分类: 顺序结构程序设计

【思路】枚举所有 a * b = c，使得 a、b、c 的十进制数字合起来恰好是 1~9 各出现一次。
数字总个数为 9，乘积 c 只能是 4 位数，因此 (a, b) 的位数只可能是 (1, 4) 或 (2, 3)。
乘数交换视为同一式子，规定较小的乘数写在前面的格式 "c = a x b"；
先按乘积 c 从小到大排序，c 相同时按较小乘数 a 从小到大排序。
"""


def main():
    results = []
    for a in range(1, 100):                # 较小乘数 a 最多两位数
        for b in range(a + 1, 10000):      # 较大乘数 b 最多四位数
            c = a * b
            if c > 9999:                   # 乘积必须是 4 位数
                break
            digits = sorted(str(a) + str(b) + str(c))
            if "".join(digits) == "123456789":
                results.append((c, a, b))

    results.sort()                         # 先按乘积、再按较小乘数排序
    for c, a, b in results:
        print(f"{c} = {a} x {b}")


if __name__ == "__main__":
    main()
