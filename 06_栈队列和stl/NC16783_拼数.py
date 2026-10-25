# -*- coding: utf-8 -*-
"""
NC16783 拼数
题目链接: https://ac.nowcoder.com/acm/problem/16783
分类: 栈、队列和 STL

【思路】把 n 个正整数拼成最大的多位整数。
将数字当作字符串，自定义比较：若 x+y > y+x 则 x 排在前面，
按此规则从大到小排序后依次拼接即为答案。
"""


def main():
    import sys
    from functools import cmp_to_key

    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    nums = input_data[1:1 + n]

    def compare(x, y):
        if x + y > y + x:
            return -1  # x 放前面
        if x + y < y + x:
            return 1
        return 0

    nums.sort(key=cmp_to_key(compare))
    print("".join(nums))


if __name__ == "__main__":
    main()
