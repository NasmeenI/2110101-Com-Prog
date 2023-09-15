def one(s):
    if len(s) >= 8: return 
    print('Less than 8 characters')
    return False

def two(s):
    ch = [False] * 4
    for e in s: 
        if not False in ch: break
        if e >= 'a' and e <= 'z': ch[0] = True
        elif e >= 'A' and e <= 'Z': ch[1] = True
        elif e >= '0' and e <= '9': ch[2] = True
        else: ch[3] = True
    
    if not ch[0]: print('No lowercase letters')
    if not ch[1]: print('No uppercase letters')
    if not ch[2]: print('No numbers')
    if not ch[3]: print('No symbols')
    if False in ch: return False

def three(s):
    for i in range(3 ,len(s)):
        if s[i-3] == s[i-2] and s[i-1] == s[i-2] and s[i] == s[i-1]: 
            print('Character repetition')
            return False
    
def four(s):
    for i in range(3 ,len(s)):
        if s[i] < '0' or s[i] > '9': continue
        if (ord(s[i])-ord(s[i-1]) == 1 or ord(s[i])-ord(s[i-1]) == -9) and ord(s[i-1])-ord(s[i-2]) == 1 and ord(s[i-2])-ord(s[i-3]) == 1: 
            print('Number sequence')
            return False
        if ord(s[i])-ord(s[i-1]) == -1 and ord(s[i-1])-ord(s[i-2]) == -1 and (ord(s[i-2])-ord(s[i-3]) == -1 or ord(s[i-2])-ord(s[i-3]) == 9): 
            print('Number sequence')
            return False

def five(s):
    s = s.lower()
    for i in range(3 ,len(s)):
        if s[i] < 'a' or s[i] > 'z': continue
        if ord(s[i])-ord(s[i-1]) == 1 and ord(s[i-1])-ord(s[i-2]) == 1 and ord(s[i-2])-ord(s[i-3]) == 1: 
            print('Letter sequence')
            return False
        if ord(s[i])-ord(s[i-1]) == -1 and ord(s[i-1])-ord(s[i-2]) == -1 and ord(s[i-2])-ord(s[i-3]) == -1: 
            print('Letter sequence')
            return False

def six(s):
    s = s.upper()
    s1 = ['!@#$%^&*()_+' ,'QWERTYUIOP' ,'ASDFGHJKL' ,'ZXCVBNM']
    for i in range(3 ,len(s)):
        for j in range(4):
            if s[i] in s1[j] and s1[j].index(s[i]) >= 3:
                ind = s1[j].index(s[i])
                if s[i-1] == s1[j][ind-1] and s[i-2] == s1[j][ind-2] and s[i-3] == s1[j][ind-3]: 
                    print('Keyboard pattern')
                    return False
            if s[i] in s1[j] and s1[j].index(s[i]) <= len(s1[j])-4:
                ind = s1[j].index(s[i])
                if s[i-1] == s1[j][ind+1] and s[i-2] == s1[j][ind+2] and s[i-3] == s1[j][ind+3]: 
                    print('Keyboard pattern')
                    return False
        
s = input()
l = [one(s) ,two(s) ,three(s) ,four(s) ,five(s) ,six(s)]
if not False in l: print('OK')