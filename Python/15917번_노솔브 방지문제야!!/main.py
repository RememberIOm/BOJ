import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = int(input())

    if a & (a - 1):
        print(0)
    else:
        print(1)
