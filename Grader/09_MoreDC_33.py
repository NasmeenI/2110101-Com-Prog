def add_poly(p1 ,p2):
    ind1 = ind2 = 0
    ans = list()
    while True:
        if ind1 == len(p1) and ind2 == len(p2): break
        elif ind1 == len(p1):
            ans += p2[ind2:len(p2)]
            break
        elif ind2 == len(p2):
            ans += p1[ind1:len(p1)]
            break

        a = p1[ind1]
        b = p2[ind2]    
        if a[1] == b[1]: 
            ans.append((a[0]+b[0] ,a[1]))
            ind1 += 1
            ind2 += 1
        elif a[1] > b[1]:
            ans.append(a)
            ind1 += 1
        elif a[1] < b[1]:
            ans.append(b)
            ind2 += 1

    i = 0
    while True:
        if i >= len(ans): break
        if ans[i][0] == 0:
            ans.pop(i)
            i -=1
        i += 1
    return ans

def func(val):
    return val[1]

def mult_poly(p1 ,p2):
    ans = list()
    for e1 in p1:
        for e2 in p2:
            ans.append((e1[0]*e2[0] ,e1[1]+e2[1]))
    ans.sort(key = lambda x:x[1] ,reverse = True)

    i = 0
    while True:
        if i >= len(ans)-1: break
        if ans[i][1] == ans[i+1][1]: 
            ans[i] = (ans[i][0]+ans[i+1][0] ,ans[i][1])
            ans.pop(i+1)
            i -= 1
        i += 1
    return ans

for i in range(3):
    exec(input().strip())