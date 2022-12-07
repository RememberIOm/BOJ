import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
map_i = tuple(input().rstrip() for _ in range(n))

add = ((0, -1), (1, 0), (0, 1), (-1, 0))
map_min_true, map_min_false = [[sys.maxsize] * m for _ in range(n)], [
    [sys.maxsize] * m for _ in range(n)
]
map_min_true[0][0] = 1
bfs_q = collections.deque([(0, 0, 1, True)])

while bfs_q:
    x, y, length, is_kabedon = bfs_q.popleft()

    if x == m - 1 and y == n - 1:
        break

    length += 1

    for cur_add in add:
        x_add, y_add = x + cur_add[0], y + cur_add[1]
        if 0 <= x_add < m and 0 <= y_add < n:
            if map_i[y_add][x_add] == "0":
                if is_kabedon:
                    if length < map_min_true[y_add][x_add]:
                        map_min_true[y_add][x_add] = length
                        bfs_q.append((x_add, y_add, length, is_kabedon))
                else:
                    if length < map_min_false[y_add][x_add]:
                        map_min_false[y_add][x_add] = length
                        bfs_q.append((x_add, y_add, length, is_kabedon))
            else:
                if is_kabedon:
                    bfs_q.append((x_add, y_add, length, False))

ans = min(map_min_false[-1][-1], map_min_true[-1][-1])
if ans != sys.maxsize:
    print(ans)
else:
    print(-1)
