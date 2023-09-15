n = int(input())
total = list()
loser = list()
for i in range(n):
    a ,b = [e for e in input().split()]
    if a not in total: total.append(a)
    if b not in total: total.append(b)
    if b not in loser: loser.append(b) 

ans = list()
for e in total:
    if e not in loser: ans.append(e)
ans.sort()
print(ans)