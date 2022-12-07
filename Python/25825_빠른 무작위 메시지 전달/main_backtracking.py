import sys

input = sys.stdin.readline

time = [list(map(int, input().split())) for _ in range(12)]

time_min = sys.maxsize

task = set([(i, i, 0, 0) for i in range(12)])
while task:
    task_cur, task_prev, time_cur, visit = task.pop()

    # 최소시간 초과 -> 백트래킹
    if time_cur + time[task_prev][task_cur] >= time_min:
        continue
    else:
        time_cur += time[task_prev][task_cur]
        visit ^= 1 << task_cur

    # 모두 visit
    if visit == 2 ** 12 - 1:
        time_min = time_cur
        continue

    # 같은 그룹 내 학생 index
    task_next = task_cur
    if task_cur % 2 == 0:
        task_next += 1
    else:
        task_next -= 1

    if not visit & (1 << task_next):
        task.add((task_next, task_cur, time_cur, visit))
    else:
        for i in [i for i in range(12) if not visit & (1 << i)]:
            task.add((i, task_cur, time_cur, visit))

print(time_min)
