import math

n = int(input())
l = []
for i in range(n):
    x ,y = [float(e) for e in input().split()]
    l.append([math.sqrt(x**2 + y**2) ,i+1 ,x ,y])
l.sort()
print('#' + str(l[2][1]) + ': (' + str(l[2][2]) + ', ' + str(l[2][3]) + ')')