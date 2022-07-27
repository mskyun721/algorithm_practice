# 소수 찾기

import itertools

def solution(numbers):
    result = []
    list_nums = list(numbers)

    for i in list_nums:
        if int(i) > 1:
            for j in range(2, int(int(i) ** 0.5) + 1):
                if int(i) % j == 0:
                    break
            else:
                result.append(int(i))

    count = 2
    while len(list_nums) >= count:
        perm = list(itertools.permutations(list_nums, count))
        tmp = []
        for i in perm:
            tmp.append(''.join(list(i)))

        for i in tmp:
            if int(i) != 1:
                for j in range(2, int(int(i) ** 0.5) + 1):
                    if int(i) % j == 0:
                        break
                else:
                    result.append(int(i))
        count += 1

    answer = len(set(result))
    print(set(result))
    return answer

print(solution('9999992'))
