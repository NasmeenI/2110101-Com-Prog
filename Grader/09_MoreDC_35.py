def func(person ,s):
    st = -1
    for i in range(4):
        if s in person[i]: st = i
    if st == -1:
        print('Not Found')
        exit()
    
    ind = list()
    for i in range(len(person[st])):
        if s == person[st][i]:
            ind.append(i)
    
    new_person = [[] ,[] ,[] ,[]]
    for e in ind:
        for i in range(4):
            new_person[i].append(person[i][e])
    return new_person

n = int(input())
person = [[] ,[] ,[] ,[]]
for i in range(n):
    a ,b ,c ,d = input().split()
    person[0].append(a)
    person[1].append(b)
    person[2].append(c)
    person[3].append(d)

input = [e for e in input().split()]
for e in input:
    person = func(person ,e)

ans = list()
for i in range(len(person[0])):
    l = list()
    for st in range(4):
        l.append(person[st][i])
    ans.append(l)

ans.sort()
for e1 in ans:
    for e2 in e1:
        print(e2 ,end=' ')
    print(end='\n')