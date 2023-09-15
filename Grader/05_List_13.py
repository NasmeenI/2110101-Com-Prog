n = int(input())
l = []
st = 1
for i in range(n):
    x = int(input())
    if st == 1:
        l.append(x)
        st = 2
    else:
        l.insert(0 ,x)
        st = 1

n1 = [int(e) for e in input().split()]
for e in n1:
    if st == 1:
        l.append(e)
        st = 2
    else:
        l.insert(0 ,e)
        st = 1
    
n2 = int(input())
while n2 != -1:
    if st == 1:
        l.append(n2)
        st = 2
    else:
        l.insert(0 ,n2)
        st = 1
    n2 = int(input())

print(l)