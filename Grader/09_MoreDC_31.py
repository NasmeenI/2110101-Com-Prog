import math

def gcd(a ,b):
    while b != 0:
        a ,b = b ,a%b
    return a

def is_coprime(a ,b ,c):
    if gcd(gcd(a ,b) ,gcd(b ,c)) == 1: return True
    return False

def primitive_Pythagorean_triples(max_len):
    ans = list()
    for c in range(1 ,max_len+1):
        for a in range(1 ,c):
            b = math.sqrt(c**2 - a**2)
            if b < a: break
            if b%1 == 0 and is_coprime(a ,b ,c): 
                ans.append([a ,int(b) ,c])
    return ans

exec(input().strip())