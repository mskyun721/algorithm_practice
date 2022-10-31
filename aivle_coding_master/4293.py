from itertools import permutations, combinations

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
loop = list(combinations(list(range(1,n+1)), 2))

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

def dfs(graph, start, end):
    # print(f'start : {start}')
    if start == end:
        # print(f'end : {path}')
        if len(path)+1 == n:
            result.append(sum(path))
    else:
        for i in range(1, n+1):
            # print(f'i : {i}')
            # print(graph[start][i], visited[i])
            if graph[start][i] != 0 and visited[i]:
                visited[start] = False
                path.append(graph[start][i])
                # print(f'path : {path}')
                dfs(graph,i, end)
                path.pop()
                # print(f'path pop : {path}')
                visited[i] = True
            # print()

result = []    
for st, ed in loop:
    visited = [True] * (n+1)
    path = []
    # print(f'loop : {st, ed}')
    dfs(graph,st, ed)

print(min(result))
