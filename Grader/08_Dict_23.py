n = int(input())
name = dict(); phone = dict()
for i in range(n):
    a ,b ,c = [e for e in input().split()]
    name[a+' '+b] = c
    phone[c] = a+' '+b

n = int(input())
for i in range(n):
    x = input()
    if ' ' in x:
        if x in name: print(x ,'-->' ,name[x])
        else: print(x ,'-->' ,'Not found')
    else:
        if x in phone: print(x ,'-->' ,phone[x])
        else: print(x ,'-->' ,'Not found')
