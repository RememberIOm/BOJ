import sys
import itertools

input = sys.stdin.readline

n = int(input())
reduce_li = []

for digit in range(1, 11):
    for reduce in itertools.combinations(range(9, -1, -1), digit):
        reduce_li.append(int("".join(map(str, reduce))))

try:
    print(sorted(reduce_li)[n - 1])
except:
    print(-1)
