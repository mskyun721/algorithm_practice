# -*- coding: utf-8 -*-
import sys

# 1 : 육지, 0 : 바다
# m : 가로, n : 세로, k : 육지 수
m, n, k = map(int, input().split())
MAP = [[0 for i in range(n)] for j in range(m)]
land = []
fly_cnt = 0

# 육지 좌표
for _ in range(k):
    x, y = map(int, input().split())
    MAP[x][y] = 1
    land.append([x,y])
    
move = [(1,0),(0,1),(-1,0),(0,-1)]

def road(point):
    global fly_cnt

    if MAP[point[0]][point[1]] == 1:
        visited = [point]
        while visited:
            x, y = visited.pop()
            MAP[x][y] = 0
            for x_, y_ in move:
                x_, y_ = x+x_, y+y_
                if 0 <= x_ < n and 0 <= y_ < m:
                    if MAP[x_][y_] == 1:
                        visited.append([x_, y_]) 
        else:
            fly_cnt += 1


for i in land:
    road(i)

print(fly_cnt)
