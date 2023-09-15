n = int(input())
l = [n]
while n != 1:
    if not n%2: n /= 2
    else: n = n*3+1
    l.append(n)

for i in range(max(0 ,len(l)-15) ,len(l)):
    print('{:.0f}'.format(int(l[i])) ,end='')
    if i != len(l)-1: print('->' ,end='')