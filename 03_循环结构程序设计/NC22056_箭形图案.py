# -*- coding: utf-8 -*-
"""
NC22056 箭形图案
题目链接: https://ac.nowcoder.com/acm/problem/22056
分类: 循环结构程序设计

【思路】多组输入。每组 n 输出 2n+1 行的箭形：
前 n+1 行第 i 行 (1 <= i <= n+1) 为 2*(n+1-i) 个空格 + i 个星号，
后 n 行按 i 从 n 到 1 重复同样的规则。
样例 n=2: "    *" / "  **" / "***" / "  **" / "    *"。
"""


def print_arrow(n):
    for i in range(1, n + 2):
        print(" " * 2 * (n + 1 - i) + "*" * i)
    for i in range(n, 0, -1):
        print(" " * 2 * (n + 1 - i) + "*" * i)


def main():
    import sys
    for n in map(int, sys.stdin.read().split()):
        print_arrow(n)


if __name__ == "__main__":
    main()
