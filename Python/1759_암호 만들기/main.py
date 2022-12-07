import sys
import itertools

input = sys.stdin.readline

l, c = map(int, input().split())
alphabet = sorted(input().split())

pw = itertools.combinations(alphabet, l)
vowel_set = set("aeiou")

for pw_i in pw:
    vowel = 0
    for pw_i_alphabet in pw_i:
        if pw_i_alphabet in vowel_set:
            vowel += 1

    consonant = l - vowel

    if vowel >= 1 and consonant >= 2:
        print("".join(pw_i))
