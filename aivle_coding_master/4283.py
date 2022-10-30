# -*- coding: utf-8 -*-
import sys
from itertools import permutations
from itertools import combinations

n = int(sys.stdin.readline())
games = list(map(int, input().split()))
# perm = list(permutations(games, 6))
# comb = list(permutations(games, 2))


# for i in perm:
#     print(i)

# print()

score = []
for i in games:
    tmp = []
    for j in games:
        tmp.append(abs(i-j))

    score.append(tmp)

for i in score:
    print(i)

    
    
    