import sys

input = sys.stdin.readline


def find(vertex):
    if parent[vertex] == vertex:
        return vertex
    else:
        parent[vertex] = find(parent[vertex])
        return parent[vertex]


v, e = map(int, input().split())
e_li = []
for _ in range(e):
    a, b, c = map(int, input().split())

    e_li.append((a - 1, b - 1, c))

parent = list(range(v))
cost_sum = 0
e_num = 0

e_li.sort(key=lambda x: x[2])

for e_i in e_li:
    a, b, cost = e_i

    a_p, b_p = find(a), find(b)

    if a_p != b_p:
        cost_sum += cost
        e_num += 1

        parent[b_p] = a_p

    if e_num == v - 1:
        break

print(cost_sum)
