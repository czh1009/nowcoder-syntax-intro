# -*- coding: utf-8 -*-
"""
NC22227 约瑟夫环
题目链接: https://ac.nowcoder.com/acm/problem/22227
分类: 数组、字符串及数据批量存储

【思路】n 个人编号 0 ~ n-1 围成一圈，从编号 k 的人开始报 1，
报到 m 的人出队，下一个人从 1 重新报数，求最后剩下的人。
数据规模小（n <= 100），直接用列表模拟即可。
"""


def main():
    n, k, m = map(int, input().split())
    people = list(range(n))
    idx = k                     # 当前报数人的下标
    while len(people) > 1:
        idx = (idx + m - 1) % len(people)
        people.pop(idx)         # 报到 m 的人出队，idx 自然指向下一个人
    print(people[0])


if __name__ == "__main__":
    main()
