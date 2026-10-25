# -*- coding: utf-8 -*-
"""
NC212955 比大小
题目链接: https://ac.nowcoder.com/acm/problem/212955
分类: 选择结构程序设计

【思路】读入两个整数 a、b，按 a<b、a=b、a>b 分别输出 "<"、"="、">"。
"""


def main():
    a, b = map(int, input().split())
    if a < b:
        print("<")
    elif a == b:
        print("=")
    else:
        print(">")


if __name__ == "__main__":
    main()
