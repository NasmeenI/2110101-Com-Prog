d = int(input())
m = int(input())
y = int(input())

l = [0 ,0 ,31 ,59 ,90 ,120 ,151 ,181 ,212 ,243 ,273 ,304 ,334 ,365]
ans = d + l[m]
if not (y - 543)%4 and m >= 3 and (not(y-543)%400 or (y-543)%100):
    ans += 1
print(ans)