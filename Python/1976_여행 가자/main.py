import sys

input = sys.stdin.readline

sys.setrecursionlimit(2 ** 31 - 1)


def find(city):
    if parents[city] == city:
        return city
    else:
        parents[city] = find(parents[city])
        return parents[city]


def union(a, b):
    a_p, b_p = find(a), find(b)

    if a_p != b_p:
        parents[b_p] = a_p


n = int(input())
m = int(input())
networks = [tuple(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))

parents = list(range(n))

for i in range(n):
    for j in range(i, n):
        if networks[i][j]:
            union(i, j)

is_connect = True
for i in range(m - 1):
    if find(plans[i] - 1) != find(plans[i + 1] - 1):
        is_connect = False
        break

if is_connect:
    print("YES")
else:
    print("NO")
