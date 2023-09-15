l = [int(e) for e in input().split()]
l.sort()
l1 = []
ans = 0
for i in range(len(l)):
    if i==len(l)-1 or l[i] != l[i+1]:
        ans += 1
        l1.append(l[i])
print(ans,end='\n') 
print(l1[:min(len(l1) ,10)])