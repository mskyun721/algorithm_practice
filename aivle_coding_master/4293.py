'''
외줄타기
H대학교 컴퓨터교육과에서는 하반기 축제에서 외줄타기 이벤트를 진행합니다. 각 지점들끼리는 외줄로 연결되어 있고, 외줄을 타고 모든 지점을 통과하는 사람에게 상금으로 50만원을 수여하기로 했습니다. 모든 지점이 어떻게든 서로 도달할 수 있도록 구성되어 있으며 출발점은 본인이 정할 수 있습니다.
길이가 N인 외줄을 타는 데에 걸리는 시간은 N초입니다. 예를 들어 길이가 2인 외줄을 타는 데에는 2초가 걸립니다.
평소 승부욕과 재물욕이 많은 세아는 이번 이벤트에서 꼭 우승해서 상금을 타고 싶습니다. 세아를 위해 모든 지점을 통과할 수 있는 가장 짧은 시간을 구하는 프로그램을 작성해주세요.

INPUT
첫째 줄에 지점의 개수 V(1 ≤ V ≤ 10,000)와 외줄의 개수 E(1 ≤ E ≤ 100,000)가 주어집니다.
다음 E개의 줄에는 각 외줄에 대한 정보를 나타내는 세 정수 A, B, C가 주어집니다. 이는 A번 지점과 B번 지점이 길이가 C인 외줄로 연결되어 있다는 의미입니다. (1 ≤ A, B, C ≤ 10,000)

OUTPUT
첫째 줄에 모든 지점을 통과할 수 있는 가장 짧은 시간을 출력하세요.
'''

import sys

n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

print(graph)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
