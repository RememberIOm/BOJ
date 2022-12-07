import sys

input = sys.stdin.readline

r, c = map(int, input().split())
abc_map = tuple(tuple(input().rstrip()) for _ in range(r))

add_li = ((-1, 0), (0, 1), (1, 0), (0, -1))
len_max = 0
bfs_q = set([(0, 0, 0, 1)])

while bfs_q:
    x, y, visit, len = bfs_q.pop()

    len_max = max(len, len_max)
    if len_max == 26:
        break

    visit |= 1 << ord(abc_map[y][x]) - ord("A")

    for add in add_li:
        x_add, y_add = x + add[0], y + add[1]
        if (
            0 <= x_add < c
            and 0 <= y_add < r
            and not (1 << ord(abc_map[y_add][x_add]) - ord("A")) & visit
        ):
            bfs_q.add((x_add, y_add, visit, len + 1))

print(len_max)
