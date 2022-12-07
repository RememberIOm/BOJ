import sys

input = sys.stdin.readline


def dp(cur, visit):
    global n

    if visit == (1 << n) - 1:
        if costs[cur][0]:
            return costs[cur][0]
        else:
            return sys.maxsize

    if dp_li[cur][visit]:
        return dp_li[cur][visit]

    cost_min = sys.maxsize
    for i in range(1, n):
        if costs[cur][i] == 0 or visit & (1 << i):
            continue

        cost_min = min(cost_min, dp(i, visit | (1 << i)) + costs[cur][i])

    dp_li[cur][visit] = cost_min

    return cost_min


n = int(input())
costs = tuple(tuple(map(int, input().split())) for _ in range(n))
dp_li = [[0] * (1 << n) for _ in range(n)]

print(dp(0, 1))
