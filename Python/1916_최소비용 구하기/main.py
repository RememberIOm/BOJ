import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = int(input()), int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())

    graph[s].append((e, w))

start, end = map(int, input().split())

d = [sys.maxsize] * (n + 1)
d[start] = 0

task = [(0, start)]
while task:
    d_cur, city_cur = heappop(task)

    if city_cur == end:
        break

    if d_cur > d[city_cur]:
        continue

    for city_next, w in graph[city_cur]:
        if d[city_next] > d[city_cur] + w:
            d[city_next] = d[city_cur] + w
            heappush(task, (d[city_next], city_next))

print(d[end])
