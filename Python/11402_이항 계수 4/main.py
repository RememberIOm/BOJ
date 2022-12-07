import sys
import math

input = sys.stdin.readline

n, k, m = map(int, input().split())

ans = 1
while n:
    ans = ans * (math.comb(n % m, k % m) % m) % m

    n //= m
    k //= m

print(ans)
