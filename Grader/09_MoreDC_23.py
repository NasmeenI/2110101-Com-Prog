def cal(s ,st):
    if st == 0:
        a ,b = s.split(':')
        return 60*int(a) + int(b)
    elif st == 1:
        a = str(s//60)
        b = str(s%60)
        if len(b) == 1: b = str(0) + b
        return a + ':' + b

n = int(input())
d = dict()
for i in range(n):
    s = [e.strip() for e in input().split(',')]
    if s[2] not in d: d[s[2]] = cal(s[3] ,0)
    else: d[s[2]] += cal(s[3] ,0)

ans = list()
for k ,v in d.items():
    ans.append([v ,k])
ans.sort(reverse = True)
for i in range(len(ans)):
    if i == 3: exit()
    print(ans[i][1] ,'-->' ,cal(ans[i][0] ,1))