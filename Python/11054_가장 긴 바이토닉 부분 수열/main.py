import sys

input = sys.stdin.readline

N = int(input())
NUMS = tuple(map(int, input().split()))

inc_dp = [0] * N
dec_dp = [0] * N

for I in range(N):
    I_INC = I
    I_DEC = N - I - 1

    for COMP_I in range(I):
        COMP_I_INC = COMP_I
        COMP_I_DEC = N - COMP_I - 1

        if NUMS[COMP_I_INC] < NUMS[I_INC]:
            inc_dp[I_INC] = max(inc_dp[I_INC], inc_dp[COMP_I_INC])

        if NUMS[COMP_I_DEC] < NUMS[I_DEC]:
            dec_dp[I_DEC] = max(dec_dp[I_DEC], dec_dp[COMP_I_DEC])

    inc_dp[I_INC] += 1
    dec_dp[I_DEC] += 1

BITONIC = map(lambda x, y: x + y - 1, inc_dp, dec_dp)

print(max(BITONIC))
