

import sys
from itertools import combinations

input = sys.stdin.readline

move = [(1,0),(0,1),(-1,0),(0,-1)]

n, m = map(int, input().split())
zoo = []
bins = []
jaguars = []
jaguars_side_bin = []

for i in range(n):
    zoo.append(list(map(int, input().split())))


for x in range(n):
    for y in range(m):
        if zoo[x][y] == 0:
            bins.append((x,y))
            for t in move:
                x_, y_ = x+t[0], y+t[1]
                if (0 <= x_ < n) and (0 <= y_ < m):
                    if zoo[x_][y_] == 2:
                        jaguars_side_bin.append((x,y))
                        break
        elif zoo[x][y] == 2:
            jaguars.append((x,y))

print(bins)
print(jaguars)
print(jaguars_side_bin)

comb_bin = list(combinations(jaguars_side_bin, 3))
print(comb_bin)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(graph, x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


for comb in comb_bin:
    tmp_zoo = zoo.copy()
    for point in comb:
        tmp_zoo[point[0]][point[1]] = 1
    
    for start in jaguars:
        for t in move:
            x_, y_ = start[0]+t[0], start[1]+t[1]
            if (0 <= x_ < n) and (0 <= y_ < m):
                if tmp_zoo[x_][y_] == 0:
                    pass