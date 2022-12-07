import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 ** 31 - 1)


def pre(in_start, in_end, post_start, post_end):
    if in_start >= in_end or post_start >= post_end:
        return

    root = post_trv[post_end - 1]
    root_idx = in_trv_idx[root]

    pre_left = root_idx - in_start

    print(root, end=" ")
    pre(in_start, root_idx, post_start, post_start + pre_left)
    pre(root_idx + 1, in_end, post_start + pre_left, post_end - 1)


n = int(input())
in_trv = list(map(int, input().split()))
post_trv = list(map(int, input().split()))
in_trv_idx = [0] * (n + 1)
for i in enumerate(in_trv):
    in_trv_idx[i[1]] = i[0]

pre(0, n, 0, n)
