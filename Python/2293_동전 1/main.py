import sys

input = sys.stdin.readline

N, K = map(int, input().split())
COIN = [int(input()) for _ in range(N)]

cases = [1] + [0] * K

for coin_cur in COIN:
    for cases_idx in range(coin_cur, K + 1):
        cases[cases_idx] += cases[cases_idx - coin_cur]

print(cases[-1])
