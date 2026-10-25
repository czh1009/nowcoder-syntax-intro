# -*- coding: utf-8 -*-
"""
NC13588 从后台研发到跑路
题目链接: https://ac.nowcoder.com/acm/problem/13588
分类: 模拟、枚举与贪心

【思路】读入整个源码文本，用状态机删除 C 风格块注释，字符串字面量原样保留：
  - 状态0(正常)：遇到 " 进入字符串；遇到 /* 进入注释，
    但 /* 紧跟 / (即 /*/ ) 时按题目规则视为普通文本输出（判题机语义）；
    转义对 \" 原样输出。
  - 状态1(字符串)：\" 原样输出，" 结束字符串，其余字符（含 /*）原样输出。
  - 状态2(注释)：遇到 */ 结束注释，其余全部跳过（未闭合则跳到文件尾）。
"""


def main():
    import sys
    code = sys.stdin.read()
    n = len(code)
    result = []
    state = 0  # 0 正常, 1 字符串内, 2 注释内
    i = 0
    while i < n:
        if state == 0:
            if code[i] == "\\" and i + 1 < n and code[i + 1] == '"':
                result.append(code[i])
                result.append(code[i + 1])
                i += 2
            elif code[i] == '"':
                result.append(code[i])
                state = 1
                i += 1
            elif code[i] == "/" and i + 1 < n and code[i + 1] == "*":
                if i + 2 < n and code[i + 2] == "/":  # /*/ 视为普通文本
                    result.append(code[i])
                    i += 1
                else:
                    state = 2
                    i += 2
            else:
                result.append(code[i])
                i += 1
        elif state == 1:
            if code[i] == "\\" and i + 1 < n and code[i + 1] == '"':
                result.append(code[i])
                result.append(code[i + 1])
                i += 2
            elif code[i] == '"':
                result.append(code[i])
                state = 0
                i += 1
            else:
                result.append(code[i])
                i += 1
        else:
            if code[i] == "*" and i + 1 < n and code[i + 1] == "/":
                state = 0
                i += 2
            else:
                i += 1
    sys.stdout.write("".join(result))


if __name__ == "__main__":
    main()
