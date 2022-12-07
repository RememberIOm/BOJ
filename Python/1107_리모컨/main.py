import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
btn_broke = set(map(int, input().split()))

btn = set(range(10))
btn -= btn_broke

click_min = sys.maxsize

for i in range(0, 1_000_000):
    is_allow = True
    for i_i in str(i):
        if int(i_i) not in btn:
            is_allow = False
            break

    if is_allow:
        click_min = min(click_min, len(str(i)) + abs(n - i))

click_min = min(click_min, abs(n - 100))

print(click_min)
