def solution(p):
    answer = ''

    if stack(list(p)):
        answer = p
    else:
        answer = regular(p)

    return answer


def stack(arr):
    result = True
    if arr[0] == '(':
        list_ = ['(']

        for i in range(1, len(arr)):
            if arr[i] == ')':
                if list_:
                    if list_.pop() == '(':
                        pass
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
            else:
                list_.append(arr[i])

        if list_:
            result = False
    else:
        result = False

    return result


def regular(str_):
    dic_ = {'(':')', ')':'('}
    result = ''
    u, v = '', ''
    count = 1
    if str_ != '':
        while True:
            if str_[:(2*count)].count('(') == str_[:(2*count)].count(')'):
                u = str_[:(2*count)]
                v = str_[2*count:]
                u2 = ''
                if len(u) == 2:
                    u2 = '()'
                else:
                    u2 = '('
                    for i in range(1, len(u)-1):
                        u2 += dic_[u[i]]

                    u2 += ')'

                if v != '':
                    result = u2 + regular(v)
                else:
                    result = u2
                break
            else:
                count += 1

    return result


# print(solution('(()())()'))
# print(solution(')('))
print(solution('()))((()'))
print(solution('()()()'))

