s = input()
l = s.split(',')
l[0] = l[0][1:]
l[2] = l[2][:-1]

s1 = input()
l1 = s1.split(',')
l1[0] = l1[0][1:]
l1[2] = l1[2][:-1]

nl = []
nl.append(float(l[0]))
nl.append(float(l[1]))
nl.append(float(l[2]))

nl1 = []
nl1.append(float(l1[0]))
nl1.append(float(l1[1]))
nl1.append(float(l1[2]))

ans = []
ans.append(nl[0] + nl1[0])
ans.append(nl[1] + nl1[1])
ans.append(nl[2] + nl1[2])

print(nl ," + " ,end='')
print(nl1 ," = " ,end='')
print(ans)