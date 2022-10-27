

import sys
input = sys.stdin.readline

from itertools import combinations, permutations

n = int(input())
score = []
list_n = [i for i in range(n)]
comb_n = list(combinations(list_n, n//2))

for _ in range(n):
    score.append(list(map(int, input().split())))

min_diff = []
for i in range(len(comb_n) // 2):
    tmp = comb_n[i]
    other = list(set(list_n).difference(tmp))

    perm_tmp = list(permutations(tmp, 2))
    perm_other = list(permutations(other, 2))
    a_score, b_score = 0, 0

    for x, y in perm_tmp:
        a_score += score[x][y]

    for x, y in perm_other:
        b_score += score[x][y]

    min_diff.append(abs(a_score - b_score))

print(min(min_diff))


