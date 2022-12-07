import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums_sort = sorted(nums)

bfs_q = deque([[nums, 0]])
visit = set()
ans = -1
while bfs_q:
    num = bfs_q.popleft()

    if num[0] == nums_sort:
        ans = num[1]
        break

    for i in range(n - k + 1):
        num_next = num[0][:i] + num[0][i : i + k][::-1] + num[0][i + k :]
        if str(num_next) not in visit:
            bfs_q.append([num_next, num[1] + 1])
            visit.add(str(num_next))

print(ans)
