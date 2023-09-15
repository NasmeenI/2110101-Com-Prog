s = input()
n = int(input())
l = []
for i in range(n):
    l.append(input())
    if len(l[i]) != len(l[max(0 ,i-1)]):
        print('Invalid size')
        exit()

if s == '90': st = 0
elif s == 'flip': st = 1
elif s == '180': st = 2

data_n = [[len(l[0]) ,n] ,[n ,len(l[0])] ,[n ,len(l[0])]]
ni = data_n[st][0]
nj = data_n[st][1]
ans = [[0 for e in range(nj)] for e in range(ni)]

for i in range(ni):
    for j in range(nj):
        if st == 0: ans[i][j] = l[n-j-1][i]
        elif st == 1: ans[i][j] = l[i][nj-j-1]
        elif st == 2: ans[i][j] = l[ni-i-1][nj-j-1]

for i in range(ni):
    for j in range(nj):
        print(ans[i][j] ,end='')
    print('\n',end='')