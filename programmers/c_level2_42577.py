# 전화번호 목록
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# input
#   phone_book : 1 <= 개수 <= 1000000
#                1 <= 원소길이 <= 20
#                중복 x

def solution(phone_book):
    phone_book.sort(key=len)
    hash_table = {}

    min_len = len(phone_book[0])

    for target in phone_book:
        hash_table[hash(target)] = target
        for i in range(min_len,len(target)):
            try:
                if hash_table[hash(target[0:i])]:
                    return False
            except KeyError:
                pass

    return True