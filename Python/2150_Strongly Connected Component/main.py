import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(node):
    visit[node] = True

    for next_node in sorted(graph[node]):
        if not visit[next_node]:
            dfs(next_node)

    dfs_stk.append(node)


def scc(node, cnt):
    visit_r[node] = True
    scc_stk[cnt].append(node)

    for next_node in graph_r[node]:
        if not visit_r[next_node]:
            scc(next_node, cnt)


v, e = map(int, input().split())

graph, graph_r = [tuple([] for _ in range(v + 1)) for _ in range(2)]
for _ in range(e):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph_r[b].append(a)

visit, visit_r = [[False] * (v + 1) for _ in range(2)]

dfs_stk = []
while len(dfs_stk) < v:
    for i in range(1, v + 1):
        if not visit[i]:
            dfs(i)

scc_stk = []
scc_cnt = 0
while dfs_stk:
    cur = dfs_stk.pop()

    if not visit_r[cur]:
        scc_stk.append([])
        scc(cur, scc_cnt)
        scc_cnt += 1

for i in scc_stk:
    i.sort()
scc_stk.sort(key=lambda x: x[0])

print(len(scc_stk))
for i in scc_stk:
    print(*i, sep=" ", end=" -1\n")
