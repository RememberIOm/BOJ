import sys
import heapq

input = sys.stdin.readline


v, e = map(int, input().split())
k = int(input())
vertex = [[] for _ in range(v + 1)]
for _ in range(e):
    u_cur, v_cur, w_cur = map(int, input().split())

    vertex[u_cur].append((v_cur, w_cur))


d = [sys.maxsize] * (v + 1)
d[k] = 0

search = [(0, k)]

while search:
    s_node_w, s_node = heapq.heappop(search)

    if s_node_w > d[s_node]:
        continue

    for e_node, e_node_w in vertex[s_node]:
        if d[e_node] > d[s_node] + e_node_w:
            d[e_node] = d[s_node] + e_node_w
            heapq.heappush(search, (d[e_node], e_node))


for i in range(1, v + 1):
    if d[i] == sys.maxsize:
        print("INF")
    else:
        print(d[i])
