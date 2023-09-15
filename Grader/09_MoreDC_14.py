file_courses = open('/Users/nasmeen/Documents/com_prog/Grader/' + input() ,"r")
file_teachers = open('/Users/nasmeen/Documents/com_prog/Grader/' + input() ,"r")
file_database = open('/Users/nasmeen/Documents/com_prog/Grader/' + input() ,"r")

courses = dict()
for line in file_courses:
    a ,b = line.strip().split(',')
    courses[a] = b

teachers = dict()
for line in file_teachers:
    a ,b = line.strip().split(',')
    teachers[a] = b

database = list()
for line in file_database:
    a ,b = line.strip().split(',')
    database.append([a ,b])

for [a,b] in database:
    if a not in courses or b not in teachers: print('record error')
    else: print(courses[a] + ',' + teachers[b])
