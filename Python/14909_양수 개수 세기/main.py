import sys

input = sys.stdin.readline

arr = map(int, input().split())

cnt = 0

for arr_i in arr:
    if arr_i > 0:
        cnt += 1

print(cnt)
