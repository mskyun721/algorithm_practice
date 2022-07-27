# 신규 아이디 추천

# 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다.
# 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
# 다음은 카카오 아이디의 규칙입니다.
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
# 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고
# 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# input : 1 <= new_id <= 1000
#     new_id는 길이 1 이상 1,000 이하인 문자열입니다.
#     new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
#     new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.
import sys

def solution(new_id):
    answer = ''

    # . => 46 / - => 45 / _ => 95
    befStr = ''
    for i in new_id:
        # 3단계 : '..' 연속 제거
        if i == '.' and befStr == '.':
            pass
        else:
            # 1단계 : 대문자치환
            if ord('A') <= ord(i) <= ord('Z'):
                answer += str(chr(ord(i) + 32))
            # 2단계 : 영어 소문자, 특수문자(. / - / _), 숫자 외 제거
            elif ord('a') <= ord(i) <= ord('z'):
                answer += i
            elif (ord(i) == 46 or ord(i) == 45 or ord(i) == 95) or i.isdigit():
                answer += i

        befStr = i
    print(answer)
    while True:
        # 4단계 : 처음 / 마지막 '.' 제거
        if len(answer) > 0 and answer[0] == '.':
            if len(answer) == 1:
                answer = ''
                break
            else:
                answer = answer[1:]
        elif len(answer) > 0 and answer[-1] == '.':
            answer = answer[:-1]
        else:
            break

    # 5단계 : 빈문자 -> 'a'
    if len(answer) == 0:
        answer = 'aaa'
    # 6단계 : 16자 이상 제거
    if len(answer) >= 16:
        answer = answer[:15]

        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계 : 2자 이하 글자 추가
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]

    return answer