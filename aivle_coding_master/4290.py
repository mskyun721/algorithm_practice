'''
영양 점수
요리의 영양 점수는 맛이나 모양이 아닌 요리에 들어간 모든 식재료들에게서 발현되는 영양 점수의 합을 말합니다. 
모든 식재료는 자기 자신으로는 영양 점수를 가질 수 없습니다. 
모든 식재료는 두개 씩 재료가 서로 조합이 되었을 때 비로소 영양 점수가 발현됩니다.

식재료로 A, B, C, D가 있다고 했을 때 A와 B를 뽑아서 음식을 만든다면, 
A가 B랑 조합될 때의 A에서 발현 되는 영양 점수와 B가 A랑 조합될 때 B에서 발현 되는 영양 점수를 합한 것이 음식의 최종 영양 점수가 됩니다.
이는 (A, B) + (B, A)로 표현할 수 있습니다.

A, B, C, D, E, F,가 있다고 했을 때 A, B, C를 뽑아서 음식을 만든다면, 
(A, B) + (B, A) + (A, C) + (C, A) + (B, C) + (C, B)가 됩니다. 
무조건 식재료는 두 개씩 서로 발현되는 것입니다.

식재료의 개수가 N이라고 할 때, 
각 요리당 N / 2가지의 식재료를 사용할 계획인데 요리마다 사용하는 식재료는 서로 다르게 할 생각입니다.

식재료를 정확히 반으로 나누어서 각 요리에 적용하려고 합니다. 
따라서 주성이가 가지고 있는 식재료의 개수는 반드시 짝수로 주어집니다. 
각각의 식재료들이 두 개씩 조합되었을 때 발현되는 영양 점수가 행렬 형태로 주어졌을 때 주성이가 생각한대로 요리를 할 수 있게 하는 프로그램을 작성해주세요.

INPUT
첫째 줄에 주성이가 현재 가지고 있는 식재료의 개수 N(4 ≤ N ≤ 20, N은 짝수)이 주어집니다.
둘째 줄부터 N개의 줄에 각 식재료에서 발현되는 영양 점수 S가 주어집니다. 
이 때각 줄에는 N개의 수가 서로 공백을 두고 주어져 있고, i번 줄의 j번째 수는 Sij입니다. 
Sij는 i번째 식재료와 j번째 식재료를 조합했을 때 i번째 식재료에서 발현되는 영양 점수입니다.
Sii는 항상 0이며 나머지 Sij는 1보다 크거나 같고 100보다 작거나 같은 정수입니다.

OUTPUT
첫째 줄에 두 요리의 영양 점수의 차이의 최솟값을 출력합니다.
'''

import sys
input = sys.stdin.readline

from itertools import combinations, permutations

n = int(input())
score = []
list_n = [i for i in range(n)]
comb_n = list(combinations(list_n, n//2))

for _ in range(n):
    score.append(list(map(int, input().split())))

min_diff = []
for i in range(len(comb_n) // 2):
    tmp = comb_n[i]
    other = list(set(list_n).difference(tmp))

    perm_tmp = list(permutations(tmp, 2))
    perm_other = list(permutations(other, 2))
    a_score, b_score = 0, 0

    for x, y in perm_tmp:
        a_score += score[x][y]

    for x, y in perm_other:
        b_score += score[x][y]

    min_diff.append(abs(a_score - b_score))

print(min(min_diff))


