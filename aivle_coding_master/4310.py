# -*- coding: utf-8 -*-
import sys

n, m = map(int, input().split())
MAP = []
cnt = 0

for _ in range(n):
    MAP.append(list(input().strip()))
    
move = [(1,0),(0,1),(-1,0),(0,-1)]

for x in range(n):
    for y in range(m):
        if MAP[x][y] == '0':
            visited = [(x,y)]
            while visited:
                x_, y_ = visited.pop()
                MAP[x_][y_] = '1'
                for mv in move:
                    mx, my = x_+mv[0], y_+mv[1]
                    if 0 <= mx < n and 0 <= my < m:
                        if MAP[mx][my] == '0':
                            visited.append((mx, my))
            else:
                cnt += 1
            
print(cnt)
