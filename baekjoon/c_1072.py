'''
게임 silver 3
input
게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 
형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

제한
1 ≤ X ≤ 1,000,000,000
0 ≤ Y ≤ X

output
최소 판수, 절대 변하지 않으면 -1
'''

from math import floor
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
e = floor(100 * y / x)
low, high = 0, x

if e >= 99: 
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        tx, ty = x + mid, y + mid

        if floor(100 * ty / tx) > e: 
            high = mid - 1
        else: 
            low = mid + 1
    print(high + 1)



