n = int(input())
d = dict()
for i in range(n):
    title = input()
    content = input().split()

    d1 = dict()
    for e in content:
        if e not in d1: d1[e] = 1
        else: d1[e] += 1
    d1['xTOTALx'] = len(content)
    d[title] = d1

while True:
    x = input()
    if x == '-1': break

    mx = 0
    for key ,value in d.items():
        if x not in value: continue
        conf = value[x]/(value['xTOTALx']*len(value))
        if mx < conf: 
            mx = conf
            ans = key
    if mx == 0: print('NOT FOUND')
    else: print(ans)