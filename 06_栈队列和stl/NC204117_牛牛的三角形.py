# -*- coding: utf-8 -*-
"""
NC204117 牛牛的三角形
题目链接: https://ac.nowcoder.com/acm/problem/204117
分类: 栈、队列和 STL

【思路】从数组中选出 3 个（下标不同）能构成三角形的元素，输出任意一组。
将数组升序排序后，若存在可行三元组，则排序后必存在相邻三元组 a[i], a[i+1], a[i+2] 满足
a[i] + a[i+1] > a[i+2]（反证：若所有相邻三元组都不行，更大的跨度更不行）。
逐个检查相邻三元组即可。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    nums = sorted(map(int, data[1:1 + n]))
    for i in range(n - 2):
        if nums[i] + nums[i + 1] > nums[i + 2]:
            print(nums[i], nums[i + 1], nums[i + 2])
            return
    print("No solution")


if __name__ == "__main__":
    main()
