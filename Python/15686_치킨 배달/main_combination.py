import sys
import itertools

input = sys.stdin.readline


def chicken(d_li):
    ans = 0
    for d in d_li:
        ans += min(d)

    return ans


n, m = map(int, input().split())
hq_li, home_li = [], []

for y in range(n):
    line_li = list(map(int, input().split()))
    for x in enumerate(line_li):
        if x[1] == 2:
            hq_li.append([x[0], y])
        elif x[1] == 1:
            home_li.append([x[0], y])

chicken_min = sys.maxsize
for hq_sel_li in itertools.combinations(hq_li, m):
    d_li = [[] for _ in range(len(home_li))]
    for i in range(len(home_li)):
        for hq in hq_sel_li:
            d_li[i].append(abs(home_li[i][0] - hq[0]) + abs(home_li[i][1] - hq[1]))
    chicken_min = min(chicken_min, chicken(d_li))

print(chicken_min)
