# -*- coding: utf-8 -*-
"""
NC15431 比较月亮大小
题目链接: https://ac.nowcoder.com/acm/problem/15431
分类: 数组、字符串及数据批量存储

【思路】月亮大小以 30 天为周期循环：0,1,...,15,14,...,1。
给定 n 条连续记录，判断"下一天比最后一天大还是小"：
枚举这 n 条记录在 30 天周期中的全部可能起点，
若所有合法起点推出的结论唯一则输出 UP / DOWN，否则（含记录矛盾）输出 -1。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    records = list(map(int, data[1:1 + n]))
    cycle = list(range(16)) + list(range(14, 0, -1))  # 长度 30

    outcomes = set()
    for start in range(30):
        if all(cycle[(start + i) % 30] == records[i] for i in range(n)):
            next_day = cycle[(start + n) % 30]
            last_day = cycle[(start + n - 1) % 30]
            outcomes.add("UP" if next_day > last_day else "DOWN")

    print(outcomes.pop() if len(outcomes) == 1 else -1)


if __name__ == "__main__":
    main()
