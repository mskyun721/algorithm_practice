import sys
from itertools import combinations
input = sys.stdin.readline

sever, client = map(int, input().split())

list_n = [i for i in range(1, sever+1)] * client

comb = list(combinations(list_n, client))
comb = list(set(comb))
if sever == 1:
    print(1)
else:
    count = 0
    for i in comb:
        for j in range(len(i)-1):
            if i[j] > i[j+1]:
                break
        else:
            count += 1
    
    print(count)
