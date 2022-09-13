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


# 최대공약수(유클리드 호제법)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


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
                
            
    

