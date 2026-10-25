# -*- coding: utf-8 -*-
"""
NC205898 卡拉兹函数
题目链接: https://ac.nowcoder.com/acm/problem/205898
分类: 选择结构程序设计

【思路】卡拉兹（Collatz）函数：
  n 为奇数时 f(n) = 3n + 1；n 为偶数时 f(n) = n / 2。
按奇偶性选择公式输出即可（样例验证：f(1)=4，f(2)=1）。
"""


def main():
    n = int(input())
    if n % 2 == 1:
        print(3 * n + 1)
    else:
        print(n // 2)


if __name__ == "__main__":
    main()
