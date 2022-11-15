import sys
input = sys.stdin.readline

# A:빨간색 / B:파란색 / O:빈칸 / X:검은색
n, m = map(int, input().split())

arr = []
not_black = []
visited = [[True for _ in range(m)] for _ in range(n)]
for i in range(n):
    tmp = list(input().strip())
    arr.append(tmp)
    for idx, j in enumerate(tmp):
        if j != 'X':
            not_black.append((i, idx))
        else:
            visited[i][idx] = False

move = [(1,0),(0,1),(-1,0),(0,-1)]
color = [0,0]
def dfs(graph, st):
    global color
    need_visited = [st]
    red, blue = 0, 0

    while need_visited:
        x, y = need_visited.pop()

        if visited[x][y]:
            visited[x][y] = False
            
            if graph[x][y] == 'A':
                red += 1
            elif graph[x][y] == 'B':
                blue += 1

            for x_, y_ in move:
                dx, dy = x+x_, y+y_
                if 0 <= dx < n and 0 <= dy < m:
                    need_visited.append((dx,dy))
                    
                    
    
    if blue >= red:
        color[1] += blue
    else:
        color[0] += red


for i in range(n):
    for j in range(m):
        if visited[i][j]:
            dfs(arr, (i,j))

print(color[0], color[1])





