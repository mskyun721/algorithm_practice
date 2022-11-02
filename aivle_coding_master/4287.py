import sys
input = sys.stdin.readline

n, m=map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

# 상하좌우
move = [(1,0),(0,1),(-1,0),(0,-1)]
graph = {}
for i in range(n):
    for j in range(m):
        center = board[i][j]
        graph[(i,j)] = []

        for x, y in move:
            x_, y_ = i+x, j+y

            if 0 <= x_ < n and 0 <= y_ < m:
                tmp = board[x_][y_]
                if center > tmp:
                    graph[(i,j)].append((i+x, j+y))


cnt = 0
def DFS(graph, start, end):
    global cnt
    # path = []
    road = [[True for _ in range(m+1)] for _ in range(n+1)]

    if start == end:
        cnt+=1
    else:
        for i in graph[start]:
            if road[i[0]][i[1]]:
                road[i[0]][i[1]] = False
                # path.append(i)
                DFS(graph, i, end)
                # path.pop()
                road[i[0]][i[1]] = True


DFS(graph, (0,0), (n-1, m-1))
print(cnt%998244353)