# 조합
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


# 순열
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
def dfs(graph, start_node, searchType):
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