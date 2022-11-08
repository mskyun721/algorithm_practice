import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def dfs(graph, start):
    need_visited, visited = [start], []

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            need_visited.extend(graph[node])
            visited.append(node)
    
    return len(visited)


result = [(0, i) for i in range(n+1)]
for i in range(1,n+1):
    result[i] = (dfs(graph, i)-1, i)

result.sort(key=lambda x:(-x[0], x[1]))
follow = result[0][0]
for i in result:
    if i[0] >= follow:
        print(i[1], end=' ')
    else:
        break

    