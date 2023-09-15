def check(s):
    s = s.upper()
    for e in s:
        if e not in 'ATGC':
            print('Invalid DNA')
            exit()
    return s

def R(s):
    d = {'A':'T' ,'T':'A' ,'G':'C' ,'C':'G'} 
    for i in range(len(s)): s = s[:i] + d[s[i]] + s[i+1:]
    print(s[::-1])

def F(s):
    d = {'A':0 ,'T':0 ,'G':0 ,'C':0}
    for e in s: d[e] += 1
    print('A=' + str(d['A']) + ', T=' + str(d['T']) + ', G=' + str(d['G']) + ', C=' + str(d['C']))

def D(s):
    x = input().strip()
    ans = 0
    for i in range(len(s)-1):
        if s[i:i+2] == x: ans += 1
    print(ans)

s = input().strip()
x = input().strip()
s = check(s)

if x == 'R': R(s)
elif x == 'F': F(s)
elif x == 'D': D(s)