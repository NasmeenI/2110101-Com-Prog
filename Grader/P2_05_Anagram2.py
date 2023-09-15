s1 = input(); s1_0 = s1.lower(); s1_1 = s1_0
s2 = input(); s2_0 = s2.lower(); s2_1 = s2_0
mydict_s1 = dict()
mydict_s2 = dict()

for e in s1_0:
    if not e.isalpha(): continue
    if e not in s2_1:
        if e in mydict_s1: mydict_s1[e] += 1
        else: mydict_s1[e] = 1
    else: s2_1 = s2_1[:s2_1.index(e)] + s2_1[s2_1.index(e)+1:]

for e in s2_0:
    if not e.isalpha(): continue
    if e not in s1_1:
        if e in mydict_s2: mydict_s2[e] += 1
        else: mydict_s2[e] = 1
    else: s1_1 = s1_1[:s1_1.index(e)] + s1_1[s1_1.index(e)+1:]

ans_s1 = list(); ans_s2 = list()
for k ,v in mydict_s1.items():
    ans_s1.append([k ,v])
for k ,v in mydict_s2.items():
    ans_s2.append([k ,v])
ans_s1.sort()
ans_s2.sort()

print(s1)
if len(ans_s1) == 0: print(' - None')
for e in ans_s1:
    print(' - remove' ,e[1] ,e[0] ,end='')
    if e[1] > 1: print("'s")
    else: print('\n' ,end='')

print(s2)
if len(ans_s2) == 0: print(' - None')
for e in ans_s2:
    print(' - remove' ,e[1] ,e[0] ,end='')
    if e[1] > 1: print("'s")
    else: print('\n' ,end='')