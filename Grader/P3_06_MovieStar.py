n = int(input())
d = dict()
for i in range(n):
    movie ,a ,b = input().split(', ')
    if a not in d: d[a] = [movie]
    else: d[a].append(movie)
    if b not in d: d[b] = [movie]
    else: d[b].append(movie)

l = [e for e in input().split(', ')]
for e in l:
    if e not in d: print(e + ' -> ' + 'Not found')
    else: print(e + ' -> ' + ', '.join(d[e]))