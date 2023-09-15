n = int(input())

l1 = []
l2 = []
for i in range(n):
    x ,y = [int(e) for e in input().split()]
    l1.append(x)
    l2.append(y)
    if i%2:
        l1[i] ,l2[i] = l2[i] ,l1[i]

mn1 ,mn2 = l1[0] ,l2[0]
mx1 ,mx2 = l1[0] ,l2[0]
for i in range(n):
    mn1 = min(mn1 ,l1[i])
    mn2 = min(mn2 ,l2[i])
    mx1 = max(mx1 ,l1[i])
    mx2 = max(mx2 ,l2[i])

ansmn = ansmx = 0
s = input()
if s == "Zig-Zag":
    ansmn = mn1
    ansmx = mx2
else:
    ansmn = mn2
    ansmx = mx1

print(ansmn ,ansmx)