import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

friend_no = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    friend = list(map(int, input().split()))
    for i in friend:
        graph[i].extend([j for j in friend if j != i])
        
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
            if (distance[node] + 1) < distance[i]:
                distance[i] = distance[node] + 1
                heapq.heappush(visited, (distance[i], i))
     
    return distance[n]

result = disjkstra(graph, 1)
if result < INF:
    print(disjkstra(graph, 1))
else:
    print(-1)
 


