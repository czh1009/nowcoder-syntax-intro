# -*- coding: utf-8 -*-
"""
NC13814 Captcha Cracker
题目链接: https://ac.nowcoder.com/acm/problem/13814
分类: 模拟、枚举与贪心

【思路】验证码网站为 02469.com，只需识别数字 0、2、4、6、9：
  0 - zero, 2 - two, 4 - four, 6 - six, 9 - nine。
从左到右扫描字符串：遇到数字 0/2/4/6/9 直接记录；
遇到这五个英文单词的起始字母则匹配整个单词并记录对应数字；
这五个单词首字母互不相同（z/t/f/s/n），不会产生歧义，按出现顺序输出即可。
"""


WORD_TO_DIGIT = (("zero", "0"), ("two", "2"), ("four", "4"),
                 ("six", "6"), ("nine", "9"))


def recognize(s):
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            if ch in "02469":
                result.append(ch)
            i += 1
        else:
            for word, digit in WORD_TO_DIGIT:
                if s.startswith(word, i):
                    result.append(digit)
                    i += len(word)
                    break
            else:
                i += 1
    return "".join(result)


def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    out_lines = [recognize(data[k]) for k in range(1, t + 1)]
    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
