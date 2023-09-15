# 2565_2_Quiz_3_1 : 6532114921 Nasmeen Islam
# passworf for PDF : good_LUCK

team = dict()
for i in range(int(input())):
    name ,country = input().split()
    team[name] = country

while True:
    group = input().split()
    if group == ['q']: break

    ck = True
    for i in range(len(group)):
        for j in range(i+1 ,len(group)):
            if group[i] not in team or group[j] not in team:
                ck = False
                continue
            if team[group[i]] == team[group[j]]:
                ck = False

    if ck: print('OK')
    else: print('Not OK')