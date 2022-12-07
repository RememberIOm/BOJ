import sys

input = sys.stdin.readline

sys.setrecursionlimit(2 ** 31 - 1)


def find(name):
    if parents[name] == name:
        return name
    else:
        parents[name] = find(parents[name])
        return parents[name]


def union(name1, name2):
    name1_p, name2_p = find(name1), find(name2)

    if name1_p != name2_p:
        parents[name2_p] = name1_p
        friends[name1_p] += friends[name2_p]


for _ in range(int(input())):
    f = int(input())

    friends = dict()
    parents = dict()

    for _ in range(f):
        a, b = input().split()

        if a not in friends:
            friends[a] = 1
            parents[a] = a
        if b not in friends:
            friends[b] = 1
            parents[b] = b

        union(a, b)

        print(friends[find(a)])
