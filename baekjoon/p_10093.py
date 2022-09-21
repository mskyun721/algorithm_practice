'''
숫자 bronze 2

두 수 사이의 개수와 오름차순 출력
'''

a, b = map(int, input().split())

listN = list(range(min(a,b)+1, max(a,b)))

print(len(listN))
print(' '.join(map(str, listN)))