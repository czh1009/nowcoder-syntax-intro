# -*- coding: utf-8 -*-
"""
NC16649 校门外的树
题目链接: https://ac.nowcoder.com/acm/problem/16649
分类: 数组、字符串及数据批量存储

【思路】数轴 0..L 每个整数点一棵树，共 L+1 棵。
用布尔数组标记每个位置是否有树，逐个区间把 [a, b] 端点内的树移走，最后统计剩余数量。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    length, regions = int(data[0]), int(data[1])
    has_tree = [True] * (length + 1)
    pos = 2
    for _ in range(regions):
        a, b = int(data[pos]), int(data[pos + 1])
        pos += 2
        for i in range(a, b + 1):
            has_tree[i] = False
    print(sum(has_tree))


if __name__ == "__main__":
    main()
