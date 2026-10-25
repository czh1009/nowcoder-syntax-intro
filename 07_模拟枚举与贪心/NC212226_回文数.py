# -*- coding: utf-8 -*-
"""
NC212226 回文数
题目链接: https://ac.nowcoder.com/acm/problem/212226
分类: 模拟、枚举与贪心

【思路】给出数码 0~9 各自的出现次数，用"全部数码"拼成最小的回文数，无解输出 -1。
构造规则：
  1. 奇数个数的数码超过 1 个 -> 无解；
  2. 回文数不能有前导 0：左半部分除了全 0 之外必须存在非零数码，
     且第一个位置选最小的非零数码，其余数码从小到大排列（0 可以紧跟其后）；
  3. 若总数码只有 1 个，直接输出该数码（样例中的 "0"）。
左半 + （奇数数码的中间位） + 左半反转 即为答案。
样例验证：0 2 4 2 0 2 0 0 0 0 -> 1223553221；4 0 2 3 0 0 0 2 0 0 -> 20037373002。
"""


def main():
    cnt = list(map(int, input().split()))
    total = sum(cnt)
    odd_digits = [d for d in range(10) if cnt[d] % 2 == 1]

    if total == 0:
        print(0)
        return
    if len(odd_digits) > 1:
        print(-1)
        return

    mid = str(odd_digits[0]) if odd_digits else ""
    half = []
    for d in range(10):
        half.extend([str(d)] * (cnt[d] // 2))

    if not half:  # 只剩中间一个数码
        print(mid)
        return

    first = next((d for d in range(1, 10) if cnt[d] // 2 > 0), None)
    if first is None:  # 左半部分全是 0，回文数必然前导 0，无解
        print(-1)
        return

    rest = []
    for d in range(10):
        rest.extend([str(d)] * (cnt[d] // 2))
    rest.remove(str(first))

    left = str(first) + "".join(sorted(rest))
    print(left + mid + left[::-1])


if __name__ == "__main__":
    main()
