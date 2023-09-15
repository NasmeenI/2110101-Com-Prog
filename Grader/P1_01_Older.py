def cal(d ,m1 ,y):
    l = [0 ,0 ,31 ,59 ,90 ,120 ,151 ,181 ,212 ,243 ,273 ,304 ,334 ,365]
    months = [' ','January','February','March','April','May','June','July','August','September','October','November','December']
    m = months.index(m1)
    ans = d + l[m]
    if not (y - 543)%4 and m >= 3 and (not(y-543)%400 or (y-543)%100):
        ans += 1
    return ans

nn1 ,m1 ,d1 ,y1 = [e for e in input().split()]
nn2 ,m2 ,d2 ,y2 = [e for e in input().split()]
d1 = d1[:-1]
d2 = d2[:-1]

if int(y1) > int(y2): print(nn2)
elif int(y1) < int(y2): print(nn1)
else:
    dd1 = cal(int(d1) ,m1 ,int(y1))
    dd2 = cal(int(d2) ,m2 ,int(y2))
    if dd1 > dd2: print(nn2)
    elif dd1 < dd2: print(nn1)
    else: print(nn1 ,nn2)