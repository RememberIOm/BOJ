import sys

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [tuple(map(int, input().split())) for _ in range(n)]

tetrominos = [
    # I
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    # O
    ((0, 0), (0, 1), (1, 0), (1, 1)),
    # L
    ((0, 0), (1, 0), (2, 0), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 0)),
    ((0, 0), (0, 1), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (-1, 2)),
    # J
    ((0, 0), (1, 0), (2, 0), (2, -1)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (0, 1), (1, 0), (2, 0)),
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    # S
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (-1, 1), (-1, 2)),
    # Z
    ((0, 0), (1, 0), (1, -1), (2, -1)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    # T
    ((0, 0), (0, 1), (0, 2), (1, 1)),
    ((0, 0), (1, 0), (2, 0), (1, -1)),
    ((0, 0), (0, 1), (0, 2), (-1, 1)),
    ((0, 0), (1, 0), (2, 0), (1, 1)),
]

sum_max = 0
for y in range(n):
    for x in range(m):
        for tetromino in tetrominos:
            is_inbound = True
            for dy, dx in tetromino:
                if 0 <= y + dy < n and 0 <= x + dx < m:
                    pass
                else:
                    is_inbound = False

            if not is_inbound:
                continue

            sum_cur = 0
            for dy, dx in tetromino:
                sum_cur += paper[y + dy][x + dx]

            sum_max = max(sum_max, sum_cur)

print(sum_max)
