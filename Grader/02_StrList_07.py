s = input()

a = s[4-1] + s[11-1] + s[18-1] + s[25-1] + s[32-1]
b = s[8-1] + s[13-1] + s[18-1] + s[23-1] + s[28-1]
c = int(a) + int(b) + 10000
d = str(c)
e = d[-4:-1]
f = int(e[0]) + int(e[1]) + int(e[2])
g = str(f)
h = int(g[-1]) + 1

digit = ['A' ,'B' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J']

ans = e + digit[h-1]
print(ans)