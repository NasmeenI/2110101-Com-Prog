def convex_polygon_area(p):
    p += [p[0]]
    ans = 0
    for i in range(len(p)-1):
        ans += p[i][0]*p[i+1][1] - p[i][1]*p[i+1][0]
    return abs(ans)/2

def is_heterogram(s):
    s = s.upper()
    l = list()
    for e in s:
        if not e.isalpha(): continue
        if e in l: return False
        else: l.append(e)
    return True

def replace_ignorecase(s, a, b):
    last = 0
    while True:
        ind = s.upper().find(a.upper() ,last)
        if ind == -1: break
        
        s = s[:ind] + b + s[ind+len(a):]
        last = ind + len(b)
    return s

def top3(votes):
    l = list(); ans = list()
    for k ,v in votes.items():
        l.append([-v ,k])
    l.sort()
    for e in l:
        ans.append(e[1])
    if len(ans) > 3: return ans[:3]
    else: return ans

for k in range(2):
    exec(input().strip())