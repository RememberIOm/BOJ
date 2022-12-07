import sys

input = sys.stdin.readline

STD = 12
time = [list(map(int, input().split())) for _ in range(STD)]

time_min = sys.maxsize

task = [(1, 1, 0, 0), (0, 0, 0, 0)]
while task:
    task_cur, task_prev, time_cur, visit = task.pop()

    if time_cur + time[task_prev][task_cur] >= time_min:
        continue
    else:
        time_cur += time[task_prev][task_cur]
        visit ^= 1 << task_cur

    if visit == 2 ** 12 - 1:
        time_min = time_cur
        continue

    task_next = task_cur
    if task_cur % 2 == 0:
        task_next += 1
    else:
        task_next -= 1

    if visit & (1 << task_next):
        task.extend(
            [
                (task_cur + 2, task_cur, time_cur, visit),
                (task_next + 2, task_cur, time_cur, visit),
            ]
        )
    else:
        task.append((task_next, task_cur, time_cur, visit))

print(time_min)
