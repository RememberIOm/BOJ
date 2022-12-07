import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [input().split() for _ in range(n)]

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
KABE, BEFORE, AFTER = "1", "0", "-1"
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

after_cnt = 0
turn_cnt = 0
while True:
    if room[r][c] == BEFORE:
        room[r][c] = AFTER
        after_cnt += 1

    d = (d - 1) % 4
    turn_cnt += 1

    dr, dc = r + direction[d][0], c + direction[d][1]
    if room[dr][dc] == BEFORE:
        r, c = dr, dc
        turn_cnt = 0
        continue
    else:
        if turn_cnt == 4:
            dr, dc = r - direction[d][0], c - direction[d][1]

            if room[dr][dc] == KABE:
                break
            else:
                r, c = dr, dc
                turn_cnt = 0

print(after_cnt)
