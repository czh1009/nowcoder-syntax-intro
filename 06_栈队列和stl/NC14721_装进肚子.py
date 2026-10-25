# -*- coding: utf-8 -*-
"""
NC14721 装进肚子
题目链接: https://ac.nowcoder.com/acm/problem/14721
分类: 栈、队列和 STL

【思路】每个巧克力 i 在早上吃得到 A[i]，晚上吃得到 B[i]，恰好 K 个早上吃。
先假设全部晚上吃，总和为 sum(B)；
把"改到早上吃"的收益 A[i] - B[i] 从大到小排序，取前 K 个改为早上吃即最优。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    b = list(map(int, data[2 + n:2 + 2 * n]))

    order = sorted(range(n), key=lambda i: a[i] - b[i], reverse=True)
    total = 0
    for rank, i in enumerate(order):
        total += a[i] if rank < k else b[i]
    print(total)


if __name__ == "__main__":
    main()
