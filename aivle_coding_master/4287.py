import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

# 상하좌우
move = [(1,0),(0,1),(-1,0),(0,-1)]
graph = {}
for i in range(n):
    for j in range(m):
        center = board[i][j]

        for x, y in move:
            x_, y_ = i+x, j+y
            if 0 <= x_ < n and 0 <= y_ < m:
                tmp = board[x_][y_]
                if center > tmp:
                    if (i,j) not in graph:
                        graph[(i,j)] = [(i+x, j+y)]
                    else:
                        graph[(i,j)].append((i+x, j+y))

print(graph)