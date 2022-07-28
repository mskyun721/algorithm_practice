# 소수 찾기

# 1<= numbers 길이 <= 7
# numbers = 0 ~ 9
import itertools

def solution(numbers):
    result = []
    list_nums = list(numbers)

    # 1자리 수 소수 확인
    for i in set(list_nums):
        if int(i) > 1:
            for j in range(2, int(int(i) ** 0.5) + 1):
                if int(i) % j == 0:
                    break
            else:
                result.append(int(i))

    # 1자리 이상 소수 확인
    count = 2
    while len(list_nums) >= count:
        # 순열
        perm = list(itertools.permutations(list_nums, count))
        tmp = [int(''.join(list(i))) for i in perm]

        for i in tmp:
            if int(i) != 1:
                for j in range(2, int(int(i) ** 0.5) + 1):
                    if int(i) % j == 0:
                        break
                else:
                    result.append(int(i))
        count += 1

    answer = len(set(result))

    return answer

print(solution('0'))
