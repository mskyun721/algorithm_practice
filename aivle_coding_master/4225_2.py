import sys
input = sys.stdin.readline

server, client = map(int, input().split())

list_n = [[0 for _ in range(client+1)] for _ in range(server+1)]

if server == 1:
    print(1)
elif client == 1:
    print(server)
else:
    list_n[1] = [1 for _ in range(client+1)]
    for i in range(1, server + 1):
        for j in range(1,client + 1):
            if j == 1:
                list_n[i][j] = i
            else:
                list_n[i][j] = list_n[i-1][j] + list_n[i][j-1]
    
    print(list_n[server][client] % 1000000007)
