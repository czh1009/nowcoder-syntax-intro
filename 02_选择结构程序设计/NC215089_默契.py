# -*- coding: utf-8 -*-
"""
NC215089 默契
题目链接: https://ac.nowcoder.com/acm/problem/215089
分类: 选择结构程序设计

【思路】读入两个整数 x、y：
  相等时输出 "Tacit！"（注意：此处是全角感叹号！），
  不相等时输出 "No Tacit!"（半角感叹号）。
两种输出与官方样例逐一对应，不可混用。
"""


def main():
    x, y = map(int, input().split())
    if x == y:
        print("Tacit！")
    else:
        print("No Tacit!")


if __name__ == "__main__":
    main()
