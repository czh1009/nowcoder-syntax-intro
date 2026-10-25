# -*- coding: utf-8 -*-
"""
NC13588 从后台研发到跑路
题目链接: https://ac.nowcoder.com/acm/problem/13588
分类: 模拟、枚举与贪心

【思路】读入整个源码文本，删除 C 风格块注释，但字符串字面量里的内容原样保留：
  - 遇到 "/*"：向后找 "*/" 并整体删除（注释可跨行）；
    若找不到闭合的 "*/"，说明这不是完整注释，按原文输出（见样例末尾的 /*）。
  - 遇到双引号：进入字符串状态，直到遇到未转义的引号；
    反斜杠转义的字符（如 \"）原样保留，其中的 /* 不算注释。
除注释外所有字符（包括空格、换行）原样输出。
"""


def main():
    import sys
    src = sys.stdin.read()
    out = []
    i, n = 0, len(src)
    while i < n:
        if src.startswith("/*", i):
            end = src.find("*/", i + 2)
            if end == -1:  # 未闭合，不是完整注释，按原文输出
                out.append("/*")
                i += 2
            else:
                i = end + 2
        elif src[i] == '"':
            # 字符串字面量：整体原样输出
            out.append('"')
            i += 1
            while i < n:
                out.append(src[i])
                if src[i] == "\\" and i + 1 < n:  # 转义字符连着下一个字符一起保留
                    out.append(src[i + 1])
                    i += 2
                    continue
                if src[i] == '"':
                    i += 1
                    break
                i += 1
        else:
            out.append(src[i])
            i += 1
    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()
