'''
깊이 우선 탐색1 silver 2

input 
n : 정점의 수
m : 간선의 수
r : 시작점

output
방문 순서 한줄 씩 출력 후 마지막 0
'''

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = {i:[0]*m for i in range(1,n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = v
    graph[v][u] = u


def dfs(graph, start):
    visited, need_visited = [], [start]

    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            graph[node].sort()
            need_visited.extend(graph[node])
        
    return visited

result = dfs(graph, r)
for i in result:
    print(i)

for _ in range(n - len(result)):
    print(0)