import sys
input = sys.stdin.readline

n, m=map(int, input().split())
board = []
# test = [[i*j for i in range(51,1,-1)] for j in range(51,1,-1)]
# n = len(test)
# m = len(test[0])
# for i in test:
#     print(i)
for i in range(n):
    board.append(list(map(int, input().split())))

# 상하좌우
move = [(1,0),(0,1),(-1,0),(0,-1)]
cnt = 0
def DFS(graph, start, end):
    global cnt
    road = [[True for _ in range(m+1)] for _ in range(n+1)]
    point = graph[start[0]][start[1]]
    if start == end:
        cnt+=1
    else:
        for x, y in move:
            x_, y_ = start[0]+x, start[1]+y
            if 0 <= x_ < n and 0 <= y_ < m:
                if point > graph[x_][y_] and road[x_][y_]:
                    road[x_][y_] = False
                    DFS(graph, (x_,y_), end)
                    road[x_][y_] = True


DFS(board, (0,0), (n-1, m-1))
print(cnt%998244353)

