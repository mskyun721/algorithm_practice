import sys
input = sys.stdin.readline

# 작업수 / 시작 작업 / 마지막 작업 / 조합
n, st, ed, m = map(int, input().split())

graph={i : [] for i in range(n)}
for i in range(m):
    # 처리작업1, 처리작업2, 사용도
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

# 작업별 효율도
list_n = list(map(int, input().split()))

for i in graph:
    tmp = []
    for j in graph[i]:
        print(j)
        tmp.append([list_n[i] + list_n[j[1]] - j[0], j[1]])
    
    graph[i] = tmp

print(graph)

visited = [True for _ in range(n)]
def dfs(graph, start):
    need_visited = [start]
    score = 0
    while need_visited:
        node = need_visited.pop()

        if visited[node]:
            visited[node] = False

            for i in graph[node]:
                need_visited.append(i[1])
                score += i[0]

    return score

print(dfs(graph, st))
print(visited)





