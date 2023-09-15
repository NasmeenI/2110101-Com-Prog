a = float(input())
l = 0
u = 0
a1 = a
while a1 > 0:
    a1 //= 10
    u += 1
x = (l+u)/2

while not(abs(a-10**x) <= (10**-10)*max(a ,10**x)):
    if 10**x > a:
        u = x
    else:
        l = x
    x = (l+u)/2

print(round(x ,6))