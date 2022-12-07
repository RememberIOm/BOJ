import sys

input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

front, end = lines[0]
ans = 0

for i in range(n - 1):
    if end >= lines[i + 1][0]:
        if end < lines[i + 1][1]:
            end = lines[i + 1][1]
    else:
        ans += end - front
        front, end = lines[i + 1]

ans += end - front

print(ans)
