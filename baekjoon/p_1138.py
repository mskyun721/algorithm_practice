'''
한 줄로 서기 silver 2

input
1. n : 사람 수
2. 1 ~ n : 본인 보다 큰 왼쪽 사람 수

output
n명 순서대로 나열
'''

import sys
input = sys.stdin.readline

n = int(input())
list_n = [0 for i in range(n)]

left = map(int, input().split())

for i, l in enumerate(left):
    if i == 0:
        list_n[l] = i+1
    elif i == (n-1):
        idx = list_n.index(0)
        list_n[idx] = n
    else:
        idx = i+1
        count = -1
        for e, j in enumerate(list_n):
            if j == 0 or j >= idx:
                count += 1
            
            if count == l:
                list_n[e] = idx
                break


print(' '.join(map(str, list_n)))
        
