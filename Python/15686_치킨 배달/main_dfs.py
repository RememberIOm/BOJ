import sys

input = sys.stdin.readline


def chicken(d_li):
    ans = 0
    for d in d_li:
        ans += min(d)

    return ans


def hq_sel(sel_li, d_li, depth, depth_max):
    if depth < depth_max:
        for i in range(sel_li[-1] + 1, len(d_li[0])):
            sel_li_next = sel_li[:]
            sel_li_next.append(i)
            hq_sel(sel_li_next, d_li, depth + 1, depth_max)
    else:
        d_li_remove = [[] for _ in range(len(d_li))]
        for home in range(len(d_li)):
            for hq in sel_li[1:]:
                d_li_remove[home].append(d_li[home][hq])

        global g_chicken_min
        g_chicken_min = min(g_chicken_min, chicken(d_li_remove))


# main
n, m = map(int, input().split())
hq_li, home_li = [], []
hq_num = home_num = 0

for y in range(n):
    line_li = list(map(int, input().split()))
    for x in enumerate(line_li):
        if x[1] == 2:
            hq_li.append([x[0], y])
            hq_num += 1
        elif x[1] == 1:
            home_li.append([x[0], y])
            home_num += 1

d_li = [[] for _ in range(home_num)]
for i in range(home_num):
    for hq in hq_li:
        d_li[i].append(abs(home_li[i][0] - hq[0]) + abs(home_li[i][1] - hq[1]))

g_chicken_min = sys.maxsize

hq_sel([-1], d_li, 0, m)

print(g_chicken_min)
