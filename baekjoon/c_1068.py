'''
트리 Gold 5

n : 노드의 개수
0 ~ n-1노드 : 각 노드의 부모 모드. -1은 부모노드 없음
d : 제거할 노드. 해당 노드의 자식노드도 모두 제거됨
'''
# import sys
# input = sys.stdin.readline

# n = int(input())

# tree = [[] for _ in range(n)]
# root, answer = 0, 0

# for node, parent in enumerate(map(int, input().split())):
#     if parent == -1:
#         root = node
#     else:
#         tree[parent].append(node)

# deleted = int(input())

# def search(graph, start, deln):
#     visited, need_visited = [deln], [start]

#     while


import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n)]
visited = [False] * n
root = answer = 0

for node, parent in enumerate(map(int, input().split())):
    if parent == -1:
        root = node
    else:
        tree[parent].append(node)

deleted = int(input())
visited[deleted] = True

def dfs(s):
    global answer

    if visited[s]: return
    visited[s] = True

    if len(tree[s]) == 0:
        answer += 1
        return
    elif len(tree[s]) == 1 and tree[s][0] == deleted:
        answer += 1

    for x in tree[s]:
        dfs(x)

dfs(root)

print(answer)