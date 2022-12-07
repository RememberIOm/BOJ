import sys
import math

input = sys.stdin.readline


def input_func():
    n, m = map(int, input().split())

    return n, m


def calc_fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    if n in memo_fibo:
        return memo_fibo[n]

    ans = 0
    if n % 2 == 0:
        ans = (calc_fibo(n // 2 - 1) + calc_fibo(n // 2 + 1)) * calc_fibo(n // 2)
    else:
        ans = calc_fibo(n // 2 + 1) ** 2 + calc_fibo(n // 2) ** 2

    memo_fibo[n] = ans % 1_000_000_007
    return ans % 1_000_000_007


def calc_fibo_gcd(n, m):
    return calc_fibo(math.gcd(n, m)) % 1_000_000_007


memo_fibo = dict()

print(calc_fibo_gcd(*input_func()))
