d,m,y = [int(e) for e in input().split()]

y -= 543
n = 31
if m==4 or m==6 or m==9 or m==11:
  n = 30
else: 
  if m == 2:
    n = 28
    if not y%400:
      n = 29
    if not y%4 and y%100:
      n = 29

d += 15
if d > n:
  d -= n
  m += 1
if m > 12:
  m -= 12
  y += 1
y += 543

print(str(d) + '/' + str(m) + '/' + str(y))