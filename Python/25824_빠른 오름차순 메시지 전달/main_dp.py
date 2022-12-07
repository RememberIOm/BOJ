import sys

input = sys.stdin.readline

cost = [[0] * 14 for _ in range(2)]
cost += [[0] * 2 + list(map(int, input().split())) for _ in range(12)]

cost_min = 0
dp_for, dp_back = [0] * 7, [0] * 7

for group_i in range(1, 7):
    prev_0, prev_1 = group_i * 2 - 2, group_i * 2 - 1
    cur_0, cur_1 = group_i * 2, group_i * 2 + 1

    cost_min += cost[cur_0][cur_1]

    dp_for[group_i] = min(
        dp_for[group_i - 1] + cost[prev_1][cur_0],
        dp_back[group_i - 1] + cost[prev_0][cur_0],
    )
    dp_back[group_i] = min(
        dp_for[group_i - 1] + cost[prev_1][cur_1],
        dp_back[group_i - 1] + cost[prev_0][cur_1],
    )

cost_min += min(dp_for[-1], dp_back[-1])

print(cost_min)
