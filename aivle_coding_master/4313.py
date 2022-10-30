# -*- coding: utf-8 -*-
import sys

n = int(sys.stdin.readline())
num = [0] + list(map(int, input().split()))

def call(st, sec):
    if num[st] == 1:
        return sec+1
    
    return call(num[st], sec+1)


if n == 1:
    print(0)
else:
    result = []
    for i in range(1, n+1):
        sec = call(i, 0)
        result.append(sec)
    print(max(result))



