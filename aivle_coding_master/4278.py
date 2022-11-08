import sys
import numpy as np
input = sys.stdin.readline

n = int(input())

list_work = []
days = [[0] * (n+1) for _ in range(n)]

for i in range(n):
    day, money = map(int, input().split())
    if day+i <= 5:
        for j in range(i, day+i):
            days[i][j] = 1
        days[i][n] = money

for _ in days:
    print(_)
