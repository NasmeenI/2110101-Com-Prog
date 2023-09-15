x = input()
s = input()

l = [' ' ,'"' ,'(' ,')' ,',' ,'.' ,"'"]
ans = 0
for i in range(len(s)):
    if s[i:i+len(x)] == x and (i-1 < 0 or s[i-1] in l) and (i+len(x) >= len(s) or s[i+len(x)] in l):
        ans += 1
print(ans)