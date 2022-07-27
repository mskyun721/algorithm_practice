# 더 맵게
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# input
#   scoville : 2 <= scoville <= 1000000
#   k : 0 <= k <= 1000000

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        min_ = heapq.heappop(scoville)

        if min_ < K:
            min2_ = heapq.heappop(scoville)
            heapq.heappush(scoville, min_ + (min2_*2))
            answer += 1

    if len(scoville) == 1:
        if scoville[0] < K:
            answer = -1

    return answer


print(solution([1, 2], 7))