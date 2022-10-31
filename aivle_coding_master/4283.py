# -*- coding: utf-8 -*-
import sys
from itertools import permutations

n = int(sys.stdin.readline())
games = list(map(int, input().split()))

perm = list(permutations(games, n))

result = []
for p in perm[0:len(perm)//n]:
    tmp = [abs(p[i]-p[i+1]) for i in range(-1,n-1)]
    result.append(max(tmp))
    
print(min(result))
    