# 신고 결과 받기

# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.
# 무지가 개발하려는 시스템은 다음과 같습니다.
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
# input example
# 1. id_list : ["muzi", "frodo", "apeach", "neo"]
#   개수 : 2 <= id_list <= 1000 /
#   원소 길이 : 1<= id_list <= 10
#   알파벳 소문자 / 중복 x
# 2. report : ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#   개수 : 1 ≤ report ≤ 200000
#   원소 길이 : 3 ≤ report ≤ 21
#   이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
#   자기 자신을 신고하는 경우는 없습니다.
# 3. k = 2(정수)
#   1 ≤ k ≤ 200
import sys

def solution(id_list, report, k):
    user = {x : [] for x in id_list}
    reporter = {x : 0 for x in id_list}
    sendCount = {x: 0 for x in id_list}
    for i in report:
        x, y = i.split()

        if x not in user[y]:
            user[y].append(x)
            reporter[y] += 1

    for i in reporter:
        if reporter[i] >= k:
            for j in user[i]:
                sendCount[j] += 1

    return list(sendCount.values())

