n = int(input())
orders = dict(); sales = dict()
for i in range(n):
    a ,b = input().split()
    b = int(b)
    orders[a] = b

n = int(input())
sum = float()
for i in range(n):
    a ,b = input().split()
    b = int(b)
    if a in orders:
        sum += orders[a] * b
        if a in sales: sales[a] += orders[a] * b
        else: sales[a] = orders[a] * b

if not sales: print('No ice cream sales'); exit()

mx = -1
ans = list()
for k ,v in sales.items():
    if mx < v: ans = [k]; mx = v
    elif mx == v: ans.append(k)
ans.sort()

print('Total ice cream sales:' ,sum)
print('Top sales: ' ,end='')
for e in ans:
    if ans.index(e) != 0: print(', ',end='')
    print(e,end='')