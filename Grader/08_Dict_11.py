def reverse(d):
    d1 = dict()
    for k,v in d.items():
        d1[v] = k
    return d1

def keys(d ,value):
    l = list()
    for k,v in d.items():
        if v == value: l.append(k)
    return l

exec(input().strip())