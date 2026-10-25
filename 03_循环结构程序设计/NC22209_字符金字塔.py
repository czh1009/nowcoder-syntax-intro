# -*- coding: utf-8 -*-
"""
NC22209 字符金字塔
题目链接: https://ac.nowcoder.com/acm/problem/22209
分类: 循环结构程序设计

【思路】输入一个大写字母 c，设 k = c - 'A'，输出 k+1 行：
第 r 行 (0 <= r <= k) 为 (k-r) 个空格 + "A..A+r" 升序 + 降序回文部分。
样例：C -> "  A" / " ABA" / "ABCBA"。
"""


def main():
    c = input().strip()
    k = ord(c) - ord("A")
    for r in range(k + 1):
        ascend = "".join(chr(ord("A") + j) for j in range(r + 1))
        descend = ascend[-2::-1]  # 去掉最后一个字母后反转，r=0 时为空串
        print(" " * (k - r) + ascend + descend)


if __name__ == "__main__":
    main()
