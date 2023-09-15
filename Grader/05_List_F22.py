def change_grade(x):
    if x == 'B+': x = 'A'
    elif x == 'B': x = 'B+'
    elif x == 'C+': x = 'B'
    elif x == 'C': x = 'C+'
    elif x == 'D+': x = 'C'
    elif x == 'D': x = 'D+'
    elif x == 'F': x = 'D'
    return x

def index_of(grades, ID):
    ind = -1
    for i in range(len(grades)):
        if grades[i][0] == ID:
            ind = i
    return ind

def upgrade(grades ,IDs):
    for e in IDs:
        ind = index_of(grades ,e)
        if ind != -1:
            grades[ind][1] = change_grade(grades[ind][1])
    grades.sort()

exec(input())
exec(input())
exec(input())