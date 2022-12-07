import sys

input = sys.stdin.readline

input_str = input().rstrip()
bomb_str = input().rstrip()
use_stk = []

for str in input_str:
    use_stk.append(str)
    if str == bomb_str[-1]:
        if bomb_str == "".join(use_stk[-len(bomb_str) :]):
            del use_stk[-len(bomb_str) :]

if len(use_stk):
    print(*use_stk, sep="")
else:
    print("FRULA")
