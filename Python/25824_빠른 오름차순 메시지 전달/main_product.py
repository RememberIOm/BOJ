import sys
import itertools

input = sys.stdin.readline

cost = [list(map(int, input().split())) for _ in range(12)]

cost_min = 0

for i in range(0, 12, 2):
    cost_min += cost[i][i + 1]

move_cost_min = sys.maxsize
for seqs in itertools.product([0, 1], repeat=6):
    move_cost = 0
    for seqs_i in range(len(seqs) - 1):
        seq_cur = seqs[seqs_i]
        seq_next = seqs[seqs_i + 1]

        move_cost += cost[seqs_i * 2 + (seq_cur == 0)][(seqs_i + 1) * 2 + seq_next]

    move_cost_min = min(move_cost_min, move_cost)

print(cost_min + move_cost_min)
