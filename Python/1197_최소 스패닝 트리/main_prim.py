import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
e_li = [[] for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())

    e_li[a - 1].append((c, b - 1))
    e_li[b - 1].append((c, a - 1))

visit = set(range(1, v))

edges_heap = []
for i in e_li[0]:
    heapq.heappush(edges_heap, i)

edge_sum = 0

while visit:
    edge, v_next = heapq.heappop(edges_heap)
    while v_next not in visit:
        edge, v_next = heapq.heappop(edges_heap)

    edge_sum += edge
    visit -= set([v_next])
    for i in e_li[v_next]:
        heapq.heappush(edges_heap, i)

print(edge_sum)
