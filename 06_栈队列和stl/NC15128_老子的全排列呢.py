# -*- coding: utf-8 -*-
"""
NC15128 老子的全排列呢
题目链接: https://ac.nowcoder.com/acm/problem/15128
分类: 栈、队列和 STL

【思路】输出 1~8 的全排列，共 8! = 40320 行。
itertools.permutations 按字典序生成，与"按照全排列的顺序输出"一致；
每行数字用单个空格分隔，行末无空格。
"""

from itertools import permutations


def main():
    lines = [" ".join(map(str, perm)) for perm in permutations(range(1, 9))]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
