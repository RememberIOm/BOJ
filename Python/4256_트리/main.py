import sys
import collections

input = sys.stdin.readline


def post_ord(tree):
    if not tree:
        return

    parent = pre_ord.popleft()
    left_tree = tree[: tree.index(parent)]
    right_tree = tree[tree.index(parent) + 1 :]

    post_ord(left_tree)
    post_ord(right_tree)
    print(parent, end=" ")


t = int(input())

for _ in range(t):
    n = int(input())
    pre_ord, in_ord = tuple(tuple(map(int, input().split())) for _ in range(2))
    pre_ord = collections.deque(pre_ord)

    post_ord(in_ord)
    print()
