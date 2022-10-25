'''
배 Gold 5

input
n : 크레인 수
1 ~ n : 크레인 제한 무게
m : 화물 수
1 ~ m : 화물 무게

output
최소 시간
'''

import sys
input = sys.stdin.readline

n = int(input())
cariers = list(map(int, input().split()))
cariers.sort()

m = int(input())
boxs = list(map(int, input().split()))
boxs.sort()


def solution(carier=cariers, box=boxs, c=0):
    count = c
    carier = carier
    box = box
