''''
수열의 합 silver 2

input
n, l : 합, 최소 개수

output
연속된 정수 
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split())

while l <= min(int(n*2**0.5)+1, 100):
    a = n // l
    stop = False

    list_n = list(range(max(0,a-l),a+l+1))
    for i in range(len(list_n) - l):
        
        if n == sum(list_n[i:i+l]):
            print(' '.join(map(str, list_n[i:i+l])))
            stop = True
            break
    else:
        l += 1
    
    if stop:
        break

else:
    print(-1)