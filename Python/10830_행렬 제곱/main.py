import sys

input = sys.stdin.readline


def mat_mul(mat_a, mat_b):
    global n

    mat_ans = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for seq in range(n):
                mat_ans[i][j] += mat_a[i][seq] * mat_b[seq][j]
                mat_ans[i][j] %= 1_000

    return mat_ans


def mat_exp(mat, exp):
    if exp == 1:
        return mat

    mat_exp_part = mat_exp(mat, exp // 2)

    if exp % 2:
        return mat_mul(mat_mul(mat_exp_part, mat_exp_part), mat)
    else:
        return mat_mul(mat_exp_part, mat_exp_part)


n, b = map(int, input().split())
mat = [tuple(map(int, input().split())) for _ in range(n)]

mat = mat_exp(mat, b)

for mat_i in mat:
    print(*map(lambda x: x % 1000, mat_i))
