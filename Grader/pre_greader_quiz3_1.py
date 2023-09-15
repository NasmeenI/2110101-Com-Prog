week = int(input())
price ,fast ,slow = [0.0] ,list() ,list()

for i in range(week):
    inp = input().split(',')
    price += [float(e) for e in inp]

sum = 0.0
for i in range(1 ,8):
    sum += price[i]
fast0 = sum/7
sum = 0.0
for i in range(1 ,15):
    sum += price[i]
slow0 = sum/14

fast += [fast0]
slow += [slow0]
sell ,buy = list() ,list()
for day in range(1 ,7*week+1):
    fast += [ (2/(1+7))*price[day] + fast[day-1]*(1-(2/(1+7))) ]
    slow += [ (2/(1+14))*price[day] + fast[day-1]*(1-(2/(1+14))) ]

    if day >= 14 and fast[day] == slow[day]:
        if fast[day+1] > slow[day+1]: sell.append(fast[day])
        elif fast[day+1] < slow[day+1]: buy.append(fast[day])

print(buy)
print(sell)