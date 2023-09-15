s = input().split()
l = []
l.append(float(s[0]))
l.append(float(s[1]))
l.append(float(s[2]))
l.append(float(s[3]))

mn = 0
mx = 0
ans = l[0] + l[1] + l[2] + l[3]

if l[mn] > l[1]:
    mn = 1
if l[mn] > l[2]:
    mn = 2
if l[mn] > l[3]:
    mn = 3
if l[mx] < l[1]:
    mx = 1
if l[mx] < l[2]:
    mx = 2
if l[mx] < l[3]:
    mx = 3

ans = round((ans - l[mn] - l[mx])/2 ,2)
print(ans)