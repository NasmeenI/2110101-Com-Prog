n = int(input())
d1 = d2 = dict()
for i in range(n):
    a ,b = input().split()
    d1[a] = b
    d2[b] = a

n = int(input())
for i in range(n):
    a = input()
    if a in d1: print(d1[a])
    elif a in d2: print(d2[a])
    else: print('Not found')