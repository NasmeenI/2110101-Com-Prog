# 2565_1_Quiz_1_2 : 6532114921 Nasmeen Islam
# passworf for PDF : quiz_QUIZ

def f1(a ,b ,c):
    l = [a ,b ,c]
    mn = 1010
    for e in l:
        if mn > e and e > 0: mn = e
    return mn

def f2(a ,b ,c):
    l = [a ,b ,c]
    mx = -1010
    for e in l:
        if mx < e and e < 0: mx = e
    return mx

def f3(a ,b ,c):
    sum = str(a + b + c)
    if sum[0] == '-': return sum[1]
    else: return sum[0]

def f4(a ,b ,c):
    sum = str(a + b + c)
    return sum[len(sum)-1]

def main():
    s1 ,s2 ,a ,b ,c = [int(e) for e in input().split()]
    if s1==0 and s2==0 : print(f1(a ,b ,c))
    elif s1==0 and s2==1: print(f2(a ,b ,c))
    elif s1==1 and s1==0: print(f3(a ,b ,c))
    elif s1==1 and s1==1: print(f4(a ,b ,c))
    else: print('Error')

exec(input().strip())