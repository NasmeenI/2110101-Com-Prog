import math

n = int(input())
a = math.sqrt(math.pi*2)*n**(n+(1/2)) * math.e**(-n+(1/(12*n+1)))
b = math.sqrt(math.pi*2)*n**(n+(1/2)) * math.e**(-n+(1/(12*n)))
print(a)
print(b)