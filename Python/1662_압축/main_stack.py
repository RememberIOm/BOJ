import sys

input = sys.stdin.readline

s = input().rstrip()

stk = []
length = 0
for i, s_i in enumerate(s):
    if s_i == "(":
        stk.append([int(s[i - 1]), length - 1])
        length = 0
    elif s_i == ")":
        mul, cur_length = stk.pop()

        length = mul * length + cur_length
    else:
        length += 1

print(length)
