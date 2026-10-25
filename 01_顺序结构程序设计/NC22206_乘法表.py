# -*- coding: utf-8 -*-
"""
NC22206 乘法表
题目链接: https://ac.nowcoder.com/acm/problem/22206
分类: 顺序结构程序设计

【思路】输出九九乘法表。第 i 行依次输出 j*i (j = 1..i)，
每个式子形如 "j*i=xx"，其中乘积用宽度为 2 的右对齐格式（相当于 C 语言的 %2d）。
"""


def main():
    for i in range(1, 10):
        row = " ".join(f"{j}*{i}={j * i:2d}" for j in range(1, i + 1))
        print(row)


if __name__ == "__main__":
    main()
