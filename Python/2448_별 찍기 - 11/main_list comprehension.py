import sys

input = sys.stdin.readline


def star(h):
    if h == 3:
        return ["  *  ", " * * ", "*****"]

    s = star(h // 2)

    ret_a = [" " * (h // 2) + i + " " * (h // 2) for i in s]
    ret_b = [i + " " + i for i in s]

    return ret_a + ret_b


n = int(input())

print(*star(n), sep="\n")
