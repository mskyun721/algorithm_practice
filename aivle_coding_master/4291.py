'''
탈출사건
빈동이는 동물원의 안전 책임자입니다. 
동물원은 N행 M열의 격자, 총 N × M 칸으로 나눌 수 있습니다. 
어느 날 재규어들이 우리에서 탈출했습니다. 
이 재규어들은 매우 공격적이라 당장 포획할 수 없습니다. 
빈동이는 입장객들에게 대피하라고 알린 뒤, 날뛰는 재규어를 막을 방법을 찾아냈습니다.

동물원은 빈 칸, 재규어가 있는 칸, 울타리가 있는 칸으로 구분할 수 있습니다. 
재규어들은 상하좌우 중 한 방향으로 인접한 빈 칸으로 이동할 수 있으며, 동물원 밖으로 나가지 못합니다. 
빈동이의 목표는 3개의 여분 울타리를 반드시 모두 설치해, 재규어가 도달할 수 없는 칸의 수를 최대화 하는 것입니다. 
여분 울타리는 빈 칸에만 설치할 수 있고, 설치하면 그 칸은 울타리가 있는 칸이 됩니다. 
빈동이가 목표를 달성했을 때, 재규어가 도달할 수 없는 빈 칸의 수를 출력하는 프로그램을 작성해주세요.

IMPUT
첫째 줄에 동물원의 세로 크기 N과 가로 크기 M이 공백을 두고 주어집니다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N+1째 줄까지, 각 줄에 공백으로 구분된 M개의 숫자로 동물원의 상태가 주어집니다.
0은 빈 칸, 1은 울타리가 있는 칸, 2는 재규어가 있는 칸입니다.
주어진 동물원의 상태에 빈 칸은 3개 이상, 재규어는 1마리 이상 존재함이 보장됩니다.

OUTPUT
3개의 울타리를 모두 설치한 뒤 재규어로부터 안전한 빈 칸의 개수의 최댓값을 출력합니다.
'''

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