import sys
input = sys.stdin.readline


n, m = map(int, input().split())
cnt = 0
students={}
schools={i:[] for i in range(m+1)}
s = []
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    students[i] = tmp[1:]
    s.extend(tmp[1:])
    for j in tmp[1:]:
        schools[j].append(i)

s = list(set(s))


while True:
    del_student = []
    stop = True
    for i in students:
        if len(students[i]) == 1:
            school = students[i][0]
            del_student.append(i)
            schools[school].remove(i)
            
            for j in students:
                if school in students[j]:
                    students[j].remove(school)

            stop = False
            cnt += 1
        else:
            for j in students[i]:
                if len(schools[j]) == 1:
                    del_student.append(i)
                    students[i].clear()
                    schools[j].remove(i)
                    
                    for k in schools:
                        if i in schools[k]:
                            schools[k].remove(i)
                    
                    stop = False
                    cnt += 1
                    break
    
    if stop:
        break
    else:
        for i in del_student:
            del students[i]


print(min(cnt + len(students), len(s)))

