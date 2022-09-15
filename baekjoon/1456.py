### 거의 소수 silver 1
'''
어떤 수가 소수의 n제곱 일때 그 수를 거의 소수라고 한다.
정수 a와 b가 주어지면 a보다 크거나 같고 b보다 작거나 같은 거의 소수가 몇개인지 출력

input
1 <= a <= b <= 10**14

'''

import sys

a, b = map(int, sys.stdin.readline().split())

list_n = [-1 for i in range(int(b ** 0.5) + 1)]

for i in range(2, int(b ** 0.5) + 1):
    if list_n[i] == -1:
        list_n[i] = i
        for j in range(i*i, int(b ** 0.5) + 1, i):
            list_n[j] = 0

list_n = [i for i in set(list_n) if i >= 2]

result = []
for i in list_n:

    n = i
    squred = 2
    while (n ** squred) <=b:
        if (n ** squred) >= a:
            result.append(n ** squred)
        squred += 1

print(len(result))