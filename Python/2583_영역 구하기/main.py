import sys

input = sys.stdin.readline


def bfs(x, y):
    blank_num = 1

    tasks = set([(x, y)])

    while tasks:
        x_cur, y_cur = tasks.pop()

        adder = ((0, -1), (1, 0), (0, 1), (-1, 0))

        for dx, dy in adder:
            x_next, y_next = x_cur + dx, y_cur + dy

            if 0 <= x_next < n and 0 <= y_next < m:
                if board[y_next][x_next] == 0:
                    board[y_next][x_next] = 2
                    blank_num += 1
                    tasks.add((x_next, y_next))

    return blank_num


m, n, k = map(int, input().split())
squares = [map(int, input().split()) for _ in range(k)]

board = [[0] * n for _ in range(m)]

for x1, y1, x2, y2 in squares:
    for dy in range(y1, y2):
        for dx in range(x1, x2):
            board[dy][dx] = 1

blanks = []

for yi in range(m):
    for xi in range(n):
        if board[yi][xi] == 0:
            board[yi][xi] = 2
            blanks.append(bfs(xi, yi))

blanks.sort()

print(len(blanks))
print(*blanks)
