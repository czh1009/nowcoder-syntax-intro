# -*- coding: utf-8 -*-
"""
NC15756 233
题目链接: https://ac.nowcoder.com/acm/problem/15756
分类: 函数与递归

【思路】每组给出两个形如 2333...3 的"233 串"（最长 50 位），
直接利用 Python 任意精度整数相乘后输出。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out_lines = []
    for _ in range(t):
        a, b = int(data[pos]), int(data[pos + 1])
        pos += 2
        out_lines.append(str(a * b))
    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
