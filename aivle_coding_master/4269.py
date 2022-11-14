import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = [(x, y, z)]

    while queue:
        print(queue)
        a, b, c = queue[0]
        del queue[0]

        if a == n - 1 and b == m - 1:
            return visited[a][b][c]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c == 0 :
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
        
        print(visited)
        
            
    return -1


print(bfs(0, 0, 0))