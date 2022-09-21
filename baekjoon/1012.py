'''
유기농 배추 silver 2

input
t : test case
m, n, k : 가로, 세로, 배추 위치 개수
x, y : 배추위치

output
test case 별 지렁이 수
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    # tmp = [[0 for i in range(m)] for j in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        

    print(count)
