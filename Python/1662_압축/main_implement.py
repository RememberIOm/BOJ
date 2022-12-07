import sys

input = sys.stdin.readline


def unzip_part(string):
    ans = []
    mem_start, prnth, has_prnth = 0, 0, False
    for enum_s in enumerate(string):
        i, char = enum_s

        if char == "(":
            prnth += 1
            has_prnth = True
        elif char == ")":
            prnth -= 1

        if prnth == 0 and has_prnth == True:
            ans.append(string[mem_start : i + 1])
            mem_start = i + 1
            has_prnth = False

    ans.append(string[mem_start:])

    return ans


def unzip(string):
    string_parted = unzip_part(string)
    ans = 0

    for new_string in string_parted:
        mem_first = new_string.find("(")
        if mem_first == -1:
            ans += len(new_string)
        else:
            ans += len(new_string[: mem_first - 1]) + unzip(
                new_string[mem_first + 1 : -1]
            ) * int(new_string[mem_first - 1])

    return ans


s = input().rstrip()

print(unzip(s))
