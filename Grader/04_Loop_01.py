sum = 0.0
n = 0
while True:
    s = input()
    if s == 'q': break
    sum += float(s)
    n += 1

if n == 0: print("No Data")
else :
    ans = round(sum/n ,2)
    print(ans)