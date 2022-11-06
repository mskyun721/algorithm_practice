import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph.append((c, a, b))

def find_parent(parent, a):
    if parent[a] != a:
        return find_parent(parent, parent[a])
    
    return a

def union_parent(parent, a, b):
    # print(f'bef : {a, b}')
    # print(parent)
    a_ = find_parent(parent, a)
    b_ = find_parent(parent, b)
    # print(f'aft : {a_, b_}')

    if a_ == b_:
        return False
    else:
        parent[max(a_,b_)] = min(a_,b_)
        # print(parent)
        return True
graph.sort()
def kruskal(graph, parent):
    total_cost = 0
    for c, a, b in graph:
        if union_parent(parent, a, b):
            total_cost += c
            # print(total_cost)
    
    return total_cost

print(kruskal(graph, parent))
        



