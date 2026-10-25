# -*- coding: utf-8 -*-
"""
NC214218 涂小天与他的画
题目链接: https://ac.nowcoder.com/acm/problem/214218
分类: 循环结构程序设计

【思路】T 组数据，每组输入奇数 n，输出高度为 n 的菱形：
第 i 行 (1 <= i <= n) 星号数 s = 2*min(i, n+1-i) - 1，
前导空格数 = (n - s) / 2，行末不留空格。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    out_lines = []
    for k in range(1, t + 1):
        n = int(data[k])
        for i in range(1, n + 1):
            stars = 2 * min(i, n + 1 - i) - 1
            out_lines.append(" " * ((n - stars) // 2) + "*" * stars)
    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
