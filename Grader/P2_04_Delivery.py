error = list()
delivered = list()
in_month = [0 ,31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
type_delivery = {'E':1 ,'Q':3 ,'N':7 ,'F':14}
while True:
    data = input().strip().split()
    if data[0] == 'END': break
    id ,type_d ,d ,m ,y = data; d = int(d); m = int(m); y = int(y)
    
    if (y-543)%400 == 0 or ((y-543)%4 == 0 and (y-543)%100 != 0): in_month[2] = 29
    else: in_month[2] = 28

    if y < 2558: error.append(data + ['--> Invalid year']) 
    elif m > 12 or m < 1: error.append(data + ['--> Invalid month'])
    elif d > in_month[m] or d < 1: error.append(data + ['--> Invalid date'])
    elif type_d not in type_delivery: error.append(data + ['--> Invalid delivery type'])
    else:
        d = d + type_delivery[type_d]
        if d > in_month[m]:
            d -= in_month[m]
            m += 1
        if m > 12:
            m -= 12
            y += 1
        delivered.append([id ,type_d ,d ,m ,y])

for e in error: 
    print('Error:' ,' '.join(e))

ans = list()
for e in delivered:
    ans.append([int(e[4]) ,int(e[3]) ,int(e[2]) ,e[0]])
ans.sort()

for e in ans:
    print(e[3] + ': delivered on ' + str(e[2]) +'/' + str(e[1]) + '/' + str(e[0]))