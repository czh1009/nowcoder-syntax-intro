# -*- coding: utf-8 -*-
"""
NC14703 素数回文
题目链接: https://ac.nowcoder.com/acm/problem/14703
分类: 函数与递归

【思路】把素数 t 拼成回文数：pal = t + reverse(t 去掉最高位)，
例如 13 -> 131，127 -> 12721。t < 1e9，回文数最多 17 位，
普通试除太慢，使用确定性的 Miller-Rabin 素性测试
（底数取 2,3,5,7,11,13,17,19,23,29,31,37，可正确判定 < 3.3e24 的整数）。
"""


def is_prime(n):
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small_primes:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def main():
    t = int(input())
    palindrome = int(str(t) + str(t)[-2::-1])
    print("prime" if is_prime(palindrome) else "noprime")


if __name__ == "__main__":
    main()
