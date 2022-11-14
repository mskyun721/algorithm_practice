import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sum_list = []

if n % 2:
    result = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        result += sum(tmp)
    
    print(result)
else:
    list_n = []
    visited = []
    # dp = [[0 for _ in range(m)] for _ in range(n)]
    dp = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        list_n.append(tmp[:])
        dp.append(tmp[:])
    
    move = [(1,0),(0,1),(0,-1),(-1,0)]
    for x in range(n):
        for y in range(m):
            value = dp[x][y]
            
            for x_, y_ in move:
                dx, dy = x+x_, y+y_
                if 0 <= dx < n and 0 <= dy < m:
                    dp[dx][dy] = max(dp[dx][dy], list_n[dx][dy] + value)

            for i in dp:
                print(i)
            print()


    