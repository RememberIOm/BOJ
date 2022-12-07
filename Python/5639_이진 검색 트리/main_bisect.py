import sys
import bisect

input = sys.stdin.readline
sys.setrecursionlimit(pow(2, 31) - 1)


def post(min, max):
    if min < max:
        right_idx = bisect.bisect_left(inputs, inputs[min], min + 1, max)
        post(min + 1, right_idx)
        post(right_idx, max)
        print(inputs[min])


inputs = []
while True:
    try:
        inputs.append(int(input()))
    except:
        break

post(0, len(inputs))
