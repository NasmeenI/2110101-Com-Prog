# 2565_2_Quiz_3_2 : 6532114921 Nasmeen Islam
# passworf for PDF : good_LUCK

a ,b ,c = input().split()
graduate = dict()
for i in range(int(a)):
    name ,faculty = input().split()
    graduate[name] = faculty

relative = dict()
for i in range(int(b)):
    inp = input().split()
    name = inp[0]; inp1 = inp[1:]
    x = set(graduate[e] for e in inp1)
    relative[name] = x

for i in range(int(c)):
    inp = input().split()
    x = relative[inp[0]]
    for j in range(len(inp)):
        x = x.intersection(relative[inp[j]])

    if len(x) == 0: print("None")
    else:
        x1 = list(x)
        x1.sort()
        print(' '.join(x1))