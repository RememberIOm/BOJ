import sys

input = sys.stdin.readline

n = int(input())
dp = [[[0] * (2 ** 10) for _ in range(10)] for _ in range(n)]
for i in range(1, 10):
    dp[0][i][1 << i] = 1

for digit in range(1, n):
    for i in range(10):
        for bit in range(2 ** 10):
            if i != 0:
                dp[digit][i][bit | 1 << i] += dp[digit - 1][i - 1][bit]

            if i != 9:
                dp[digit][i][bit | 1 << i] += dp[digit - 1][i + 1][bit]

ans = 0
for num in dp[-1]:
    ans += num[-1]
print(divmod(ans, 1_000_000_000)[1])
