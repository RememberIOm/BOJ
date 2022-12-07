import sys

input = sys.stdin.readline


def isStar(row, col, scale):
    while True:
        scaleDiv3 = scale / 3

        if (
            row >= scaleDiv3
            and row < scaleDiv3 * 2
            and col >= scaleDiv3
            and col < scaleDiv3 * 2
        ):
            return False
        elif scale == 3:
            return True
        else:
            row %= scaleDiv3
            col %= scaleDiv3
            scale /= 3


a = int(input())

entireStr = ""
for col in range(a):
    for row in range(0, a, 3):
        if isStar(row, col, a):
            if col % 3 == 1:
                entireStr += "* *"
            else:
                entireStr += "***"
        else:
            entireStr += "   "
    entireStr += "\n"

print(entireStr)
