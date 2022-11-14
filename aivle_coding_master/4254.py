import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i : [] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(graph, start):
    need_visited = [start]
    visited = []

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
        else:
            return True
    
    return False

for i in range(1,n+1):
    if dfs(graph, i):
        print('YES') 
        break
else:
    print('NO')

