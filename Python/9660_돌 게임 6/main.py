import sys

input = sys.stdin.readline

n = int(input())
ndiv = n % 7

if ndiv == 0 or ndiv == 2:
    print("CY")
else:
    print("SK")
