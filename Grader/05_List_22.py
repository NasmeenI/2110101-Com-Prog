def change_grade(x):
    if x == 'B+': x = 'A'
    elif x == 'B': x = 'B+'
    elif x == 'C+': x = 'B'
    elif x == 'C': x = 'C+'
    elif x == 'D+': x = 'C'
    elif x == 'D': x = 'D+'
    elif x == 'F': x = 'D'
    return x

s = input()
ids = []
grades = []
while s != 'q':
    id ,grade = s.split()
    ids.append(id)
    grades.append(grade)
    s = input()

uids = [e for e in input().split()]
for e in uids:
    ind = ids.index(e)
    grades[ind] = change_grade(grades[ind])

ans = []
for i in range(len(ids)):
    ans.append([ids[i] ,grades[i]])

ans.sort()
for id ,grade in ans:
    print(id ,grade)