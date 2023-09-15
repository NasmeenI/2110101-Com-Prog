d = dict()
while True:
    s = input().split()
    if len(s) == 1: break

    if s[0] not in d: d[s[0]] = [s[1]]
    else: d[s[0]].append(s[1])
    if s[1] not in d: d[s[1]] = [s[0]]
    else: d[s[1]].append(s[0])

if s[0] not in d: 
    print(s[0])
    exit()

ans = [s[0]]
for e in d[s[0]]:
    if e not in ans: ans.append(e)
    for e1 in d[e]:
        if e1 not in ans: ans.append(e1)

ans.sort()
for e in ans:
    print(e)