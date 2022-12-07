import sys
import itertools
import copy

input = sys.stdin.readline


n, m = map(int, input().split())
virus_map = sum([list(input().split()) for _ in range(n)], [])

VIRUS_MAP_LEN = len(virus_map)

blanks, viruses = [], []

for i in range(VIRUS_MAP_LEN):
    if virus_map[i] == "0":
        blanks.append(i)
    elif virus_map[i] == "2":
        viruses.append(i)

blank_max = 0
kabes = itertools.combinations(blanks, 3)

for kabe in kabes:
    virus_map_cur = copy.deepcopy(virus_map)
    for kabe_i in kabe:
        virus_map_cur[kabe_i] = "1"

    virus_move = set(viruses)

    while virus_move:
        virus_cur = virus_move.pop()

        virus_next = []

        if virus_cur % m != 0:
            virus_next.append(virus_cur - 1)
        if virus_cur % m != m - 1:
            virus_next.append(virus_cur + 1)
        if virus_cur // m != 0:
            virus_next.append(virus_cur - m)
        if virus_cur // m != n - 1:
            virus_next.append(virus_cur + m)

        for virus_next_i in virus_next:
            if virus_map_cur[virus_next_i] == "0":
                virus_map_cur[virus_next_i] = "2"
                virus_move.add(virus_next_i)

    blank_max = max(blank_max, virus_map_cur.count("0"))

print(blank_max)
