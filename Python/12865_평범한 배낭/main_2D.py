import sys

input = sys.stdin.readline

n, k = map(int, input().split())
thing = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    for w in range(1, k + 1):
        if w - thing[i][0] >= 0:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - thing[i][0]] + thing[i][1])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[-1][-1])
