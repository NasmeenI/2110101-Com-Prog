s = input()

num = 1
for i in range(len(s)):
    if i==len(s)-1 or s[i] != s[i+1]:
        print(s[i] ,num,end=' ')
        num = 1
    else:
        num += 1