n = int(input())
k = int(input())
if ((n < 1 or n > 15) and (k < 1 or k > 100)): print('Invalid n and k')
elif n < 1 or n > 15: print('Invalid n')
elif k < 1 or k > 100: print('Invalid k')
if n < 1 or n > 15 or k < 1 or k > 100: exit()
l = ['0' ,'1']
for i in range(n-1):
    l1 = l[-1::-1]
    l += l1
    for j in range(len(l)):
        if j < len(l)/2: l[j] = '0' + l[j]
        else: l[j] = '1' + l[j]

for i in range(1 ,k):
    print(str(i) + '-'*(n+1-len(str(i))) ,end='')
print(str(k) + '-'*(n-len(str(k))))

for i in range(0 ,len(l) ,k):
    print(','.join(l[i:i+k]))