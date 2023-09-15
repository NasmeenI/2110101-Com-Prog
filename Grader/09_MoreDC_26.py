n = int(input())
d = dict()
order = list()
for i in range(n):
    id ,city = input().split(':')
    citys = city.split(',')
    d[id] = []
    for e in citys: d[id].append(e.strip())
    order += [id]

ID = input()
ans = []
for id ,citys in d.items():
    if id == ID: continue
    for e in citys:
        if e in d[ID]:
            ans.append(id)
            break
    
if len(ans): 
    for e in order:
        if e in ans: print(e)
else: print('Not Found')