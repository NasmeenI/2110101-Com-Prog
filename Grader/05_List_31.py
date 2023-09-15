def cut(s):
    n = int(len(s)/2)
    s = s[n:] + s[:n]
    return s

def scream(s):
    n = int(len(s)/2)
    s1 = s[:n]
    s2 = s[n:]

    l = []
    for i in range(n):
        l.append(s1[i])
        l.append(s2[i])
    return l

s = [e for e in input().split()]
s1 = input()

for e in s1:
    if e == 'C':
        s = cut(s)
    elif e == 'S':
        s = scream(s)
for e in s:
    print(e,end=' ')