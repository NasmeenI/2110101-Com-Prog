s = input().lower()
d = dict()
for e in s:
    if e < 'A' or e > 'z': continue
    if e in d: d[e] += 1
    else: d[e] = 1

l = list()
for k ,v in d.items():
    l.append([-v ,k])
l.sort()

for v ,k in l:
    print(k ,'->' ,-v)