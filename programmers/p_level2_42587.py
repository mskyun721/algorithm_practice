# 프린터
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# input
#   priorities : 1 <= list 개수 <= 100
#   location : 0 <= location <= list 개수 - 1

def solution(priorities, location):
    answer = 0
    prior = {i:priorities.count(i) for i in set(priorities)}
    arr = [[i, priorities[i]] for i in range(len(priorities))]
    list_prior = list(prior.keys())
    list_prior.sort(reverse=True)
    result = []
    count = 0

    for i in list_prior:
        priorCount = 0
        while len(result) < len(priorities):
            seq, p = arr[count % len(priorities)]
            count += 1
            if i == p and seq not in result:
                result.append(seq)
                priorCount += 1

            if prior[i] == priorCount:
                break
    answer = result.index(location) + 1
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))