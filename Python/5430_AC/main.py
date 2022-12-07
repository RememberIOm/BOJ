import sys
from collections import deque

input = sys.stdin.readline


def ac_lang(q: deque, cmd: str):
    is_normal = True

    for cmd_i in cmd:
        if cmd_i == "R":
            is_normal = not is_normal
        elif cmd_i == "D":
            if not q:
                return "error"
            else:
                if is_normal:
                    q.popleft()
                else:
                    q.pop()

    if is_normal:
        return "[" + ",".join(q) + "]"
    else:
        return "[" + ",".join(reversed(q)) + "]"


t = int(input())
for _ in range(t):
    cmd = input().rstrip()
    q_num = int(input())
    q = deque(input()[1:-2].split(","))
    if q == deque([""]):
        q = deque()

    print(ac_lang(q, cmd))
