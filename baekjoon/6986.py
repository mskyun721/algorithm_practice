'''
절사평균 silver3
input
n : 점수의 개수
k : 절사 수

output
절사평균
보정평균
소숫점 2자리 까지
'''

import sys
import decimal

n, k = map(int, sys.stdin.readline().split())
scores = []
total_score = 0

for _ in range(n):
    score = float(sys.stdin.readline().strip())
    scores.append(score)
    total_score += score

scores.sort()

def trim_mean(arr, total):
    lenScore = n-k-k

    sumScore = total
    sumScore -= sum(arr[:k])
    sumScore -= sum(arr[-k:])
    
    return round(decimal.Decimal(sumScore / lenScore), 2) 

def adjuste_mean(arr, total):
    sumScore = trim_mean(arr, total)
    sumScore += (arr[k] * k)
    sumScore += (arr[-k-1] * k)

    return round(decimal.Decimal(sumScore / n), 2)

print('{:.2f}'.format(trim_mean(scores, total_score)))
print('{:.2f}'.format(adjuste_mean(scores, total_score)))