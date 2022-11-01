import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i : [] for i in range(1,n+1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

def search_Dfs(graph, start):
    need_visited, visited = [start], []

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            if graph[node]:
                graph[node].sort(reverse=True)
                need_visited.extend(graph[node])
    
    return visited


tmp = search_Dfs(graph, 1)
for i in tmp:
    print(i, end=' ')

                