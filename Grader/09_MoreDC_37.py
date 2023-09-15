n = int(input())
depart = dict()
for i in range(n):
    a ,b = input().split()
    depart[a] = int(b)

n = int(input())
person = list()
for i in range(n):
    person.append(input().split())
for e in person: 
    e[1] = float(e[1])

person.sort(key = lambda x:x[1] ,reverse = True)
ans = list()
for e in person:
    for i in range(2 ,6):
        if depart[e[i]] > 0:
            ans.append([e[0] ,e[i]])
            depart[e[i]] -= 1
            break

ans.sort()
for e in ans:
    print(e[0] ,e[1])