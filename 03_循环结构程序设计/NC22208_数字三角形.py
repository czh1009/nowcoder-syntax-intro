# -*- coding: utf-8 -*-
"""
NC22208 数字三角形
题目链接: https://ac.nowcoder.com/acm/problem/22208
分类: 循环结构程序设计

【思路】从 1 开始连续编号，第 i 行输出 i 个数，
每个数按宽度 4 右对齐（相当于 C 语言的 %4d），行内直接拼接。
"""


def main():
    n = int(input())
    num = 1
    for i in range(1, n + 1):
        row = "".join(f"{x:4d}" for x in range(num, num + i))
        print(row)
        num += i


if __name__ == "__main__":
    main()
