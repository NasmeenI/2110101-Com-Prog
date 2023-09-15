n = int(input())
d = dict()
list_bidder = list()
for i in range(n):
    inp = input().split()
    if inp[0] == 'B': 
        person = inp[1]
        order = inp[2]
        price = int(inp[3])
        if person not in list_bidder: list_bidder.append(person)

        if order not in d: d[order] = [[person ,price]]
        else:
            for e in d[order]:
                if e[0] == person: 
                    d[order].remove(e)
                    break
            d[order].append([person ,price])
    elif inp[0] == 'W':
        person = inp[1]
        order = inp[2]

        if order not in d: continue
        for e in d[order]:
            if e[0] == person:
                d[order].remove(e)
                break
    else: continue

list_bidder.sort()
bidder = dict()
for key ,value in d.items():
    mx = 0
    winner = 'xNOTx'
    for e in value:
        if mx < e[1]:
            mx = e[1]
            winner = e[0]
    if winner == 'xNOTx': continue
    elif winner not in bidder: bidder[winner] = [[key ,mx]]
    else: bidder[winner].append([key ,mx])

for e in list_bidder:
    if e not in bidder: print(e + ': $0')
    else:
        l = list()
        price = 0
        for e1 in bidder[e]:
            l.append(e1[0])
            price += e1[1]
        l.sort()
        print(e + ': $' + str(price) + ' -> ' + ' '.join(l))