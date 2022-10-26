'''
태일이가 다니는 학교에는 얼마전 홍수가 크게 나서 길이 다 사라졌습니다. 
대신 학교 건물들 중에서 몇몇 건물들은 서로 다리 하나로 연결되어 있다고 합니다.
연결이 되어 있는 건묻들끼리는 서로 왕래할 수 있습니다.
태일이는 조금 있으면 수업에 가야하는데 강의실까지 거리가 꽤 됩니다. 
현재 태일이가 있는 건물에서 강의실까지 가장 빨리 갈 수 있게 도와주는 프로그램을 작성해주세요.

INPUT
첫째 줄에 학교 내 건물의 개수 N(1 ≤ N ≤ 100)과 다리의 개수 M(1 ≤ M ≤ 100,000)이 주어집니다.
둘째 줄부터 M + 1줄까지 처음에는 서로 연결되어 있는 건물들의 번호가 주어지고 
이 건물들 사이를 오가는 데 걸리는 소요시간이 주어집니다.
M + 2번째 줄에는 태일이가 현재 있는 건물의 번호와 가야하는 강의실의 건물 번호가 주어집니다. 
소요 시간은 0보다 크고 100,000보다 작은 정수입니다.
또한, 도달할 수 없는 경우는 주어지지 않습니다.

OUTPUT
태일이가 강의에 가는 데에 걸리는 최소시간을 출력하세요.
'''

# import sys

# n, m = map(int, input().split())
# graph = {i : {} for i in range(1, n+1)}

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c

# start, end = map(int, input().split())
# import heapq  # 우선순위 큐 구현을 위함

# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph} 
#     distances[start] = 0 
#     queue = []
#     heapq.heappush(queue, [distances[start], start]) 

#     while queue: 
#         current_distance, current_destination = heapq.heappop(queue) 

#         if distances[current_destination] < current_distance:
#             continue
        
#         for new_destination, new_distance in graph[current_destination].items():
#             distance = current_distance + new_distance
#         if distance < distances[new_destination]:
#             distances[new_destination] = distance
#             heapq.heappush(queue, [distance, new_destination])
    
#     return distances

# print(dijkstra(graph, start)[end])


import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

# 주어지는 그래프 정보 담는 N개 길이의 리스트
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)  # 방문처리 기록용
distance = [INF] * (n+1)   # 거리 테이블용

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())
# 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작노드 -> 시작노드 거리 계산 및 방문처리
    distance[start] = 0
    visited[start] = True
    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_smallest_node()  # 방문X 면서 시작노드와 최단거리인 노드 반환
        visited[now] = True        # 해당 노드 방문처리
        # 해당 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            cost = distance[now] + next[1]  # 시작->now 거리 + now->now의 인접노드 거리
            if cost < distance[next[0]]:    # cost < 시작->now의 인접노드 다이렉트 거리
                distance[next[0]] = cost


dijkstra(start)


print(distance[end])