import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    result = -1

    for i in range(x, math.lcm(m, n) + 1, m):
        if i % n == y % n:
            result = i
            break

    print(result)
