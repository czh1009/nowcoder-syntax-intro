# -*- coding: utf-8 -*-
"""
NC213397 C Simple math problem
题目链接: https://ac.nowcoder.com/acm/problem/213397
分类: 选择结构程序设计

【思路】给定正整数 X、Y：若 X 是 Y 的因数（即 Y % X == 0），Z = X + Y；否则 Z = Y - X。
数据可达 1e11，Python 整数无溢出问题。
"""


def main():
    x, y = map(int, input().split())
    if y % x == 0:
        print(x + y)
    else:
        print(y - x)


if __name__ == "__main__":
    main()
