a = {'A':1 ,'2':2 ,'3':3 ,'4':4 ,'5':5 ,'6':6 ,'7':7 ,'8':8 ,'9':9 ,'T':10 ,'J':11 ,'Q':12 ,'K':13}
b = {'C':1 ,'D':2 ,'H':3 ,'S':4}

s = input()
for i in range(2 ,len(s) ,2):
    if a[s[i]] == a[s[i-2]]:
        x = b[s[i+1]] - b[s[i-1]]
        if x  <0: print('+',end="")
        elif x > 0: print('-',end="")
        print(abs(x),end="")
    else:
        x = a[s[i]] - a[s[i-2]]
        if x < 0: print('+',end="")
        elif x > 0: print('-',end="")
        print(abs(x),end="")