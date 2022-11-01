# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
games = list(map(int, input().split()))
games.sort(reverse=True)

result = [games[0]]
isWhere = True
for g in games[1:]:
    if isWhere:
        result.append(g)
        isWhere=False
    else:
        result.insert(0, g)
        isWhere=True

tmp = [abs(result[i]-result[i+1]) for i in range(-1,n-1)]
print(max(tmp))
