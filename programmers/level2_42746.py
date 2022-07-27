# 가장 큰수

import itertools

def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True)

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]

    print(numbers)
    return ''.join(numbers)

print(solution([0]))
