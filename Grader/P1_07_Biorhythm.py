import math

def blue(d, m, y):
    l = [0 ,0 ,31 ,59 ,90 ,120 ,151 ,181 ,212 ,243 ,273 ,304 ,334 ,365]
    ans = d + l[m]
    if not (y - 543)%4 and m >= 3 and (not(y-543)%400 or (y-543)%100):
        ans += 1
    return ans-1

def black(y1 ,y2):
    return 365*(y2-y1-1)

def red(d ,m ,y):
    l = [365 ,334 ,306 ,275 ,245 ,214 ,184 ,153 ,122 ,92 ,61 ,31 ,0]
    month = [0 ,31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
    ans = month[m] - d + 1 + l[m]
    if not (y - 543)%4 and m <= 2 and (not(y-543)%400 or (y-543)%100):
        ans += 1
    return ans

d1 ,m1 ,y1 ,d2 ,m2 ,y2 = [int(e) for e in input().split()]
t = red(d1 ,m1 ,y1) + black(y1 ,y2) + blue(d2 ,m2 ,y2)
physical = math.sin((2*math.pi*t)/23)
emotional = math.sin((2*math.pi*t)/28)
intellectual = math.sin((2*math.pi*t)/33)

print(t ,"{:.2f}".format(physical) ,"{:.2f}".format(emotional) ,"{:.2f}".format(intellectual))