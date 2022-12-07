import sys

input = sys.stdin.readline


def input_func():
    return int(input())


def calc_fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    if n in memo_fibo:
        return memo_fibo[n]

    ans = 0
    if n % 2 == 0:
        ans = (calc_fibo(n / 2 - 1) + calc_fibo(n / 2 + 1)) * calc_fibo(n / 2)
    else:
        ans = calc_fibo(n // 2 + 1) ** 2 + calc_fibo(n // 2) ** 2

    memo_fibo[n] = ans
    return ans % 1_000_000


memo_fibo = dict()
print(calc_fibo(input_func() % 1_500_000))  # 파사노 주기
