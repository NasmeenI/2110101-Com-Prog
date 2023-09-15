from math import floor

sum_a = sum_b = sum_d = 0
for i in range(9):
    a ,b ,c = [int(e) for e in input().split()]
    if c: d = min(a+2 ,b)
    else: d = 0
    sum_a += a
    sum_b += b
    sum_d += d

x = floor((1.5*sum_d - sum_a)*0.8)
y = sum_b - x
print(sum_b)
print(x)
print(y)