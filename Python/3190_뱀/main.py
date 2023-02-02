import sys
import collections

input = sys.stdin.readline

n = int(input())
k = int(input())
apples = set([tuple(map(int, input().split()[::-1])) for _ in range(k)])

l = int(input())
moves = dict()
for x, c in [input().split() for _ in range(l)]:
    moves[int(x)] = c

snake = collections.deque([(int(1), int(1))])
snake_set = set(snake)

time = 0
d_loc = ((0, -1), (1, 0), (0, 1), (-1, 0))
d = 1

while True:
    time += 1

    cur_head = snake[-1]
    next_head = (cur_head[0] + d_loc[d][0], cur_head[1] + d_loc[d][1])

    if not (1 <= next_head[0] <= n and 1 <= next_head[1] <= n):
        break
    if next_head in snake_set:
        break

    snake.append(next_head)
    snake_set.add(next_head)

    if next_head in apples:
        apples.remove(next_head)
    else:
        snake_set.remove(snake.popleft())

    if time in moves:
        if moves[time] == "L":
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

print(time)
