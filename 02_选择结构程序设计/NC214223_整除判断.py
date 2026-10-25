# -*- coding: utf-8 -*-
"""
NC214223 整除判断
题目链接: https://ac.nowcoder.com/acm/problem/214223
分类: 选择结构程序设计

【思路】读入整数 m、n，若 m % n == 0 输出 "YES"，否则输出 "NO"。
"""


def main():
    m, n = map(int, input().split())
    print("YES" if m % n == 0 else "NO")


if __name__ == "__main__":
    main()
