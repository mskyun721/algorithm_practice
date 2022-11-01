import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
graph_re = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

for i in zip(*graph):
    graph_re.append(list(i))

max_land = 0
for i in range(n-1):
    tmp = graph[i]
    for j in range(m-2):
        tmp_ = sum(tmp[j:j+3])
        # ㄱ
        tmp2 = tmp_ + graph[i+1][j+2]
        tmp3 = tmp_ + graph[i+1][j]
        # ㅡ
        tmp4 = 0
        if j != (m-3):
            tmp4 = tmp_ + tmp[j+3]
        # ㅁ
        tmp5 = tmp_ - tmp[j+2] + graph[i+1][j] + graph[i+1][j+1]
        max_tmp = max(tmp2, tmp3, tmp4, tmp5)

        if max_land < max_tmp:
            max_land = max_tmp

        
for i in range(n-1, 0, -1):
    tmp = graph[i]
    for j in range(m-2):
        tmp_ = sum(tmp[j:j+3])
        # ㄴ
        tmp2 = tmp_ + graph[i-1][j]
        tmp3 = tmp_ + graph[i-1][j+2]
        
        max_tmp = max(tmp2, tmp3)

        if max_land < max_tmp:
            max_land = max_tmp


for i in range(m-1):
    tmp = graph_re[i]
    for j in range(n-2):
        tmp_ = sum(tmp[j:j+3])
        # ㄱ
        tmp2 = tmp_ + graph_re[i+1][j+2]
        tmp3 = tmp_ + graph_re[i+1][j]
        # ㅡ
        tmp4 = 0
        if j != (n-3):
            tmp4 = tmp_ + tmp[j+3]
        max_tmp = max(tmp2, tmp3, tmp4)

        if max_land < max_tmp:
            max_land = max_tmp

        
for i in range(m-1, 0, -1):
    tmp = graph_re[i]
    for j in range(n-2):
        tmp_ = sum(tmp[j:j+3])
        # ㄴ
        tmp2 = tmp_ + graph_re[i-1][j]
        tmp3 = tmp_ + graph_re[i-1][j+2]
        max_tmp = max(tmp2, tmp3)

        if max_land < max_tmp:
            max_land = max_tmp

print(max_land)
