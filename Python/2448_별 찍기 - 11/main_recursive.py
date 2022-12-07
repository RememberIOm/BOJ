import sys

input = sys.stdin.readline


def star(h, x, y):
    if h == 3:
        li[y][x] = "*"
        li[y + 1][x - 1 : x + 2] = list("* *")
        li[y + 2][x - 2 : x + 3] = list("*****")
        return

    star(h // 2, x, y)
    star(h // 2, x - h // 2, y + h // 2)
    star(h // 2, x + h // 2, y + h // 2)


n = int(input())
li = [[" "] * (n * 2 - 1) for _ in range(n)]

star(n, n - 1, 0)

for i in li:
    print(*i, sep="")
