'''
RGB 거리 silver 1

Input
1. n : 집의 개수
2. n개의 색칠 비용 (빨, 초, 파)

Output
최소 비용
'''

import sys
input = sys.stdin.readline

loop = n = int(input())
cost = 0

combination = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]

while loop > 0:
    rgb = []
    if (loop // 3) > 0:
        for _ in range(3):
            rgb.append(list(map(int, input().split)))
    else:
        for _ in range(loop % 3):
            rgb.append(list(map(int, input().split)))

