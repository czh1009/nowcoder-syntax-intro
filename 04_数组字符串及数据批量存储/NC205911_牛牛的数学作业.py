# -*- coding: utf-8 -*-
"""
NC205911 牛牛的数学作业
题目链接: https://ac.nowcoder.com/acm/problem/205911
分类: 数组、字符串及数据批量存储
备注: 该题在牛客题库中的现题面即"牛牛的数学作业"（极差 + 方差）。

【思路】每组数据读入 m 个数，输出：
  极差 = max - min（整数）；
  方差 = sum((x - mean)^2) / m（总体方差，样例验证除以 m 而非 m-1）。
为避免浮点误差，方差用整数公式 sum(x^2)*m - (sum x)^2 后再除以 m^2，保留 3 位小数。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out_lines = []
    for _ in range(t):
        m = int(data[pos])
        pos += 1
        nums = list(map(int, data[pos:pos + m]))
        pos += m
        range_value = max(nums) - min(nums)
        total = sum(nums)
        sum_sq = sum(x * x for x in nums)
        variance = (m * sum_sq - total * total) / (m * m)
        out_lines.append(f"{range_value} {variance:.3f}")
    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
