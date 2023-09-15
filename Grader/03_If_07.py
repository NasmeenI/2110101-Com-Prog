n = input().strip()
if len(n) >= 10:
    x = float(n[0:len(n)-9+3])
    if x >= 10000:
        x = round(x/1000 ,0)
        print(int(x),end='')
    else:
        x = round(x/1000 ,1)
        print(x,end='')
    print('B')
elif len(n) >= 7:
    x = float(n[0:len(n)-6+3])
    if x >= 10000:
        x = round(x/1000 ,0)
        print(int(x),end='')
    else:
        x = round(x/1000 ,1)
        print(x,end='')
    print('M')
elif len(n) >= 4:
    x = float(n[0:len(n)-3+3])
    if x >= 10000:
        x = round(x/1000 ,0)
        print(int(x),end='')
    else:
        x = round(x/1000 ,1)
        print(x,end='')
    print('K')
else: print(n)