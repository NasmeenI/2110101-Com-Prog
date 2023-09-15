n = int(input())
ans = list()
for k in range(n):
    s = input()
    for i in range(len(s)):
        if s[i] == '.':  continue
        s = '.'*(i//2) + s[i:]
        ans.append(s)
        break
for e in ans: 
    print(e)