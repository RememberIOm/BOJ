import sys

input = sys.stdin.readline


def checking(chess, cur):
    for i in range(len(chess)):
        # y좌표 체킹
        if cur in chess:
            return False

        # 대각선 체킹
        if abs(i - len(chess)) == abs(chess[i] - cur):
            return False

    return True


def dfs(chess):
    global n, result

    if len(chess) == n:
        result += 1
        return

    for i in range(n):
        if checking(chess, i):
            dfs(chess + [i])


n = int(input())

result = 0

for i in range(n // 2):
    dfs([i])

result *= 2

if n % 2:
    dfs([n // 2])

print(result)
