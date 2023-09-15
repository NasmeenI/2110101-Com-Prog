n = int(input())
ans = []
for i in range(n):
    s = [e for e in input().split()]
    ans.append(s)

s = input().split()
if s[0] == 'show':
    for e in ans:
        print(' '.join(map(lambda x: str(x),e)))
elif s[0] == 'get':
    ck = False
    for e in ans:
        if e[0] == s[1]:
            print(' '.join(map(lambda x: str(x),e)))
            ck = True
    if ck == False:
        print(s[1] ,'not found')
elif s[0] == 'avg':
    sum = 0
    for e in ans:
        sum += float(e[int(s[1])])
    print(round(sum/n ,4))
elif s[0] == 'max':
    mx = 0
    for e in ans:
        if mx < float(e[int(s[1])]): ind = ans.index(e)
        elif mx == float(e[int(s[1])]) and e[0] < ans[ind][0]: ind = ans.index(e) 
        mx = max(mx ,float(e[int(s[1])]))
    print(ans[ind][0] ,ans[ind][int(s[1])])
elif s[0] == 'sort':
    ans = sorted(ans, key = lambda x: (x[int(s[1])], x[0]))
    for e in ans:
        print(e[0],end=' ')