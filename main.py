# 조합(Itertools combinations)
def comb(arr, n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result


# 순열(Itertools permutations)
def perm(arr, n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in arr:
            tmp = [i for i in arr]
            tmp.remove(i)
            for j in perm(tmp, n-1):
                result.append([i] + j)

    return result

from collections import deque
check = [[0 for _ in range(1001)] for _ in range(1001)]
maze = []
def dfs(startX,startY,endX,endY):
    q = [(startX,startY)]
    check[startX][startY]=0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x,y= q.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if maze[nx][ny] == 0 and check[nx][ny]==0:
                    q.append((nx,ny))
                    check[nx][ny] = check[x][y]+1
                    if nx == endX and ny==endY:
                        break
    return check[endX][endY]


# dfs (depth first search) / bfs (breadth first search)
def search(graph, start_node, searchType):
    need_visited, visited = [], []
    need_visited.append(start_node)

    if searchType == 'dfs':
        while need_visited:
            node = need_visited.pop()
    
            if node not in visited:
                visited.append(node)
                need_visited.extend(graph[node])
    elif searchType == 'bfs':
        while need_visited:
            node = need_visited[0]
            del need_visited[0]

            if node not in visited:
                visited.append(node)
                need_visited.extend(graph[node])

    return visited


# DFS 전체 경로 경우의 수
def DFS(v):
    global cnt, path
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0
           
if __name__=="__main__":
    n, m=map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a, b=map(int, input().split())
        g[a][b]=1
    cnt=0
    ch[1]=1
    path=list()
    path.append(1)
    DFS(1)
    print(cnt)


# 최소공배소
def lcm(a, b):
    return a * b / gcd(a, b)


# https://docs.python.org/3.4/library/string.html
from operator import ne
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789


# list 뒤집기(역정렬)
list.reverse()
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 2차원 리스트 뒤집기
new_list = list(map(list, zip(*mylist)))


# 검색 알고리즘
#   선형 검색
def seq_search(arr, key):
    idx = 0
    for i, value in enumerate(arr):
        if value == key:
            idx = i
    
    return idx

#   이진 검색(순서 정렬 필수)
def bin_search(arr, key):
    st = 0
    ed = len(arr)-1
    
    while True:
        mid = (st + ed) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            st = mid + 1
        else:
            ed = mid - 1
        
        if st > ed:
            break
        
    return -1

#   해시 검색
# dict() 활용

#   이진 트리 https://it-garden.tistory.com/406
class node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        
class binartTree:
    def __init__(self):
        self.root = None
    
    # 전위 순환
    def preCycle(self, n):
        if n != None:
            print(n.item)
            if n.left:
                self.preCycle(n.left)
            if n.right:
                self.preCycle(n.right)
    
    # 중위 순환
    def inCycle(self, n):
        if n != None:
            if n.left:
                self.preCycle(n.left)
            print(n.item)
            if n.right:
                self.preCycle(n.right)
                
    # 후위 순환
    def postCycle(self, n):
        if n != None:
            if n.left:
                self.preCycle(n.left)
            if n.right:
                self.preCycle(n.right)
            print(n.item)
            
    # 레벨 순환
    def levelCycle(self, root):
        q = []
        q.append(root)
        while q:
            t = q.pop(0)
            print(t.item)
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.qppend(t.right)
        
    def height(self, root):
        if root == None:
            return 0
        
        return max(self.height(root.left, self.height(root.right))) + 1

# example
tree = binartTree()
n1 = node(10)
n2 = node(20)
n3 = node(30)
n4 = node(40)
n5 = node(50)
n6 = node(60)
n7 = node(70)
n8 = node(80)

tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

# 트리 높이
print(tree.height(tree.root))
# 트리 전위
print(tree.preCycle(tree.root))
# 트리 중위
print(tree.inCycle(tree.root))
# 트리 후위
print(tree.post(tree.root))
# 트리 레벨
print(tree.levelCycle(tree.root))
                

# 다익스트라 알고리즘 ( 특정 노드에서 각 노드까지의 최단 거리 )
import heapq  # 우선순위 큐 구현을 위함
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
        if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
            distances[new_destination] = distance
            heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
    return distances

# 방문하지 않은 노드 중 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node(distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(n, start):
    # 방문 체크
    visited = [False]*(n+1)
    # 최단거리 테이블
    distance = [INF]*(n+1)
    # 시작 노드
    distance[start] = 0
    visited[start] = True
    # 출발노드와 인접노드에 대해 최단거리 테이블 갱신
    for j in graph[start]:
            distance[j[0]] = j[1]

    # 모든 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 선택된 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
        # 선택된 노드를 통해 가는 비용을 다시 계산
        # 선택된 노드의 비용 + 연결된 노드로 가는 비용
            cost = distance[now] + j[1]
            # 선택된 노드를 거쳐서 가는 비용이 더 짧은 경우
            if cost<distance[j[0]]:
                distance[j[0]] = cost # 최단거리 테이블 갱신


# 플로이드-워셜 알고리즘 (모든 정점 사이의 최단 경로)
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
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