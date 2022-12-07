import sys

sys.setrecursionlimit(100_000)

input = sys.stdin.readline


def area(color, rgb, x, y):
    rgbLen = len(rgb)
    rgb[y][x] = "0"

    if x - 1 >= 0 and rgb[y][x - 1] == color:
        area(color, rgb, x - 1, y)
    if x + 1 < rgbLen and rgb[y][x + 1] == color:
        area(color, rgb, x + 1, y)
    if y - 1 >= 0 and rgb[y - 1][x] == color:
        area(color, rgb, x, y - 1)
    if y + 1 < rgbLen and rgb[y + 1][x] == color:
        area(color, rgb, x, y + 1)


n = int(input())
rgb, rgbHen = [], []
for i in range(n):
    inputStr = input().rstrip()
    inputStrHen = inputStr.replace("G", "R")
    rgb.append(list(inputStr))
    rgbHen.append(list(inputStrHen))

rgbCnt, rgbHenCnt = 0, 0
for i in range(n):
    for j in range(n):
        if rgb[i][j] != "0":
            area(rgb[i][j], rgb, j, i)
            rgbCnt += 1
        if rgbHen[i][j] != "0":
            area(rgbHen[i][j], rgbHen, j, i)
            rgbHenCnt += 1

print(rgbCnt, rgbHenCnt)
