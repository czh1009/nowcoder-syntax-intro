# -*- coding: utf-8 -*-
"""
NC200369 四舍五入
题目链接: https://ac.nowcoder.com/acm/problem/200369
分类: 模拟、枚举与贪心

【思路】最多 t 次四舍五入，求可得到的最大值，输出不得带尾零（10.30 视为错误）。
贪心：每一轮在"小数部分最左边一个 >= 5 的数字"处做进位式四舍五入
（进位后截掉其后的所有小数位）。由于该位置左边的数字全部 < 5，进位不会连锁进位；
每轮严格使数值增大。若小数部分已无 >= 5 的数字，继续操作只会变小或不变，直接停止。
样例验证：10.245 -> 10.25（1 次）-> 10.3（2 次）。
"""


def main():
    import sys
    data = sys.stdin.read().split()
    # n = 数字符串长度（含小数点），本题代码中无需显式使用
    _, t = int(data[0]), int(data[1])
    s = data[2]

    if "." in s:
        int_part, frac = s.split(".")
    else:
        int_part, frac = s, ""
    frac = list(frac)

    search_from = 0  # 该下标之前的小数位都已确认 < 5
    for _ in range(t):
        i = search_from
        while i < len(frac) and int(frac[i]) < 5:
            i += 1
        if i >= len(frac):
            break  # 小数部分没有 >= 5 的数字，无法再变大
        if i == 0:
            # 四舍五入到整数：整数部分进一，小数部分清空
            int_part = str(int(int_part) + 1)
            frac = []
            search_from = 0
        else:
            # 保留 i-1 位小数并在末位进一（左边全 < 5，不会连锁进位）
            frac = frac[:i - 1] + [str(int(frac[i - 1]) + 1)]
            search_from = i - 1

    frac_str = "".join(frac).rstrip("0")
    print(int_part + ("." + frac_str if frac_str else ""))


if __name__ == "__main__":
    main()
