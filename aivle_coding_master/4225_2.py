import sys
import numpy as np
input = sys.stdin.readline

server, client = map(int, input().split())

list_n = [[i for _ in range(client+1)] for i in range(server+1)]
# list_n = np.zeros((server+1, client+1))

if server == 1:
    print(1)
elif client == 1:
    print(server)
else:
    for i in range(2, server + 1):
        for j in range(2,client + 1):
                list_n[i][j] = list_n[i-1][j] + list_n[i][j-1]
    
    
    print(list_n[server][client] % 1000000007)
