import sys
import heapq
input = sys.stdin.readline

n, k, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    friend = list(map(int, input().split()))
    for i in friend:
        graph[i].extend([(j, 1) for j in friend if j != i])
        
INF = 1e9
def disjkstra(graph, start):
    distance, visited = [INF for _ in range(n+1)], []
    heapq.heappush(visited, (1, start))
    distance[start] = 1

    while visited:
        dist, node = heapq.heappop(visited)
        if distance[node] < dist:
            continue

        for i in graph[node]:
            d = distance[node] + i[1]
            if d < distance[i[0]]:
                distance[i[0]] = d
                heapq.heappush(visited, (d, i[0]))
     
    return distance[n]

result = disjkstra(graph, 1)
if result < INF:
    print(disjkstra(graph, 1))
else:
    print(-1)
 

