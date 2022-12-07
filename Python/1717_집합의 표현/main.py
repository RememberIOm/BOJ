import sys

input = sys.stdin.readline

sys.setrecursionlimit(2 ** 31 - 1)


def find(n):
    if n == my_set[n]:
        return n
    else:
        my_set[n] = find(my_set[n])
        return my_set[n]


n, m = map(int, input().split())

my_set = list(range(n + 1))

for _ in range(m):
    cmd, a, b = map(int, input().split())

    a_set, b_set = find(a), find(b)

    if cmd == 0:
        if a_set < b_set:
            my_set[b_set] = a_set
        else:
            my_set[a_set] = b_set
    else:
        if a_set == b_set:
            print("YES")
        else:
            print("NO")
