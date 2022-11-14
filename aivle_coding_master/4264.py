import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))

def lis(list_n):
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if list_n[j] < list_n[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lis(list_n))