# -*- coding: utf-8 -*-
"""
NC21874 好串
题目链接: https://ac.nowcoder.com/acm/problem/21874
分类: 栈、队列和 STL

【思路】好串定义为：从空串出发，每次在任意位置插入子串 "ab" 若干次得到的字符串。
这等价于"括号匹配"型字符串（a 视为左括号，b 视为右括号）：
  1. 任意前缀中 a 的数量 >= b 的数量；
  2. 整串中 a 的数量 == b 的数量。
用栈思想扫描一遍：遇到 a 加 1，遇到 b 减 1，中途出现负数或最终不为 0 则为 Bad。
样例验证：ab -> Good，aab -> Bad。
"""


def main():
    s = input().strip()
    balance = 0
    ok = True
    for ch in s:
        if ch == "a":
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                ok = False
                break
    print("Good" if ok and balance == 0 else "Bad")


if __name__ == "__main__":
    main()
