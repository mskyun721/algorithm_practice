import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    # print(f'i : {i}')
    for j in range(i):
        # print(f'j : {j}')
        # print(f'scores[j] < scores[i] : {scores[j], scores[i]}')
        if scores[j] < scores[i]:
            # print(f'dp[i], dp[j] : {dp[i], dp[j]}')
            dp[i] = max(dp[i], dp[j] + 1)
            # print(f'dp : {dp}')


print(max(dp))