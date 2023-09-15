import math
a = float(input())
l = 0.0
u = a
x = (l+u)/2

while not(abs(a-x**2) <= (1/10**10)*max(a ,x**2)):
    if x**2 > a:
        u = x
    elif x**2 < a:
        l = x;
    x = (l+u)/2

ans = round(2*math.log(x ,10) ,6)
print(ans)