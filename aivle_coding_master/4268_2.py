import sys
from collections import deque

n, k, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    inputs = list(map(int, input().split()))
    for idx, x in enumerate(inputs):
        graph[x].extend(inputs[:idx] + inputs[idx+1:])


def bfs(n,a):
    queue = deque()
    queue.append(a)
    visited[a] = 1

    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if visited[i] == 0 or visited[i] > visited[node] + 1:
                visited[i] = visited[node]+1
                queue.append(i)
                  
            
    if visited[n] == 0:
        return -1
    else:
        return visited[n]


print(bfs(n, 1))

