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

dp = [[-1 for _ in range(m)] for _ in range(n)]
# 상하좌우
move = [(1,0),(0,1),(-1,0),(0,-1)]
cnt = 0
def DFS(graph, start, end):
    global cnt
    point = graph[start[0]][start[1]]
    print(f'start : {start, point, dp[start[0]][start[1]]}')
    if start == end:
        print(f'cnt(start == end) : {cnt+1, start}')
        return 1
    
    # dp??
    if dp[start[0]][start[1]] != -1:
        print(f'dp : {dp[start[0]][start[1]], start}')
        print(f'cnt(dp) : {cnt+1, start}')
        return dp[start[0]][start[1]]
        
    for x, y in move:
        x_, y_ = start[0]+x, start[1]+y
        if 0 <= x_ < n and 0 <= y_ < m:
            if point > graph[x_][y_]:
                cnt += DFS(graph, (x_,y_), end)
      
    dp[start[0]][start[1]] = cnt
    print(f'end : {dp[start[0]][start[1]], start}')
    print(f'cnt(end) : {cnt, start}')
    return dp[start[0]][start[1]]


DFS(board, (0,0), (n-1, m-1))
print(cnt%998244353)

