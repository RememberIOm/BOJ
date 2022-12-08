import sys

input = sys.stdin.readline

n = int(input())

cnt = 0

for a in range(1, 500):
    if int((a * a + n) ** 0.5) == (a * a + n) ** 0.5:
        cnt += 1

print(cnt)
