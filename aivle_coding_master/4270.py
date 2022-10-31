import sys
from itertools import permutations
n = int(input())

def perm(arr, n, len_n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in arr:
            tmp = [i for i in arr]
            tmp.remove(i)

            for j in perm(tmp, n-1, len_n):
                re = [i] + j
                result.append(re)
                

    return result

list_n = list(range(n))

perm_ = perm(list_n, n, n)
print(perm_)
count = 0
for p in perm_:
    for idx, value in enumerate(p):
        if idx == value:
            break
    else:
        count += 1

print(count)
    
