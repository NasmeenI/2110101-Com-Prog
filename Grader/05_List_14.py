l = [int(e) for e in input().split()]
ans = 0
for i in range(1 ,len(l)-1):
    if l[i-1] < l[i] > l[i+1]: ans += 1
print(ans)