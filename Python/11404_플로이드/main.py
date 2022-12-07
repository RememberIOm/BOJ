import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = tuple(map(int, input().split()) for _ in range(m))

dist = [[sys.maxsize if i != j else 0 for j in range(n)] for i in range(n)]

for start, end, cost in bus:
    start, end = start - 1, end - 1

    dist[start][end] = min(dist[start][end], cost)

for mid in range(n):
    for start in range(n):
        for end in range(n):
            dist_cur = dist[start][mid] + dist[mid][end]

            dist[start][end] = min(dist[start][end], dist_cur)

print(
    "\n".join(
        " ".join([str(i) if i < sys.maxsize else "0" for i in dist_i])
        for dist_i in dist
    )
)
