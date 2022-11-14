import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i : [] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start):
    need_visited, visited = [start], []

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited

cnt = 0
st = [True for _ in range(n+1)]
for i in range(1, n+1):
    if st[i]:
        tmp = dfs(graph, i)
        cnt+=1
        for j in tmp:
            st[j] = False

print(cnt)
    
