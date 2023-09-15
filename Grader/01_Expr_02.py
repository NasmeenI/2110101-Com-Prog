import math

a = float(input())
b = float(input())
c = float(input())

ans1 = round(( -b - math.sqrt(b**2-(4*a*c)) ) / (2*a) ,3)
ans2 = round(( -b + math.sqrt(b**2-(4*a*c)) ) / (2*a) ,3)

print(ans1)
print(ans2)