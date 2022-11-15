import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

move = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(x, y, z):
    queue = [(x, y, z)]

    while queue:
        a, b, c = queue[0]
        del queue[0]

        if a == n - 1 and b == m - 1:
            return visited[a][b][c]

        for x_, y_ in move:
            nx, ny = a + x_, b + y_

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c == 0 :
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
            
    return -1


print(bfs(0, 0, 0))