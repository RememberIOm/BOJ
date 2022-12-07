import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

lcs_dp = tuple([0] * (len(a) + 1) for _ in range(len(b) + 1))

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j - 1] == b[i - 1]:
            lcs_dp[i][j] = lcs_dp[i - 1][j - 1] + 1
        else:
            lcs_dp[i][j] = max(lcs_dp[i - 1][j], lcs_dp[i][j - 1])

print(lcs_dp[-1][-1])
