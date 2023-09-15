s = input()
d = dict()
order = list()
while(s != 'q'):
    a ,b = s.split(',')
    if b not in d: d[b] = [a]
    elif a not in d[b]: d[b].append(a)
    if b not in order: order += [b]
    s = input()

for k in order:
    v = d[k]
    print(k.strip() + ':',end=' ')
    for e in v:
        if v.index(e) != len(v)-1: print(e + ',',end=' ')
        else: print(e)