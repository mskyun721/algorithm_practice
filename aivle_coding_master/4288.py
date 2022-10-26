'''
심부름
동현이 어머니는 우선 마을에 1번부터 N번까지의 N개의 집을 지으시고, 
동현이에게 도로를 건설하라는 심부름을 시키셨습니다. 
M개의 도로 후보 중 몇 개를 골라서 건설해야 합니다. 도로 후보는 세 정수 a, b, c로 이루어져 있으며, 
a번 집과 b번 집을 양방향으로 잇는 도로를 비용 c로 지을 수 있다는 뜻입니다. 

INPUT
첫 번째 줄에 동현이의 어머니께서 지으신 집의 수 N(2 ≤ N ≤ 5)과 도로 후보의 수 M(1 ≤ M ≤ 10)이 공백을 구분으로 주어집니다.
두 번째 줄부터 M+1번째 줄까지 각 도로 후보의 세 정수 a, b, c(a ≠ b, 1 ≤ a, b ≤ N, 1 ≤ c ≤ 10)가 공백을 구분으로 주어집니다.
모든 도로 후보를 사용해도 동현이가 목표를 이룰 수 없는 경우는 주어지지 않습니다.

OUTPUT
동현이가 목표를 이루려면 최소 얼마의 비용이 필요한지 출력합니다.

'''


INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)  # 방문처리 기록용
distance = [INF] * (n+1)   # 거리 테이블용

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

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