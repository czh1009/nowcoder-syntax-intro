# -*- coding: utf-8 -*-
"""
NC22204 上下金字塔
题目链接: https://ac.nowcoder.com/acm/problem/22204
分类: 循环结构程序设计

【思路】多组输入。每组 n 输出一个总高度为 2n-1 行的菱形金字塔：
第 i 行 (1 <= i <= 2n-1) 的星号数 s = 2*min(i, 2n-i) - 1，
前导空格数 = (2n-1-s) / 2。
"""


def print_diamond(n):
    width = 2 * n - 1
    for i in range(1, width + 1):
        stars = 2 * min(i, width + 1 - i) - 1
        print(" " * ((width - stars) // 2) + "*" * stars)


def main():
    import sys
    for n in map(int, sys.stdin.read().split()):
        print_diamond(n)


if __name__ == "__main__":
    main()
