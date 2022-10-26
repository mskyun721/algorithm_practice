'''
병원
유진이는 버스를 타고 병원에 가려고 합니다.

유진이가 살고있는 동네에는 N개의 버스 정류장과 M개의 버스 경로가 존재합니다.
버스 정류장에는 1번부터 N번까지 번호가 붙어있습니다.
버스 정류장과 버스 경로에 대한 정보가 주어질 때, 
유진이의 집 근처 버스 정류장에서 출발해 병원 근처 버스 정류장까지 버스로 이동하는 데 걸리는 시간의 최솟값을 구하는 프로그램을 작성해주세요.

INPUT
첫째 줄에 버스 정류장의 개수 N이 주어집니다. 
N은 1 이상 5 이하의 양의 정수입니다.

둘째 줄에는 운행하는 버스 경로의 개수 M이 주어집니다. 
M은 1 이상 10 이하의 양의 정수입니다.

그리고 셋째 줄부터 M+2번째 줄까지 경로의 시작 정류장 번호 U, 경로의 도착 정류장 번호 V, 이동 시간 T가 주어집니다. 
이는 U번 정류장에서 버스를 타서 V번 정류장까지 이동하는 데 T분이 걸린다는 의미입니다.
M+3번째 줄에는 유진이의 집 근처 버스 정류장 번호 S와 병원 근처 버스 정류장 번호 E가 공백으로 구분되어 주어집니다. 
S에서 E로 이동할 수 없는 입력은 주어지지 않습니다.
'''

import sys

from sympy import I
input = sys.stdin.readline
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)  # 방문처리 기록용
distance = [INF] * (n+1)   # 거리 테이블용

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))


start, end = map(int, input().split())

print(graph)
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = I
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
