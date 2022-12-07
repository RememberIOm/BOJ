import sys
import itertools

input = sys.stdin.readline

cost = [list(map(int, input().split())) for _ in range(12)]

cost_min = 0

for i in range(0, 12, 2):
    cost_min += cost[i][i + 1]

move_cost_min = sys.maxsize
for seqs in itertools.product(range(2), repeat=6):
    for group_seqs in itertools.permutations(range(6), 6):
        move_cost = 0
        for i in range(5):
            seq_cur, seq_next = seqs[i], seqs[i + 1]
            group_cur, group_next = group_seqs[i], group_seqs[i + 1]

            move_cost += cost[group_cur * 2 + (seq_cur == 0)][group_next * 2 + seq_next]

        move_cost_min = min(move_cost_min, move_cost)

print(cost_min + move_cost_min)
