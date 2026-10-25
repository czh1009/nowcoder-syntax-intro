# -*- coding: utf-8 -*-
"""
NC13585 安卓图案解锁
题目链接: https://ac.nowcoder.com/acm/problem/13585
分类: 模拟、枚举与贪心

【思路】安卓九宫格（1 2 3 / 4 5 6 / 7 8 9）图案合法性判定，多组输入：
  1. 数字必须在 1~9 内且不能重复出现；
  2. 若相邻两次选择连线"跨过"了某个中间点（如 1->3 跨 2，1->9 跨 5），
     该中间点必须已经被使用过。
跳跃关系共 8 对（双向）：(1,3)->2, (1,7)->4, (1,9)->5, (2,8)->5,
(3,7)->5, (3,9)->6, (4,6)->5, (7,9)->8。
"""

JUMP = {}
for a, b, mid in ((1, 3, 2), (1, 7, 4), (1, 9, 5), (2, 8, 5),
                  (3, 7, 5), (3, 9, 6), (4, 6, 5), (7, 9, 8)):
    JUMP[(a, b)] = mid
    JUMP[(b, a)] = mid


def check(pattern):
    used = set()
    prev = None
    for ch in pattern:
        d = int(ch)
        if d in used:  # 数字重复
            return False
        if prev is not None:
            mid = JUMP.get((prev, d))
            if mid is not None and mid not in used:  # 跨点未被使用
                return False
        used.add(d)
        prev = d
    return True


def main():
    import sys
    for line in sys.stdin:
        pattern = line.strip()
        if not pattern:
            continue
        print("YES" if check(pattern) else "NO")


if __name__ == "__main__":
    main()
