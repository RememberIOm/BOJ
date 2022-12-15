import sys

input = sys.stdin.readline

n, k = map(int, input().split())
weight_value = [list(map(int, input().split())) for _ in range(n)]

weight_value.sort()

bag = [0] * (k + 1)

for w, v in weight_value:
    for bag_i in range(k, w - 1, -1):
        bag[bag_i] = max(bag[bag_i], bag[bag_i - w] + v)

print(bag[-1])
