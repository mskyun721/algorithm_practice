import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
MAP = [[0 for _ in range(m)] for _ in range(n)]
city = []
start = []
for i in range(n):
    tmp = list(map(int, input().split()))
    city.append(tmp)

    for idx, j in enumerate(tmp):
        if j == 1:
            start.append((i,idx))
            

move = [(1,0),(0,1),(-1,0),(0,-1)]
def search(graph, st):
    need_visited = deque()
    need_visited.append(st)

    while need_visited:
        x, y = need_visited.popleft()
        
        for x_, y_ in move:
            dx, dy = x+x_, y+y_
            if 0 <= dx < n and 0 <= dy < m:
                if graph[dx][dy] != 2 and (dx,dy) not in start:
                    if MAP[dx][dy] == 0 or MAP[dx][dy] > MAP[x][y] + 1:
                        MAP[dx][dy] = MAP[x][y] + 1
                        need_visited.append((dx,dy))
                        
for st in start:
    search(city, st)
    MAP[st[0]][st[1]] = -1

day = 0
for i in MAP:
    if 0 in i:
        print(-1)
        break
    
    day = max(max(i), day)
else:
    print(day)
