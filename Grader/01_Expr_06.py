def cal(h1 ,m1 ,s1 ,h2 ,m2 ,s2):
    ds = (60 + (s2 - s1)) % 60
    if(s2 < s1):
        m2 -= 1

    dm = (60 + (m2 - m1)) % 60
    if(m2 < m1):
        h2 -= 1

    dh = (24 + (h2 - h1)) % 24
    return str(dh)+":"+str(dm)+":"+str(ds)

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
print(cal(h1 ,m1 ,s1 ,h2 ,m2 ,s2))