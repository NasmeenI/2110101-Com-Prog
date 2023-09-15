i = 0
mn = [1e9 ,1e9]
mx = [-1e9 ,-1e9]
while True:
    s = input()
    if s == 'Zig-Zag':
        st = 0
        break
    elif s == 'Zag-Zig':
        st = 1
        break
    s1 = s.split()  
    mn[0] = min(mn[0] ,int(s1[(0+i)%2]))
    mn[1] = min(mn[1] ,int(s1[(1+i)%2]))
    mx[0] = max(mx[0] ,int(s1[(1+i)%2]))
    mx[1] = max(mx[1] ,int(s1[(0+i)%2]))
    i += 1

print(mn[st] ,mx[st])