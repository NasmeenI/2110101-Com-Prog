# 2565_2_Quiz_3_3 : 6532114921 Nasmeen Islam
# passworf for PDF : good_LUCK

def f_find(ally ,x):
    for i in range(len(ally)):
        if x in ally[i]: return ally[i]
    return [x]

ally ,enemy ,table = list() ,list() ,list()
while True:
    inp = input().split()
    if inp == ['End']: break
    elif inp[0] == 'Ally': ally.append(inp[1:])
    elif inp[0] == 'Enemy': enemy.append(inp[1:])
    elif inp[0] == 'Table': table.append(inp[1:])

for i in range(len(enemy)):
    for e in enemy[i]:
        ck = True
        for j in range(len(ally)):
            if e in ally[j]: ck = False
        if ck: ally.append([e])

enemy_1 = list()
for i in range(len(ally)):
    x = []
    for e in ally[i]:
        for j in range(len(enemy)):
            if e == enemy[j][0]:
                x += f_find(ally ,enemy[j][1])
            elif e == enemy[j][1]:
                x += f_find(ally ,enemy[j][0])
    enemy_1.append([ally[i] ,x])

for x in table:
    ck = True
    for i in range(len(x)):
        if i == len(x)-1: a ,b = x[i] ,x[0]
        else: a ,b = x[i] ,x[i+1]
        for e in enemy_1:
            if a in e[0] and b in e[1]: ck = False
            elif a in e[1] and b in e[0]: ck = False

    if ck: print('Okay')
    else: print('No')