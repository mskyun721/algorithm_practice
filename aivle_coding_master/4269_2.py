import sys
input = sys.stdin.readline


def search(graph, start, end, cut_point):
    MAP = [[0 for _ in range(m)] for _ in range(n)]
    node = [start]
    graph[cut_point[0]][cut_point[1]] = '0'
    while node:
        x, y = node.pop()
        for x_, y_ in move:
            nx, ny = x+x_, y+y_
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0':
                    node.append((nx, ny))
                    MAP[nx][ny] += MAP[x][y] + 1
    
    return MAP[end[0]][end[1]]



n, m = map(int, input().split())
move = [(1,0),(0,1),(-1,0),(0,-1)]
road = []
for _ in range(n):
    road.append(list(input().strip()))

start, end = (0,0), (n-1, m-1)

wood = []
for i in range(n):
    for j in range(m):
        if road[i][j] == '1':
            cnt = 0
            for x, y in move:
                x_, y_ = i+x, y+j
                if 0 <= x_ < n and 0 <= y_ < m:
                    if road[x_][y_] == '0':
                        cnt += 1
                    
                    if cnt == 2:
                        wood.append((i,j))
                        break

result = []
if not wood:
    print(-1)
else:
    for w in wood:
        result.append(search(road, start, end, w))


            