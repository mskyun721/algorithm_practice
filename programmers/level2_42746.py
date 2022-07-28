# 가장 큰수

# 1 <= numbers 길이 <= 100,000
# numbers 원소 : 0 ~ 1,000

import itertools

def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True)
    print(numbers)

    for i in range(0, len(numbers) - 1):
        if numbers[i] + numbers[i+1] < numbers[i+1] + numbers[i]:
            numbers[i+1], numbers[i] = numbers[i], numbers[i+1]

    print(numbers)
    return ''.join(numbers)

print(solution([3, 30, 34, 5, 9]))
